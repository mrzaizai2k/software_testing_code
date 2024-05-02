# software_testing_code
Code for software testing automation

# Mô tả tổng quan

Web automation testing là 1 dự án dựa trên các list test case trong bài project 2 và phát triển lên thành web automation testing. Ở bài project 2 em test trên web moodle. Tuy nhiên, vì server yếu, chậm và dễ sập nên em xin phép test trên 2 ứng dụng khác theo như project 2 mà nhóm đã làm, chi tiết ở file ./docs/Group2-proj3-testcase.xlsm. 
2 application test bao gồm:

- BMI test: https://www.calculator.net/bmi-calculator.html
- Body_fat test: https://www.calculator.net/body-fat-calculator.html

Trong quá trình thực thi chạy thử nếu có xảy ra vấn đề, thầy có thể liên lạc với em thông qua:
- Video demo (phòng trường hợp xảy ra sự cố thực thi/ môi trường): https://youtu.be/0Hyueac8eHA
- Email: chibao24.12.1999@gmail.com
- Github: https://github.com/mrzaizai2k/software_testing_code


# Yêu cầu cài đặt

## OS: Window 10/11

Anaconda: Để cài đặt thư viện. 

Nếu đã có anaconda thầy có thể cài python bằng lệnh:
- ```conda init```
- ```conda activate```
- ```conda create -n auto_test python=3.12.2 -y```
- ```conda activate auto_test```

Python 3.12.2 hoặc 3.10.9
Sau đó cài đặt thư viện theo lệnh

- ```pip install -r setup.txt```

Thư viện gồm:
- selenium==4.19.0
- pandas==1.5.3
- numpy==1.23.5
- PyYAML==6.0

Thay đổi đường dẫn trong file config.yaml: 
    
    driver_path: chromedriver-win64/chromedriver-win64/chromedriver.exe

## OS: Mac

Cũng làm các bước tương tự như trên, nhưng thầy cần thay đổi đường dẫn trong file config.yaml

    driver_path: chromedriver-mac-x64/chromedriver-mac-x64/chromedriver

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

File config chứa:

- driver_path: Là đường dẫn tương đối đến file chrome driver (driver phải compatible với phiên bản chrome đang sử dụng)
- BMI_url: https://www.calculator.net/bmi-calculator.html: Là đường dẫn đến trang web để test BMI
- BMI_test: Chứa các test case cho việc test BMI.
- TC-001-XXX: Mã cho test case của bài test BMI. Chứa data input và expected output cho test case
- Body_fat_url: https://www.calculator.net/body-fat-calculator.html: Là đường dẫn đến trang web để test Body fat
- Body_fat_test: Chứa các test case cho việc test Body fat.
- TC-002-XXX: Mã cho test case của bài test Body fat. Chứa data input và expected output cho test case


## Diễn tả file chạy

File auto_test.py sẽ thực hiện chạy tuần tự như sau:

Đầu tiên file sẽ mở đường dẫn BMI_url để thực hiện test các test case cho BMI. Phần mềm sẽ tự động nhập hoặc để trống như các input data cho trước, sau khi click vào nút "Calculate" trên trang web thì phần mềm sẽ tiến hành kiểm thử. Kiểm thử sẽ gồm kiểm thử kết quả đúng hay sai, và sai thì có cho ra lỗi trùng khớp với expected output đã cho ở trong file config hay không. Ở command line, phần mềm sẽ hiển thị tên test case, config của test case (gồm input data và expected output)

Tiếp theo phần mềm sẽ mở đường dẫn Body_fat_url để thực hiện test các test case cho body fat. Phần mềm sẽ tự động nhập hoặc để trống như các input data cho trước, sau khi click vào nút "Calculate" trên trang web thì phần mềm sẽ tiến hành kiểm thử. Kiểm thử sẽ gồm kiểm thử kết quả đúng hay sai, và sai thì có cho ra lỗi trùng khớp với expected output đã cho ở trong file config hay không. Ở command line, phần mềm sẽ hiển thị tên test case, config của test case (gồm input data và expected output)

Toàn bộ đoạn code được chạy trên python dùng tool Selenium. Đoạn code được chạy tối đa 3 lần thử, phòng trường hợp có sự cố mạng xảy ra. Sau mỗi lần test phần mềm sẽ chờ từ 2 - 5 giây để đảm bảo đường link và các thành phần web đã hiển thị nhằm mục đích đảm bảo hoạt động tốt


# Mô tả test case

Vì lí do bài project 2 em có sử dụng moodle login, và đồng thời server của moodle bị giật lag, không đảm bảo nên em xin phép được làm project 3 sử dụng 2 application tại 
- BMI_url: https://www.calculator.net/bmi-calculator.html cho việc test data ở trang BMI
- Body_fat_url: https://www.calculator.net/body-fat-calculator.html cho việc test tại trang tính Body Fat
- 
Các test case được mô tả chi tiết tại file ./docs/Group2-proj3-testcase.xlsm. 

Ở trang BMI sẽ có tổng cộng 8 test case như sau, nếu trong phần Expected chỉ có bmi_value và status thì test case đó đang test trường hợp thành công và em sẽ so sánh kết quả BMI đó với expected value nằm trong output, Ở các test case có bmi_value == Null và có error là đang test các trường hợp thất bại, lúc này trang web sẽ báo lỗi và em sẽ so sánh lỗi xem có đúng với expected output không:

