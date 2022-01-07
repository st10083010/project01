import requests, json , time, re, csv
from bs4 import BeautifulSoup
from time import sleep


# start = time.time()


male_name_url = 'https://www.yces.chc.edu.tw/english/engboyname-all.htm'
female_name_url = 'https://www.yces.chc.edu.tw/english/enggirlname-all.htm'

male_name_LIST = ['Abe', 'Abel', 'Abner', 'Abraham', 'Allen', 'Adam', 'Adolf', 'Albin', 'Alden', 'Alexis',
                  'Ambrose', 'Amos', 'Adrian', 'Al', 'Albert', 'Alexander', 'Alfred', 'Alistair', 'Alvin',
                  'Andrew', 'Andy', 'Anselm', 'Anthony', 'Antony', 'Angus', 'Archibald', 'Archie', 'Arnold',
                  'Arthur', 'Augustin', 'Augustus', 'Auberon', 'Aubrey', 'Baldwin', 'Bertran', 'Bryan', 'Barnaby',
                  'Barry', 'Bartholomew', 'Basil', 'Ben', 'Benjamin', 'Bernard', 'Bernie', 'Bert', 'Bill', 'Billy',
                  'Bob', 'Bobby', 'Boris', 'Bradford', 'Brad', 'Brandon', 'Brendan', 'Brian', 'Bruce', 'Bud', 'Burt',
                  'Caesar', 'Calvin', 'Carlton', 'Cary', 'Christian', 'Carl', 'Cecil', 'Cedric', 'Charles', 'Charlie',
                  'Chuck', 'Christopher', 'Chris', 'Clarence', 'Clark', 'Claude', 'Clement', 'Clare', 'Constant', 'Curtis',
                  'Clifford', 'Cliff', 'Clint', 'Clive', 'Clyde', 'Colin', 'Craig', 'Curt', 'Cyril', 'Cuthbert', 'Dexter',
                  'Derby', 'Dale', 'Daniel', 'Dan', 'Danny', 'Darrell', 'Darren', 'David', 'Dave', 'Dean', 'Dennis', 'Derek',
                  'Dermot', 'Desmond', 'Des', 'Dick', 'Dirk', 'Dominic', 'Donald', 'Don', 'Douglas', 'Doug', 'Duane', 'Dudley',
                  'Dud', 'Duncan', 'Dustin', 'Dwight', 'Duke', 'Earl', 'Ebenezer', 'Eamonn', 'Ed', 'Edgar', 'Edmund', 'Edward',
                  'Edwin', 'Eliot', 'Elmer', 'Elroy', 'Emlyn', 'Enoch', 'Eric', 'Ernest', 'Errol', 'Eugene', 'Eli', 'Enos', 'Freddie',
                  'Felix', 'Ferdinand', 'Fergus', 'Floyd', 'Francis', 'Frank', 'Frankie', 'Frederick', 'Fred', 'Gaston', 'Gabriel', 'Gareth',
                  'Gary', 'Gavin', 'Gene', 'Geoffrey', 'Geoff', 'George', 'Geraint', 'Gerald', 'Gerry', 'Gerard', 'Gilbert', 'Giles', 'Glen',
                  'Godfrey', 'Gordon', 'Graham', 'Graeme', 'Gregory', 'Greg', 'Guy', 'Gideon', 'Grant', 'Humphry', 'Hal', 'Hank', 'Harold',
                  'Harry', 'Henry', 'Herbert', 'Horace', 'Howard', 'Hubert', 'Hugh', 'Hamilton', 'Hector', 'Heman', 'Hugo', 'Herman', 'Hilary',
                  'Howell', 'Hugh', 'Humphrey', 'Hiram', 'Homer', 'Ian', 'Isaac', 'Ivan', 'Ivor', 'Ira', 'Irving', 'Irwin', 'Jarvis', 'Jean',
                  'Job', 'Jack', 'Jacob', 'Jake', 'James', 'Jamie', 'Jason', 'Jasper', 'Jed', 'Jeff', 'Jeffrey', 'Jeremy', 'Jerome', 'Jerry',
                  'Jesse', 'Jessy', 'Jim', 'Jimmy', 'Jock', 'Joe', 'John', 'Johnny', 'Jonathan', 'Jon', 'Joseph', 'Joshua', 'Julian', 'Justin',
                  'Julius', 'Karl', 'Kay', 'Keith', 'Ken', 'Kenneth', 'Kenny', 'Kent', 'Kevin', 'Kit', 'Kev', 'Kirk', 'Laban', 'Lee', 'Lance',
                  'Larry', 'Laurence', 'Len', 'Lenny', 'Leo', 'Leonard', 'Les', 'Leslie', 'Lester', 'Lew', 'Leon', 'Lincoln', 'Lewis', 'Liam',
                  'Lionel', 'Lou', 'Louis', 'Luke', 'Lucius', 'Luman', 'Lynn', 'Malcolm', 'Mark', 'Martin', 'Malachi', 'Marshall', 'Marvin',
                  'Marty', 'Matt', 'Mattew', 'Matlhew', 'Milton', 'Monroe', 'Maurice', 'Max', 'Mervyn', 'Michael', 'Mick', 'Micky', 'Miles',
                  'Mike', 'Mitch', 'Mitchell', 'Morris', 'Mort', 'Murray', 'Morgan', 'Montgomery', "Na'amai", 'Nat', 'Nathan', 'Nahum', 'Napoleon',
                  'Nelson', 'Newton', 'Noah', 'Norbert', 'Nathaniel', 'Neal', 'Ned', 'Neddy', 'Nicholas', 'Nick', 'Nicky', 'Nigel', 'Noel', 'Norm',
                  'Norman', 'Ollie', 'Oliver', 'Oscar', 'Oswald', 'Owen', 'Oz', 'Ozzie', 'Octavius', 'Osmond', 'Otto', 'Paddy', 'Pat', 'Patrick',
                  'Paul', 'Percy', 'Pete', 'Peter', 'Phil', 'Philip', 'Padraic', 'Pearce', 'Perry', 'Philander', 'Philemen', 'Pius', 'Quentin',
                  'Quincy', 'Rene', 'Reuben', 'Ralph', 'Randolf', 'Randy', 'Raphael', 'Ray', 'Raymond', 'Reg', 'Reginald', 'Rex', 'Richard',
                  'Richie', 'Rick', 'Ricky', 'Rob', 'Robbie', 'Robby', 'Robert', 'Robin', 'Rod', 'Roderick', 'Rodney', 'Rodge', 'Roger', 'Ronald',
                  'Ron', 'Ronnie', 'Rory', 'Roy', 'Rudolph', 'Rufus', 'Rupert', 'Russ', 'Reuel', 'Reynold', 'Roland', 'Ross', 'Russell', 'Samson',
                  'Saul', 'Sam', 'Sammy', 'Samuel', 'Sandy', 'Scott', 'Seamas', 'Sean', 'Seb', 'Sebastian', 'Sid', 'Sidney', 'Simon', 'Stan',
                  'Stanley', 'Steve', 'Steven', 'Stewart', 'Sinclair', 'Solomon', 'Stuart', 'Ted', 'Teddy', 'Tel', 'Terence', 'Terry', 'Theo',
                  'Theodore', 'Thomas', 'Tim', 'Timmy', 'Timothy', 'Toby', 'Tom', 'Tommy', 'Tony', 'Theobald', 'Theodoric', 'Terence', 'Trevor',
                  'Troy', 'Urban', 'Van', 'Vivian', 'Vic', 'Victor', 'Vince', 'Vincent', 'Viv', 'Wallace', 'Wally', 'Walter', 'Warren', 'Wayne',
                  'Wesley', 'Winston', 'Will', 'Wilbur', 'Wilfred', 'Willy', 'William', 'Willis']

