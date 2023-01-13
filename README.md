
# CloudVisionTextBoxRecognizer
Google Cloud Vision Text Recognizer

This a simple command line client to Google Cloud Vision Text Recognizer.<br>

<h2> 
1 Install
</h2>
Please install Coogle Cloud SDK on your PC. We use Windows11 OS.<br>
Install the Google Cloud CLI<br>
https://cloud.google.com/sdk/docs/install-sdk
<br>

<br>
<h2>
2 Install python packages
</h2>
Please clone this repository to your local PC.<br>
We use Python3 venv on Windows11 OS.
<br>
>pip install requirements.txt
</h2>


<h2>
3 Sample Program
</h2>
Please open <b>Cloud Tools for PowerShell</b> from <b>Google Cloud SDK</b>.<br>

<img src="./asset/Google_Clout_SDK.png" width="400" height="auto"><br>

Please run the following command in <b>Cloud Tools for PowerShell</b> console.<br>

> python CloudVisionTextBoxRecognizer.py 
<br>
This CloudVisionTextBoxRecognizer.py script reads the recognition.conf file.<br>
<pre>
[parameter]
images_dir   = "./samples"
;output_dir   = "./outputs"
output_dir   = "./non_preprocessed"
image_format = ".png"
language_hints   = ["ja"]

[preprocessor]
;preprocessing    = True
preprocessing    = False
gray_image       = True
image_scaling    = 3
contrast         = 1.5
sharpness        = 3

[visualizer]
font_name        = "BIZ-UDMinchoM.ttc"
draw_boundingbox = True
expanding_ratio  = 1.0
scaling_on_nonpreprocessing = 3
</pre>

Please note that we specify the language_hints in this config file to be ["ja"] to recognize Japanese text.<br>
You have to change this language_hints property depending on your text language.<br>



Example 1: 参考・教育漢字を除く常用漢字.png<br>
<img src="./samples/参考・教育漢字を除く常用漢字.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_参考・教育漢字を除く常用漢字.png"
     width="1280" height="auto">
<br>

Example 2: 付録常用漢字の一覧_付表<br>
<img src="./samples/付録常用漢字の一覧_付表.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_付録常用漢字の一覧_付表.png"
     width="1280" height="auto">
<br>


Example 3: 半角カタカナ一覧<br>
<img src="./samples/半角カタカナ一覧.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_半角カタカナ一覧.png"
     width="1280" height="auto">
<br>

Example 4: VSCodeScreenShot<br>
<img src="./samples/VSCodeScreenShot.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_VSCodeScreenShot.png"
     width="1280" height="auto">
<br>

Example 5: Symbols_Kakana<br>
<img src="./samples/Symbols_Kakana.png" width="1280" height="auto"><br>
<br>


Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_Symbols_Kakana.png"
     width="1280" height="auto">
<br>

Example 6: RoadSign.png<br>
<img src="./samples/RoadSign.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_RoadSign.png"
     width="1280" height="auto">
<br>




Example 7: ARTIZON_MUSEUM.png<br>
<img src="./samples/ARTIZON_MUSEUM.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_ARTIZON_MUSEUM.png"
     width="1280" height="auto">
<br>



Example 8: Nihonbashi-Takashimaya.png<br>
<img src="./samples/Nihonbashi-Takashimaya.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_Nihonbashi-Takashimaya.png"
     width="1280" height="auto">
<br>

Example 9: Chuoh-Street.png<br>
<img src="./samples/Chuoh-Street.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_Chuoh-Street.png"
     width="1280" height="auto">
<br>

Example 10: No_parking.png<br>
<img src="./samples/No_parking.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_No_parking.png"
     width="1280" height="auto">
<br>


Example 11: NadaDana.png<br>
<img src="./samples/NadaDana.png" width="1280" height="auto"><br>
<br>

Text Box Recognition:<br>
<img src="./outputs/preprocessed_scaling_3_contrast_1.5_sharpness_3_NadaDana.png"
     width="1280" height="auto">
<br>

