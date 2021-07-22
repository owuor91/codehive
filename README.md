# Codehive API

This REST service allows you to enrol students to codehive and register them to courses


## Docs
### Registration

```
POST http://13.244.243.129/students/register
{
    "name": "Anna Banana",
    "phone_number": "0700000001",
    "email": "annab9@gmail.com",
    "date_of_birth": "2000-06-18",
    "nationality": "UGANDAN",
    "password": "banana123"
}
```
#### Response
```
{
    "date_created": "2021-07-22T08:25:19.636217+00:00",
    "date_updated": "2021-07-22T08:25:19.636226+00:00",
    "created_by": "Unknown",
    "updated_by": "Unknown",
    "active": true,
    "student_id": "0df42a79-1673-4436-84f0-06482e1c05ff",
    "name": "Anna Banana",
    "email": "annab9@gmail.com",
    "phone_number": "0700000001",
    "date_of_birth": "2000-06-18",
    "nationality": "UGANDAN"
}
```


### Login
You can login with either email/password or phone_number/password 
```
POST http://13.244.243.129/students/login
{
    "email": "annab9@gmail.com",
    "password": "banana123"
}
```
#### Response
```
{
    "message": "login successful",
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYyNjk0MjUzNSwianRpIjoiMWNlMzlhM2MtNTk2OS00ZmU2LWI3MmUtMTY4NDkyOTIzNzYxIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjBkZjQyYTc5LTE2NzMtNDQzNi04NGYwLTA2NDgyZTFjMDVmZiIsIm5iZiI6MTYyNjk0MjUzNSwiZXhwIjoxNjI3MDI4OTM1fQ.-PIjdwylhAMNh7HOvhSeUscNSeALTw9RHjM47vAm60Q",
    "student_id": "0df42a79-1673-4436-84f0-06482e1c05ff"
}
```


### Post a Course
Be sure to add the access token as a Bearer Token
```
POST http://13.244.243.129/courses
{
    "course_name": "Android development",
    "course_code": "AND 101",
    "description": "Android development with Kotlin",
    "instructor": "John Owuor"
}
```
#### Response
```
{
    "date_created": "2021-07-22T12:02:37.004315+03:00",
    "date_updated": "2021-07-22T12:02:37.004329+03:00",
    "created_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
    "updated_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
    "active": true,
    "course_id": "885e4f09-189e-4752-b5f2-9f5cca529cf9",
    "course_name": "Android development",
    "course_code": "AND 101",
    "description": "Android development with Kotlin",
    "instructor": "John Owuor"
}
```


### List Courses
Be sure to add the access token as a Bearer Token
```
GET http://13.244.243.129/courses
```
#### Response
```
[
    {
        "date_created": "2021-07-14T14:58:11.469525+03:00",
        "date_updated": "2021-07-14T15:00:32.276558+03:00",
        "created_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "updated_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "active": true,
        "course_id": "37e39c62-bcd2-44c0-b835-c741254814c8",
        "course_name": "Mathematics",
        "course_code": "MAT 301",
        "description": "Mathematics for computing",
        "instructor": "Katerina M."
    },
    {
        "date_created": "2021-07-22T12:02:37.004315+03:00",
        "date_updated": "2021-07-22T12:02:37.004329+03:00",
        "created_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "updated_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "active": true,
        "course_id": "885e4f09-189e-4752-b5f2-9f5cca529cf9",
        "course_name": "Android development",
        "course_code": "AND 101",
        "description": "Android development with Kotlin",
        "instructor": "John Owuor"
    },
    {
        "date_created": "2021-07-22T12:48:18.368601+03:00",
        "date_updated": "2021-07-22T12:48:18.368638+03:00",
        "created_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "updated_by": "e0d94341-53c9-49c5-909c-8bcae5873ac0",
        "active": true,
        "course_id": "790eebbd-1624-4a8a-a321-4a12ceb44f36",
        "course_name": "Web development",
        "course_code": "WEB 101",
        "description": "Web development",
        "instructor": "Bee Trice"
    }
]
```
## License
[MIT](https://choosealicense.com/licenses/mit/)