Ví dụ ở TC-001-001, phần Expected output có bmi_value: 20.8, status: Healthy weight em sẽ kiểm tra kết quả sau khi nhấn nút Calculate có hiện giá trị bmi_value: 20.8 và status: Healthy weight không. Còn ở TC-001-003 phần Expected output có bmi_value: Null và age_error: Please provide an age between 2 and 120. Em sẽ check kết quả sau khi nhấn nút Calculate, trang web có hiển thị lỗi "Please provide an age between 2 and 120" và không hiển thị kết quả BMI hay không.

TC-001-001:

    # Input
    age: 20
    height: 170
    weight: 60
    gender: male

    # Expected
    bmi_value: 20.8
    status: Healthy weight

TC-001-002:

    # Input
    age: 30
    height: 160
    weight: 55
    gender: female

    # Expected
    bmi_value: 21.5
    status: Normal

TC-001-003:

    # Input
    age: 1
    height: 180
    weight: 80
    gender: male

    # Expected
    bmi_value: Null
    age_error: Please provide an age between 2 and 120.



TC-001-004:

    # Input
    age: 121
    height: 180
    weight: 80
    gender: male

    # Expected
    bmi_value: Null
    age_error: Please provide an age between 2 and 120.



TC-001-005:

    # Input
    age: 80
    height: 180
    weight: 80
    gender: male

    # Expected
    bmi_value: 24.7
    status: Normal

TC-001-006:

    # Input
    age: 119
    height: 180
    weight: 80
    gender: male

    # Expected
    bmi_value: 24.7
    status: Normal

TC-001-007:

    # Input
    age: 3
    height: 180
    weight: 80
    gender: male

    # Expected
    bmi_value: 24.7
    status: Overweight

TC-001-008:

    # Input
    age: 80
    height: 180
    weight: 0
    gender: male

    # Expected
    bmi_value: Null
    weight_error: Please provide positive weight value.

Ở trang Body Fat sẽ có tổng cộng 6 test case như sau, nếu trong phần Expected chỉ có body_fat thì test case đó đang test trường hợp thành công và em sẽ so sánh kết quả Body Fat đó với expected value nằm trong output, Ở các test case có body_fat == Null và có error là đang test các trường hợp thất bại, lúc này trang web sẽ báo lỗi và em sẽ so sánh lỗi xem có đúng với expected output không:

Ví dụ ở TC-002-001, phần Expected output có body_fat: 15.0 em sẽ kiểm tra kết quả sau khi nhấn nút Calculate có hiện giá trị body_fat: 15.0 không. Còn ở TC-002-004 phần Expected output có body_fat: Null, neck_error: Neck need to be numeric., waist_error: Waist need to be numeric.. Em sẽ check kết quả sau khi nhấn nút Calculate, trang web có hiển thị 2 lỗi "Neck need to be numeric.", "Waist need to be numeric." và không hiển thị kết quả Body Fat hay không

TC-002-001:

    # Input
    age: 23
    height: 182
    weight: 71
    gender: male
    neck: 34
    waist: 80

    # Expected
    body_fat: 15.0
    


TC-002-002:

    # Input
    age: -1
    height: -1
    weight: -1
    gender: male
    neck: -1
    waist: -1

    # Expected
    body_fat: Null
    age_error: Please provide a positive age.
    height_error: Height need to be positive.
    weight_error: Please provide a positive weight.
    neck_error: Neck need to be numeric.
    waist_error: Waist need to be numeric.

TC-002-003:

    # Input
    age: Null
    height: Null
    weight: Null
    gender: male
    neck: Null
    waist: Null

    # Expected
    body_fat: Null
    age_error: Please provide a positive age.
    height_error: Height need to be positive.
    weight_error: Please provide a positive weight.
    neck_error: Neck need to be numeric.
    waist_error: Waist need to be numeric.

TC-002-004:

    # Input
    age: 25
    height: 175
    weight: 75
    gender: male
    neck: Null
    waist: Null

    # Expected
    body_fat: Null
    neck_error: Neck need to be numeric.
    waist_error: Waist need to be numeric.


TC-002-005:

    # Input
    age: 70
    height: 155
    weight: 60
    gender: female   
    neck: Null
    waist: Null

    # Expected
    body_fat: Null
    neck_error: Neck need to be numeric.
    waist_error: Waist need to be numeric.


TC-002-006:

    # Input
    age: 0
    height: 140
    weight: 80
    gender: male
    neck: Null
    waist: Null

    # Expected
    body_fat: Null
    neck_error: Neck need to be numeric.
    waist_error: Waist need to be numeric.
    
# Kết quả thực hiện

Sau khi chạy file thì các test case đã được thực hiện và cho ra kết quả tốt

# Tài liệu
- Trong quá trình thực thi chạy thử nếu có xảy ra vấn đề hãy liên lạc với em thông qua email: chibao24.12.1999@gmail.com
- Github: https://github.com/mrzaizai2k/software_testing_code
- Video demo (phòng trường hợp xảy ra sự cố thực thi/ môi trường): https://youtu.be/0Hyueac8eHA

# Tài liệu tham khảo
- https://www.browserstack.com/guide/python-selenium-to-run-web-automation-test
- https://viblo.asia/p/tim-hieu-testing-web-automation-voi-selenium-webdriver-va-python-Qbq5Q46RlD8