female_name_LIST = ['Abigail', 'Ada', 'Agatha', 'Adelaide', 'Adelina', 'Alethea', 'Aggie', 'Agnes', 'Aileen', 'Alex', 'Alexandra', 'Alexis', 'Alice',
                    'Alison', 'Amanda', 'Amy', 'Angela', 'Angie', 'Anita', 'Anne', 'Anna', 'Annabel', 'Annie', 'Annette', 'Anthea', 'Antonia',
                    'Audrey', 'Allson', 'Alma', 'Althea', 'Angelica', 'Aspasia', 'Aurelian', 'Ava', 'Avis', 'Beata', 'Belle', 'Babs', 'Barbara',
                    'Beatrice', 'Becky', 'Belinda', 'Bernadette', 'Beryl', 'Betty', 'Bid', 'Brenda', 'Bridget', 'Brittany', 'Bertha', 'Bonny',
                    'Camilla', 'Candice', 'Carla', 'Carol', 'Caroline', 'Carrie', 'Catherine', 'Cathy', 'Cecilia', 'Cecily', 'Celia', 'Charlene',
                    'Charlotte', 'Cherry', 'Cheryl', 'Chloe', 'Chris', 'Chrissie', 'Christina', 'Christine', 'Cindy', 'Clare', 'Claudia', 'Cleo',
                    'Connie', 'Constance', 'Crystal', 'Candida', 'Carmen', 'Celestine', 'Charissa', 'Colleen', 'Cora', 'Corinna', 'Cynthia',
                    'Dulcie', 'Dottie', 'Daisy', 'Daphne', 'Dawn', 'Deb', 'Debby', 'Deborah', 'Deirdre', 'Delia', 'Della', 'Denise', 'Di', 'Diana',
                    'Diane', 'Dolly', 'Donna', 'Dora', 'Doreen', 'Doris', 'Dorothy', 'Dot', 'Elva', 'Edith', 'Edna', 'Eileen', 'Elaine', 'Eleanor',
                    'Eleanora', 'Eliza', 'Elizabeth', 'Ella', 'Ellen', 'Ellie', 'Elsa', 'Elsie', 'Elspeth', 'Emily', 'Emma', 'Erica', 'Ethel',
                    'Eunice', 'Eva', 'Eve', 'Evelyn', 'Eugenia', 'Eulalia', 'Evadne', 'Evangeline', 'Faustina', 'Fay', 'Felicity', 'Fidelia',
                    'Fiona', 'Flo', 'Flora', 'Florence', 'Felicia', 'Flavia', 'Frieda', 'Freda', 'Florrie', 'Fran', 'Frances', 'Frankie', 'Gene',
                    'Georgia', 'Georgie', 'Georgina', 'Geraldine', 'Germaine', 'Gertie', 'Gertrude', 'Gill', 'Gillian', 'Ginny', 'Gladys', 'Glenda',
                    'Gloria', 'Grace', 'Gracie', 'Ashley', 'Gwen', 'Gwendoline', 'Hannah', 'Harriet', 'Hazel', 'Heather', 'Helen', 'Henrietta',
                    'Hilary', 'Hilda', 'Hedda', 'Hedwig', 'Helga', 'Hortensia', 'Isabella', 'Ivy', 'Ida', 'Ingrid', 'Irene', 'Iris', 'Isabel',
                    'Jemima', 'Juliana', 'Jan', 'Jane', 'Janet', 'Janey', 'Janice', 'Jackie', 'Jacqueline', 'Jean', 'Jeanie', 'Jennifer', 'Jenny',
                    'Jess', 'Jessica', 'Jessie', 'Jill', 'Jo', 'Joan', 'Joanna', 'Joanne', 'Jocelyn', 'Josephine', 'Josie', 'Jode', 'Joyce',
                    'Judith', 'Judy', 'Julia', 'Julie', 'Juliet', 'June', 'Karen', 'Kathleen', 'Kate', 'Kathy', 'Katie', 'Kay', 'Kelly', 'Kim',
                    'Kimberly', 'Kirsten', 'Kitty', 'Katharine', 'Kit', 'Leila', 'Laura', 'Lauretta', 'Lesley', 'Libby', 'Lilian', 'Lily', 'Linda',
                    'Lindsay', 'Lisa', 'Livia', 'Liz', 'Lois', 'Lori', 'Lorna', 'Louisa', 'Louise', 'Lucia', 'Lucinda', 'Lucy', 'Lydia', 'Lynn',
                    'Leslie', 'Lucile', 'LuLu', 'Mabel', 'Madeleine', 'Madge', 'Maggie', 'Maisie', 'Mandy', 'Marcia', 'Marcie', 'Margaret',
                    'Margery', 'Maria', 'Marian', 'Mary', 'Marilyn', 'Marlene', 'Martha', 'Melanie', 'Mercedes', 'Mignon', 'Mimi', 'Martha',
                    'Martina', 'Mary', 'Maud', 'Maureen', 'Mavis', 'Meg', 'Melanie', 'Melinda', 'Melissa', 'Michelle', 'Mildred', 'Millicent',
                    'Millie', 'Miranda', 'Miriam', 'Moira', 'Molly', 'Monica', 'Muriel', 'Minnie', 'Nadine', 'Nina', 'Nadia', 'Nan', 'Nancy',
                    'Naomi', 'Natalie', 'Natasha', 'Nell', 'Nellie', 'Nicky', 'Nicola', 'Nicole', 'Nora', 'Norma', 'Nita', 'Olga', 'Olympia',
                    'Olive', 'Olivia', 'Pam', 'Pamela', 'Pat', 'Patience', 'Pancy', 'Persis', 'Prudence', 'Patricia', 'Patsy', 'Patti', 'Paula',
                    'Pauline', 'Pearl', 'Peggie', 'Penelope', 'Penny', 'Philippa', 'Phoebe', 'Phyllis', 'Poll', 'Polly', 'Priscilla', 'Pru',
                    'Renee', 'Rachel', 'Rebecca', 'Rhoda', 'Rita', 'Roberta', 'Robin', 'Rosalie', 'Rosalind', 'Rosalyn', 'Rose', 'Rosemary',
                    'Rosie', 'Ruby', 'Rosa', 'Ruth', 'Salome', 'Sylvia', 'Sadie', 'Sal', 'Sally', 'Sam', 'Samantha', 'Sandra', 'Sandy', 'Sara',
                    'Sharon', 'Sheila', 'Sherry', 'Shirley', 'Sibyl', 'Silvia', 'Sonia', 'Sophia', 'Sophronia', 'Sophie', 'Stella', 'Stephanie',
                    'Susan', 'Susanna', 'Sue', 'Susie', 'Suzanne', 'Tabitha', 'Teresa', 'Terri', 'Tess', 'Tessa', 'Thelma', 'Tina', 'Thalia',
                    'Thea', 'Thirza', 'Toni', 'Tracy', 'Tricia', 'Trudie', 'Uerica', 'Una', 'Undine', 'Ursula', 'Urania', 'Vivian', 'Vivien',
                    'Val', 'Valerie', 'Vanessa', 'Vera', 'Veronica', 'Vicky', 'Victoria', 'Viola', 'Violet', 'Virginia', 'Viv', 'Willa', 'Wendy',
                    'Winifred', 'Winnie', 'Yvonne', 'Zoe']


