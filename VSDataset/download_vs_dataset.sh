dataset_filename=VSDataset.zip

drive_file_id=1jDuByxPJr5rQKTjlkJmTgCGTPNHxg1ot

output_path=$1

extract_path=$output_path

drive_url=https://drive.google.com/uc?id=$drive_file_id

output_filename=$output_path/$dataset_filename

echo "\n"
echo "--------------------------"
echo "Downloading $dataset_filename"
echo "--------------------------"
echo "\n"
gdown $drive_url -O $output_filename 

echo "\n"
echo "--------------------------"
echo "Extracting $dataset_filename"
echo "--------------------------"
echo "\n"
unzip $output_filename -d $extract_path
rm $output_filename

