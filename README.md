# software_testing_code
Code for software testing automation

Vì trang moodle load chập chờn nên em xin phép thầy cho em test ở link này ạ
https://www.calculator.net/bmi-calculator.html

Learn Selenium
Level 0: re-test all test cases in proj#2 using Selenium IDE. Note that, at the end of each test case recording, you need to "verify" the expected output.
Level 1: data-driven test for test cases in proj#2 using Selenium Driver (using any programming languages supported by Selenium) - test inputs and exepected outputs are in data files
Leve 2: (bonus) Level 1 and web items are in data files.

For group, who tested a real application that needs your/tester's user name and password, you may need to change the testing application, Or, if you want to update your test cases, please describe clearly in the report.

Report
- Report file type: .pdf and .xls(x) and source of the code(s).
- Review the tool with a short description how to use the tool.
- Show the way to apply the tool to test your application.
- Show the test results

# Yêu cầu cài đặt

OS: Window 10/11
Anaconda: Để cài đặt thư viện. Nếu đã có anaconda thầy có thể cài python bằng lệnh:
- ```conda init```
- ```conda activate```
- ```conda create -n auto_test python=3.12.2 -y```
- ```conda activate auto_test```

Python 3.12.2 hoặc 3.10.9
Sau đó cài đặt thư viện theo lệnh

- ```pip install -r setup.txt```

Thay đổi đường dẫn trong file config.yaml: 
    driver_path: chromedriver-win64/chromedriver-win64/chromedriver.exe

OS: Mac

Cũng làm các bước tương tụ như trên, nhưng thầy cần thay đổi đường dẫn trong file config.yaml
    
- driver_path: chromedriver-win64/chromedriver-win64/chromedriver.exe

Trong trường hợp chrome drive không trùng với bản chrome của thầy
- Thầy vui lòng tải bản chrome drive tại link https://googlechromelabs.github.io/chrome-for-testing/ cho đúng phiên bản.
- Giải nén file và đưa vào thư mục làm việc
- Thay đổi đường dẫn trong file config.yaml thành đường dẫn đến file driver


# Cách sử dụng

Sau khi cài đặt môi trường cần thiết. Chúng ta cần cd vào thư mục đang hoạt động. và dùng lệnh:

- ```python auto_test.py```

Câu lệnh này sẽ thực hiện chạy test tự động và đưa ra kết quả trên cmd


# Mô tả phần mềm
## Mô tả file config 

File config chứa 
- driver_path: Là đường dẫn tương đối đến file chrome driver (driver phải compatible với phiên bản chrome đang sử dụng)
- BMI_url: https://www.calculator.net/bmi-calculator.html: Là đường dẫn đến trang web để test BMI
- Body_fat_url: https://www.calculator.net/body-fat-calculator.html: Là đường dẫn đến trang web để test Body fat
- BMI_test: Chứa các test case cho việc test BMI.
- TC-001-XXX: Mã cho test case của bài test BMI. Chứa data input và expected output cho test case
- Body_fat_test: Chứa các test case cho việc test Body fat.
- TC-002-XXX: Mã cho test case của bài test Body fat. Chứa data input và expected output cho test case


## Diễn tả file chạy

File auto_test.py sẽ thực hiện chạy tuần tự như sau:
Đầu tiên file sẽ mở đường dẫn BMI_url để thực hiện test các test case cho BMI. Phần mềm sẽ tự động nhập hoặc để trống như các input data cho trước, sau khi click vào nút "Calculate" trên trang web thì phần mềm sẽ tiến hành kiểm thử. Kiểm thử sẽ gồm kiểm thử kết qủa đúng hay sai, và sai thì có cho ra lỗi trùng khớp với expected output đã cho ở trong file config hay không. Ở command line, phần mềm sẽ hiển thị tên test case, config của test case (gồm input data và expected output)

Tiếp theo phần mềm sẽ mở đường dẫn Body_fat_url để thực hiện test các test case cho body fat. Phần mềm sẽ tự động nhập hoặc để trống như các input data cho trước, sau khi click vào nút "Calculate" trên trang web thì phần mềm sẽ tiến hành kiểm thử. Kiểm thử sẽ gồm kiểm thử kết qủa đúng hay sai, và sai thì có cho ra lỗi trùng khớp với expected output đã cho ở trong file config hay không. Ở command line, phần mềm sẽ hiển thị tên test case, config của test case (gồm input data và expected output)

Toàn bộ đoạn code được chạy trên python dùng tool Selenium


# Mô tả test case

# Kết quả thực hiện
- Mô tả kết quả, đã check như thế nào
