 - For optimising /tour/matches endpoint, solution is to create index for name column in tours table,  and modified the query to use index  
   `SELECT *
    FROM matches
    LEFT JOIN tours ON matches.tourId = tours.id AND tours.name = ? `

    - In the modified query **WHERE** clause has been moved to the **ON**  clause of the LEFT JOIN. This allows the database to 
      utilize the index on the tours.name column more efficiently during the join operation. [commit](https://github.com/marcos5163/fancode-assignment/commit/067fa7b58c44def258f8701ede89d0d9852eeda8)

- Added match's id, startTime and format in endpoint **/sport/tour/match** changes in [commit](https://github.com/marcos5163/fancode-assignment/commit/a2b984c2c894fb22fe489d131fedc9d99e9f8ffc)


- For adding news support, created a django project sports_news which uses same database as node project

- Created **news** table:
  `{
   "title": "string",
   "description":"string",
   "tourid":"int",
   "matchid":"int",
   "sportid":"int"
  }`

**News support APIs**  
   - For creating news,
     
     POST news/  
     **Payload**
      `{
        "title": "CSK won",
        "description": "CSK defeated GT to win IPL 2023",
        "tourid"/"matchid": 1 
       }`  
   - For getting news by any particular sport, tour, match  
     GET `news/sport/<sport_id>/`, `news/tour/<tour_id>/`, `news/match/<match_id>/`  

- Unit test are included in sports_news/app/tests.py
     

