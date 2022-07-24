# [BE - Berat](https://gist.github.com/fandywie/c895e83afb2faa829116696d9a09ddbe)

![capture](https://user-images.githubusercontent.com/56458008/180660515-1456677e-17a1-4b32-ae56-2c3cf4ae5b8a.png)

## Usage

Run the following command to run the application.

```
cd SIRCLO/BE\ -\ Berat/
flask run
```

By default, the application will be served on `localhost:5000`.

## API

| Method   | Route             | Request                                                   | Description                                     |
|:--------:|-------------------|-----------------------------------------------------------|-------------------------------------------------|
| `GET`    | /index            | -                                                         | Display all berats.                             |
| `GET`    | /show/{tanggal}   | -                                                         | Display berat of {tanggal}.                     |
| `GET`    | /add              | -                                                         | Display add berat form.                         |
| `POST`   | /add              | 'tanggal', 'berat_min', 'berat_max'                       | Add berat.                                      |
| `GET`    | /update/{tanggal} | -                                                         | Display update berat form.                      |
| `POST`   | /update/{tanggal} | 'tanggal', 'berat_min', 'berat_max'                       | Update berat of {tanggal}.                      |
| `POST`   | /delete           | 'tanggal'                                                 | Update berat.                                   |

**NOTE: I do understand that we need to use method `PUT`, `PATCH`, and `DELETE` instead of `POST` for update and delete. However, I haven't found any solution to submit that method from HTML form.**

## Test

Run the following commands to run the test.

```
cd SIRCLO/BE\ -\ Berat/
python3 -m pytest -v
```

Here's what it will be looked like if all the tests are passed.

![image](https://user-images.githubusercontent.com/56458008/180660162-9651eb76-bef6-444c-8cbe-99a5816e76c6.png)

---

This project was developed for SIRCLO | Technical Test Software Engineer Backend.
