#check avaiable name
ban_word =[
  "đụ","địt","đ ụ","đjt","djt",
  "đm","đmm","cđm","vc","d!t","vkl","vcc","vklm","sml","vclm"
  "loz","lồn","l o z",
  "cẹc","buồi","buoi'","cặc","cặk",
  "đĩ","điếm",
  "cock","dick","pussy","porn","bitch","fuk",
  "đéo",
]

name_check=["q","w","e","r","t","y","u","i","o","p",
"a","s","d","f","g","h","j","k","l",
"z","x","c","v","b","n","m",

"Q","W","E","R","T","Y","U","I","O","P",
"A","S","D","F","G","H","J","K","L",
"Z","X","C","V","B","N","M",

"0","1","2","3","4","5","6","7","8","9",

"ă","â","đ","ê","ô","ơ","ư",
"á","à","ã","ả","ạ",
"ắ","ằ","ặ","ẵ","ẳ",
"ầ","ấ","ẩ","ẫ","ậ",
"è","ẻ","é","ẽ","ẹ",
"ề","ế","ể","ễ","ệ",
"ồ","ố","ổ","ỗ","ộ",
"ờ","ớ","ở","ỡ","ợ",
"ừ","ứ","ử","ữ","ự",
"í","ì","ĩ","ỉ","ị",
"ỳ","ý","ỵ","ỷ","ỹ",
"ò","ó","õ","ỏ","ọ",
"ù","ú","ũ","ụ","ủ",

"_"]
number = [
"0","1","2","3","4","5","6","7","8","9",
]

command_mess="""
**Các lệnh:**
```
/public: mở phòng cho tất cả mọi người vào

/private: khóa phòng, chỉ những người được mời mới vào được

/allow + [tên_người_muốn_mời hoặc id]: cho phép người bạn muốn vào phòng

/invite + [tên_người_muốn_mời hoặc id]: mời người vào phòng

/disallow | /kick + [tên_người_muốn_kick hoặc id]: kick ra khỏi phòng

/limit + [số_người_giới_hạn]

/rename + [tên phòng]: đổi tên phòng

```

***Chú ý:**
-Bạn chỉ có thể tạo 1 phòng cùng lúc
-Phòng chat này chỉ những người đang trong phòng của bạn mới thấy
-Phòng sẽ mất khi không còn ai trong phòng
-Bạn có thể gọi bot trong kênh này
||Chúc các bạn học vui =)))||
"""

command_mess_ts="""
**Các lệnh:**
```
/public: mở phòng cho tất cả mọi người vào

/private: khóa phòng, chỉ những người được mời mới vào được

/hide: ẩn phòng với mọi người

/show: hiện phòng với mọi người

/allow + [tên_người_muốn_mời hoặc id]: cho phép người bạn muốn vào phòng

/invite + [tên_người_muốn_mời hoặc id]: mời người vào phòng

/disallow | /kick + [tên_người_muốn_kick hoặc id]: kick ra khỏi phòng

/limit + [số_người_giới_hạn]

/rename + [tên phòng]: đổi tên phòng

```

***Chú ý:**
-Bạn chỉ có thể tạo 1 phòng cùng lúc
-Phòng chat này chỉ những người đang trong phòng của bạn mới thấy
-Phòng sẽ mất khi không còn ai trong phòng
-Bạn có thể gọi bot trong kênh này
||Có gì khúc mắc hãy tâm sự cùng mọi người nhé||
"""



command_mess_sg="""
**Các lệnh:**
```
/public: mở phòng cho tất cả mọi người vào

/private: khóa phòng, chỉ những người được mời mới vào được

/allow + [tên_người_muốn_mời hoặc id]: cho phép người bạn muốn vào phòng

/invite + [tên_người_muốn_mời hoặc id]: mời người vào phòng

/disallow | /kick + [tên_người_muốn_kick hoặc id]: kick ra khỏi phòng

/limit + [số_người_giới_hạn]

/rename + [tên phòng]: đổi tên phòng

```

***Chú ý:**
-Bạn chỉ có thể tạo 1 phòng cùng lúc
-Phòng chat này chỉ những người đang trong phòng của bạn mới thấy
-Phòng sẽ mất khi không còn ai trong phòng
||Chúc các bạn học vui =)))||
"""


command_mess_cp="""
**Các lệnh:**
```
/public: mở phòng cho tất cả mọi người vào

/private: khóa phòng, chỉ những người được mời mới vào được

/hide: ẩn phòng với mọi người

/show: hiện phòng với mọi người

/allow + [tên_người_muốn_mời hoặc id]: cho phép người bạn muốn vào phòng

/invite + [tên_người_muốn_mời hoặc id]: mời người vào phòng

/disallow | /kick + [tên_người_muốn_kick hoặc id]: kick ra khỏi phòng

/rename + [tên phòng]: đổi tên phòng

```

***Chú ý:**
-Bạn chỉ có thể tạo 1 phòng cùng lúc
-Phòng chat này chỉ những người đang trong phòng của bạn mới thấy
-Phòng sẽ mất khi không còn ai trong phòng
||Chúc các bạn phát cơm tró vui vẻ =)))||
"""
command_mess_sa="""
**Các lệnh:**
```
/rename + [tên phòng]: đổi tên phòng
```
***Chú ý:**
-Bạn chỉ có thể tạo 1 phòng cùng lúc
-Phòng chat này chỉ 1 mình bạn thấy
-Phòng sẽ mất khi không còn ai trong phòng
||Chúc bạn tự kỉ vui vẻ =)))||
"""