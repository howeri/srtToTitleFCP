# Transform an SRT File to Title for Final Cut Pro Users
When importing SRT files into Final Cut Pro, the captions lack flexibility, restricting options such as changing font styles or positioning. However, by utilizing this code, one can transform SRT files into a title format that offers greater flexibility, enabling modifications to font styles, placements, and more. For questions, queries and bug reports, please feel free to contact: huangeric@ucla.edu

## Examples:
Follow the steps in pyTranscriber (https://github.com/raryelcostasouza/pyTranscriber/releases) to transcribe your video and generate an SRT file. Download this repository. In terminal, run 
```python
python [drag_the_main.py_file_here] -f [drag_your_srt_file_here]
```
Then, open the 'output.fcpxml' file with Final Cut Pro. Copy and Paste and align the titles.

## Note:
The code is tested with Python 3.9.12. Please install Python 3 before running the code.