# file_path_M = r'C:\Users\TibeMe_user\Desktop\男用姓名.csv'
#--------------------------------------------------
# with open(file_path_M, encoding='utf-8') as f:
#     mycsv = csv.reader(f)
#     try:
#         for row in mycsv:
#             male_name_LIST.append(row[0])
#             male_name_LIST.append(row[1])
#             male_name_LIST.append(row[2])
#             # print(row)
#             # print('='*10)
#             # print(row[0])
#             # print('-' * 10)
#             # print(row[1])
#             # print('-' * 10)
#             # print(row[2])
#             # print('~'*10)
#     except IndexError:
#         pass
#--------------------------------------------------
# file_path_F = r'C:\Users\TibeMe_user\Desktop\女用姓名.csv'
# with open(file_path_F, encoding='utf-8') as f:
#     mycsv0 = csv.reader(f)
#     try:
#         for row0 in mycsv0:
#             female_name_LIST.append(row0[0])
#             female_name_LIST.append(row0[1])
#             female_name_LIST.append(row0[2])
#             print(row0)
#             print('='*10)
#             print(row0[0])
#             print('-' * 10)
#             print(row0[1])
#             print('-' * 10)
#             print(row0[2])
#             print('~'*10)
#     except IndexError:
#         pass
#--------------------------------------------------
# 檢查資料
# print(male_name_LIST)
# print(len((male_name_LIST)))
# print(female_name_LIST)
# print(len((female_name_LIST)))

# 在網路上找出資料，處理過後轉成CSV，將輸出的結果複製改掉原本的空LIST，讓別的檔案import
# #--------------------------------------------------
# end = time.time()
# spendTime = end - start
# print('花費時間: ' + str(spendTime) + '秒')