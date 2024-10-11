import * as fs from 'fs';
import * as path from 'path';

function csvToSqlInsert(csvFilePath: string): string {
    /**
     * Converts the contents of a csv file into an SQL insert statement with a table name with the suffix removed.
     *
     * @param {string} csvFilePath - csv file path
     * @returns {string} - parsed sql str
     */
    const tableName = path.basename(csvFilePath).replace('.csv', '');
    let sqlStr = `INSERT INTO ${tableName} VALUES\n(`;

    // Read and parse CSV content
    const fileContent = fs.readFileSync(csvFilePath, 'utf8');
    const rows = fileContent.split('\n');

    for(let i = 1; i < rows.length; i++) {
        const rowValues = rows[i].split(',');
        sqlStr += '(';
        for(let j = 0; j < rowValues.length; j++) {
            sqlStr += `'${rowValues[j]}',`;
        }
        sqlStr = sqlStr.slice(0, -1); // Remove last comma
        sqlStr += '),\n';
    }

    // Remove last comma and newline character
    sqlStr = sqlStr.slice(0, -2);
    sqlStr += ';';

    return sqlStr;
}