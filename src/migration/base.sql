-- create tables
create table if not exists fancode.sports
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    status boolean not null default true,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp
);

create table if not exists fancode.tours
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    sportId int not null,
    status boolean not null default true,
    startTime timestamp not null,
    endTime timestamp not null,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp,
    foreign key (sportId) references sports(id)
);

create table if not exists fancode.matches
(
    id int auto_increment not null primary key,
    name varchar(50) not null,
    tourId int not null,
    status boolean not null default true,
    format varchar(50) not null,
    startTime timestamp not null,
    endTime timestamp not null,
    recUpdatedAt timestamp not null default current_timestamp on update current_timestamp,
    createdAt timestamp not null default current_timestamp,
    foreign key (tourId) references tours(id)
);

create table if not exists fancode.news
(
    id int auto_increment not null primary key,
    title varchar(50) not null,
    description text,
    sportId int not null,
    tourId int not null,
    matchId int null,
    createdAt timestamp not null default current_timestamp,
    foreign key (tourId) references tours(id),
    foreign key (sportId) references sports(id),
    foreign key (matchId) references matches(id),
);

-- creating index on name column in tours table
CREATE INDEX idx_tours_name ON tours (name);


-- seed data
insert ignore into fancode.sports (id, name) values (1, 'Cricket');
insert ignore into fancode.sports (id, name) values (2, 'Football');

insert ignore into fancode.tours (id, name, sportId, startTime, endTime) values (1, 'Indian Premier League, 2023', 1, '2023-04-09 00:00:00', '2023-05-30 00:00:00');
insert ignore into fancode.tours (id, name, sportId, startTime, endTime) values (2, 'India Super League, 2023', 2, '2023-04-21 00:00:00', '2023-06-20 00:00:00');
insert ignore into fancode.tours (id, name, sportId, startTime, endTime) values (3, 'India Tour of West Indies, 2023', 1, '2023-06-10 00:00:00', '2023-06-29 00:00:00');
insert ignore into fancode.tours (id, name, sportId, startTime, endTime) values (4, 'English Premier League, 2022', 2, '2022-04-09 00:00:00', '2022-05-30 00:00:00');
insert ignore into fancode.tours (id, name, sportId, startTime, endTime) values (5, 'SAFF Championship 2023', 2, '2022-04-09 00:00:00', '2022-05-30 00:00:00');

insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('GT vs RCB', 1, 'T20', '2023-04-09 18:00:00', '2023-04-09 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('CSK vs MI', 1, 'T20', '2023-04-10 18:00:00', '2021-04-10 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('LSG vs KXIP', 1, 'T20', '2023-04-11 18:00:00', '2023-04-11 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('RR vs SRH', 1, 'T20', '2023-04-12 18:00:00', '2023-04-12 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('BLR vs BEN', 2, 'soccer', '2023-04-29 18:00:00', '2023-04-29 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('ATK vs MCFC', 2, 'soccer', '2023-04-21 18:00:00', '2023-04-21 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('KER vs JFC', 2, 'soccer', '2023-04-22 18:00:00', '2023-04-22 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-10 10:00:00', '2023-06-10 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-12 10:00:00', '2023-06-12 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('IND vs WI', 3, 'ODI', '2023-06-14 10:00:00', '2023-06-14 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('KER vs JFC', 4, 'soccer', '2022-04-09 18:00:00', '2022-04-09 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('IND vs KWT', 5, 'soccer', '2022-04-09 18:00:00', '2022-04-09 23:00:00');
insert ignore into fancode.matches (name, tourId, format, startTime, endTime) values ('CSK vs GT', 1, 'T20', '2022-04-09 18:00:00', '2022-04-09 23:00:00');

insert ignore into fancode.news (title, description, sportId, tourId, matchId) values ('SAFF Championship 2023: India win thrilling penalty shootout to claim ninth title', 'The Indian football team beat Kuwait 5-4 in a penalty shootout after the final was tied at 1-1 after regulation time.', 2, 5, 23);
insert ignore into fancode.news (title, description, sportId, tourId, matchId) values ('IPL 2023 Chennai Super Kings beats Gujarat Titans by five wickets to win fifth title', 'The M.S. Dhoni-led side has now matched Mumbai Indians’ record of five IPL crowns; Hardik Pandya’s outfit falls agonisingly short of defending the trophy that it won last year', 1, 1, 24);