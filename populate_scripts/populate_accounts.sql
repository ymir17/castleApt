INSERT INTO signup_accounts ("lastName", "firstName", "phoneNo", email, password)
VALUES('G�slason', '�mir P�ll', 8237424, 'ymir17@ru.is', 'ymir17');
INSERT INTO signup_accounts ("lastName", "firstName", "phoneNo", email, password)
VALUES('Ing�lfsson', 'S�var', 7707344, 'saevar17@ru.is', 'saevar17');
INSERT INTO signup_accounts ("lastName", "firstName", "phoneNo", email, password)
VALUES('J�nsson', 'Anton B�i', 8946341, 'anton17@ru.is', 'anton17');
INSERT INTO signup_accounts ("lastName", "firstName", "phoneNo", email, password)
VALUES('Bjarnason', 'Atli Steinn', 8484432, 'atlib17@ru.is', 'atlib17');
INSERT INTO signup_accounts ("lastName", "firstName", "phoneNo", email, password)
VALUES('�lafsson', 'Arnar', 8945831, 'arnaro17@ru.is', 'arnaro17');

INSERT INTO contacts_realtorimages ("realtImgUrl")
VALUES ('static/images/realtors/ymir.JPG"');
INSERT INTO contacts_realtorimages ("realtImgUrl")
VALUES ('static/images/realtors/saevar.jpg');
INSERT INTO contacts_realtorimages ("realtImgUrl")
VALUES ('static/images/realtors/anton.jpeg');
INSERT INTO contacts_realtorimages ("realtImgUrl")
VALUES ('static/images/realtors/atli.jpg');
INSERT INTO contacts_realtorimages ("realtImgUrl")
VALUES ('static/images/realtors/arnar.png');

INSERT INTO contacts_realtors ("accountId_id", "description", "realtImgId_id")
VALUES(1, 'Ymir has a PhD in real estate economics. He has worked for Castle Apartments since he co-founded with his five other coworkers in 1962.', 1);
INSERT INTO contacts_realtors ("accountId_id", "description", "realtImgId_id")
VALUES(2, 'Saevar has a master degree in real estate engineering. Since he co-founded Castle Apartments in 1962 he has engineered the very fundamentals of real estates.', 2);
INSERT INTO contacts_realtors ("accountId_id", "description", "realtImgId_id")
VALUES(3, 'Anton has both a bachelor degree in business and a master degree in real estate economics. When he co-founded Castle Apartments in 1962 he was nominated as person of the year in Times magazine.', 3);
INSERT INTO contacts_realtors ("accountId_id", "description", "realtImgId_id")
VALUES(4, 'Atli has a high school degree. In 1962 he, along with others, co-founded Castle Apartments. He has not accomplished anything since.', 4);
INSERT INTO contacts_realtors ("accountId_id", "description", "realtImgId_id")
VALUES(5, 'Arnar has a PhD in real estate science. After he co-founded Castle Apartments in 1962, he backpacked through Asia, tamed lions, teach children english and introduced the people to communism. He returned back to Castle Apartments in 1989.', 5);