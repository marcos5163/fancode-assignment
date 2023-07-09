const mysql = require('../lib/mysql');

const getAllSportsToursAndMatches = async () => {
    const statement = `
      SELECT s.name AS sportName, t.name AS tourName, m.name AS matchName, m.id AS matchId, m.startTime, m.format
      FROM matches AS m
      LEFT JOIN tours AS t ON m.tourId = t.id
      LEFT JOIN sports AS s ON t.sportId = s.id
    `;
    const parameters = [];
    return await mysql.query(statement, parameters);
}

module.exports = {
    getAllSportsToursAndMatches: getAllSportsToursAndMatches
}