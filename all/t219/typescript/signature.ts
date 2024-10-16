/**
 * Check for ticker symbols with the same ex-dividend date but different dividend amounts.
 * @param {Array} records - Each tuple contains [ticker, ex_dividend_date, dividend_amount].
 * @returns {Array} - Each tuple contains [ticker, ex_dividend_date] that have different dividend amounts.
 */
function checkDividendVariances(records: Array<[string, string, number]>): Array<[string, string]> {}