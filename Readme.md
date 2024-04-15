# Test Cacib 

## Installation method

1. Set up EC2 instance Amazon Linux 2023 AMI

```shell
sudo yum install git -y
git clone https://github.com/Cyrano71/TestCacib.git
curl -O https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py --user
 ```

2. Install the required packages

   ```
   cd Cacib
   pip install -r requirements.txt
   ```

3. Start the app

   ```shell
   python3 main.py
   ```

4. Check the app on [notes](http://localhost:8000/docs)
Open your browser and navigate to [docs](http://localhost:8000/docs) to view the swagger documentation for the api.

5. Run the tests with `pytest`

6. Next steps
- add try catch / checks
- add NoSql database
- create dockerfile
- add a .gitlab-ci.yml
- deploy on AWS