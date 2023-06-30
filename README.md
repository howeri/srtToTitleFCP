# Transform an SRT File to Title for Final Cut Pro Users
When importing SRT files into Final Cut Pro, the captions lack flexibility, restricting options such as changing font styles or positioning. However, by utilizing this code, one can transform SRT files into a title format that offers greater flexibility, enabling modifications to font styles, placements, and more. For questions, queries and bug reports, please feel free to contact: huangeric@ucla.edu

## Examples:
Edit your video in 23.98p frame rate. Follow the steps in pyTranscriber (https://github.com/raryelcostasouza/pyTranscriber/releases) to transcribe your video and generate the SRT file. Download this repository. In terminal, run 
```python
python [drag_the_main.py_file_here] -f [drag_your_srt_file_here]
```
Then, open the "output.fcpxml" file from this repository with Final Cut Pro. Copy the titles. Choose "Edit" -> "Paste as Connected Clip" and align the titles.

## Note:
The code is tested with Python 3.9.12. Please install Python 3 before running the code. The feature of generating titles for other frame rates will be added soon.

-----------
# 將 SRT文件 轉換為 Final Cut Pro 標題格式
將SRT文件匯入Final Cut Pro時，字幕缺乏靈活性且限制了更改字體風格以及定位等選項。透過此程式，SRT文件將轉換為標題格式。此將提供字體風格位置等修改靈活度。如有問題、查詢或錯誤報告，請聯繫：huangeric@ucla.edu

## 範例：
請使用23.98p幀率製作影片。依照 pyTranscriber (https://github.com/raryelcostasouza/pyTranscriber/releases) 中步驟操作生成SRT文件。下載此 repository。在終端機中運行
```python
python [拖曳main.py] -f [拖曳您的SRT文件]
```
在此 repository 中使用 Final Cut Pro 打開 "output.fcpxml" 文件。複製後選擇 "Edit" -> "Paste as Connected Clip" 並對齊標題。

## 詳細範例：
1. 用 Final Cut Pro 23.98p 幀率製作影片並輸出 (1)影片以及 (2)音訊.
2. 在 https://www.python.org/downloads/ 下載並安裝 Python.
3. 至 pyTranscriber (https://github.com/raryelcostasouza/pyTranscriber/releases) ，Assets 處點擊下載 pyTranscriber-v1.9-mac.zip.
4. 在 Spotlight(聚焦搜索) 或 應用程式 中打開 終端機 (Terminal).
5. 在終端機中輸入 `xattr -cr [拖曳下載之應用程式]` (例如：`xattr -cr Download/pyTranscriber-v1.9-mac.app`)，按鍵盤Return.
6. 點擊打開 pyTranscriber-v1.9-mac.app。點擊 Select Files 並選取您的音訊。選擇語言。點擊"Transcribe Audio / Generate Subtitles"。SRT檔 將會生成於桌面的 pyTranscriber 資料夾.
7. 在此網頁點擊 "<>Code" 並下載ZIP. 資料夾 srtToTitleFCP 將會下載於”下載“資料夾中.
8. 回到 終端機 (Terminal) 並輸入 `python [拖曳由此下載的main.py檔] -f [拖曳您桌面 pyTranscriber 資料夾中的SRT文件]` (例如：`python /Users/erichuang/Desktop/srtToTitleFCP/main.py -f /Users/erichuang/Desktop/pyTranscriber/example.srt`)，按鍵盤Return.
9. 至 srtToTitleFCP 資料夾，右鍵選擇 output.fcpxml 並使用 Final Cut Pro 開啟檔案"。新的 TitleTest Project 將出現在您目前選取的 Final Cut Pro 圖庫(Library).
10. 複製 標題 (Title) 後在您的影片中選擇 "Edit" -> "Paste as Connected Clip" 並對齊標題.
