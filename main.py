import os
import sys
import re
import argparse
current_file_path = os.path.abspath(__file__)
current_directory = os.path.dirname(current_file_path)
sys.path.append(current_directory)

def time_to_seconds(time):
    time_parts = time.split(':')
    hours, minutes = map(int, time_parts[:2])
    seconds, milliseconds = map(int, time_parts[2].replace(',', '.').split('.'))
    return hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

def transform_srt(srt_file):
    with open(srt_file, 'r') as file:
        srt_content = file.read()

    caption_regex = re.compile(r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3})\s-->\s(\d{2}:\d{2}:\d{2},\d{3})\n(.+?)(?=\n\d+|\Z)', re.DOTALL)

    captions = []
    matches = caption_regex.findall(srt_content)
    for match in matches:
        caption_number = int(match[0])
        start_time = match[1]
        end_time = match[2]
        caption_text = match[3].strip()
        start_seconds = time_to_seconds(start_time)
        duration_seconds = time_to_seconds(end_time) - start_seconds
        captions.append((caption_number, start_seconds, duration_seconds, caption_text))

    return captions

def create_xml_with_captions(srt_file, titleBlock_XML_file, template_XML_file):
    # Process captions
    captions = transform_srt(srt_file)
    all_titleBlocks = ''
    for caption in captions:
        caption_number, start_seconds, duration_seconds, caption_text = caption
        # Create title block content
        with open(titleBlock_XML_file, 'r') as file:
            titleBlock_content = file.read()     

        updated_titleBlock_content = re.sub(r'id="[^"]*"', f'id="ts{caption_number}"', titleBlock_content, count=1)

        start_seconds_x120000 = int(start_seconds*120000)
        updated_titleBlock_content = re.sub(r'offset="[^"]*"', f'offset="{start_seconds_x120000}/120000s"', updated_titleBlock_content, count=1)
        
        duration_seconds_x120000 = int(duration_seconds*120000)
        updated_titleBlock_content = re.sub(r'duration="[^"]*"', f'duration="{duration_seconds_x120000}/120000s"', updated_titleBlock_content, count=1)
        
        updated_titleBlock_content = re.sub(r'templateTest', caption_text, updated_titleBlock_content)

        all_titleBlocks = all_titleBlocks + updated_titleBlock_content
    
    # Insert title blocks to template
    with open(template_XML_file, 'r') as file:
        template_content = file.read()
    keyword_position = template_content.find('<spine>\n')
    insert_position = keyword_position + len('<spine>\n')
    output = template_content[:insert_position] + all_titleBlocks + template_content[insert_position:]

    # Create output file
    with open(current_directory+'/output.fcpxml', 'w') as output_file:
        output_file.write(output)
    print("XML file updated successfully.")

# Main
parser = argparse.ArgumentParser()
parser.add_argument('-f', '--file', type=str, help='Name of your srt caption file with extension (.srt)')
args = parser.parse_args()

srt_file = args.file
titleBlock_XML_file = current_directory+'/titleBlock.fcpxml'
template_XML_file = current_directory+'/template.fcpxml'
create_xml_with_captions(srt_file, titleBlock_XML_file, template_XML_file)
