gobuster gcs -w ./s3words.txt -t 100 > gcspartho.txt

python -u create_links.py 
python -u check_links.py