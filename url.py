#!/usr/bin/env python3
"""
Script to find HLS master playlist URLs that combine audio and video streams
from JSON files in the same directory.
"""

import json
import os
import glob
from pathlib import Path

def has_audio_and_video_streams(streaming_playlists):
    """
    Check if streaming playlists contain both audio and video streams.
    Returns True if there are separate audio-only and video-only files.
    """
    for playlist in streaming_playlists:
        if 'files' not in playlist:
            continue
            
        has_audio_only = False
        has_video_only = False
        
        for file_info in playlist['files']:
            if file_info.get('hasAudio') and not file_info.get('hasVideo'):
                has_audio_only = True
            elif file_info.get('hasVideo') and not file_info.get('hasAudio'):
                has_video_only = True
        
        # If we have both audio-only and video-only files, the master playlist combines them
        if has_audio_only and has_video_only:
            return True, playlist.get('playlistUrl')
    
    return False, None

def find_master_playlist_urls(filename="video_data.json"):
    """
    Extract master playlist URLs that combine audio and video streams
    from a specific JSON file.
    """
    results = []
    
    if not os.path.exists(filename):
        print(f"File not found: {filename}")
        return results
    
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Check if this JSON has the expected structure
        if 'streamingPlaylists' not in data:
            print(f"No 'streamingPlaylists' found in {filename}")
            return results
        
        has_combined_streams, master_url = has_audio_and_video_streams(data['streamingPlaylists'])
        
        if has_combined_streams and master_url:
            # Get resolution info from video files
            resolutions = []
            for playlist in data['streamingPlaylists']:
                for file_info in playlist.get('files', []):
                    if file_info.get('hasVideo') and not file_info.get('hasAudio'):
                        resolution = file_info.get('resolution', {})
                        width = file_info.get('width', 0)
                        height = file_info.get('height', 0)
                        resolutions.append({
                            'label': resolution.get('label', 'Unknown'),
                            'width': width,
                            'height': height,
                            'size': file_info.get('size', 0),
                            'fps': file_info.get('fps', 0)
                        })
            
            video_info = {
                'file': filename,
                'name': data.get('name', 'Unknown'),
                'uuid': data.get('uuid', 'Unknown'),
                'duration': data.get('duration', 0),
                'master_playlist_url': master_url,
                'video_url': data.get('url', 'Unknown'),
                'resolutions': resolutions
            }
            results.append(video_info)
        else:
            print("No combined audio+video streams found in this file.")
            
    except json.JSONDecodeError as e:
        print(f"Error parsing {filename}: {e}")
    except Exception as e:
        print(f"Error processing {filename}: {e}")
    
    return results

def main():
    """Main function to run the script."""
    current_dir = os.getcwd()
    print(f"Searching for JSON files in: {current_dir}")
    
    results = find_master_playlist_urls()
    
    if not results:
        print("No videos found with combined audio+video master playlists.")
        return
    
    print(f"\nFound {len(results)} video(s) with combined audio+video streams:")
    print("=" * 80)
    
    for i, video in enumerate(results, 1):
        print(f"\n{i}. {video['name']}")
        print(f"   File: {video['file']}")
        print(f"   UUID: {video['uuid']}")
        print(f"   Duration: {video['duration']} seconds ({video['duration']//60}:{video['duration']%60:02d})")
        print(f"   Video URL: {video['video_url']}")
        print(f"   Master Playlist: {video['master_playlist_url']}")
        
        if video['resolutions']:
            print(f"   Available Resolutions:")
            for res in video['resolutions']:
                size_mb = res['size'] / (1024 * 1024) if res['size'] > 0 else 0
                print(f"     - {res['label']}: {res['width']}x{res['height']} @ {res['fps']}fps ({size_mb:.1f} MB)")
        else:
            print(f"   No resolution information available")
    
    print("\n" + "=" * 80)
    print("Master playlist URLs with resolutions:")
    for video in results:
        print(f"\n{video['master_playlist_url']}")
        if video['resolutions']:
            res_info = ", ".join([f"{res['label']} ({res['width']}x{res['height']})" for res in video['resolutions']])
            print(f"Available: {res_info}")
        else:
            print("No resolution info available")

if __name__ == "__main__":
    main()