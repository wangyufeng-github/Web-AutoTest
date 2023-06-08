pip install -r requirements.txt -i https://pypi.douban.com/simple
cd ./testCase
pytest -s --alluredir ./outFiles/reports/tmp --clean-alluredir
