## Rclone to help us determine which folders take up the most space in our google drive

Rclone gives us a way to export sizes of folders as json which gives us a nice way to use python scripts to get total sizes

Note that the occurences of baylyd should be replaced with whatever your remote configured name is.

First get a json showing the folders in the root

```
rclone lsjson --dirs-only baylyd:/ > root_folders.json
```

then we can use the python script which will iterate over the elements in that returned json to create individual jsons of the folder contents

```
python3 rclone_folder_summaries.py
```

This command you even run multiple times if not all the folders have been summarized and it will pickup summarizing folders it hasn't already.

We then want to run the `drive-json-consolidator.py` script to make a single csv from our data for visulizing

```
python3 drive-json-consolidator.py
```

This should produce a `drive_files_analyzed.csv` file that we can then use in the visualization tool below.


## Visualizing our results

Use this observable notebook to visualize the data

https://observablehq.com/@devinbayly/drive-data-parser
