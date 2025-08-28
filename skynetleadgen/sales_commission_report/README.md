# Sales Commission Report (Per Salesperson)

Generates a PDF with one page per salesperson for a selected month, pulling data from `manual.sales.commission`.

## Fields in commission model
- `name` (Char) → Salesperson name
- `no_of_leads` (Integer)
- `commission_amount` (Float, computed = no_of_leads * 500)

## Usage
1. Go to **Sales Commissions → Commission Report**.
2. Pick any date in the target month.
3. Print the PDF → one page per salesperson, with leads and commission totals.
