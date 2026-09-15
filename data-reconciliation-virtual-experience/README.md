# Data Reconciliation - Capgemini Virtual Experience

Work completed as part of Capgemini's Data Reconciliation job simulation on Forage.

## Task

A client migrated from a legacy system to a new cloud system. Users can now generate management reports in the new cloud system with a single click, but the migration needs to be validated. The task was to confirm that the Opex Report for August 2019, generated in the new cloud system, matches the source data in the legacy system.

The client organises its data by company code (organisational subsections), with multiple G/L (general ledger) accounts under each one.

## Approach

- Built a unique lookup key per record by concatenating Company Code and G/L Account
- Used `VLOOKUP` to pull the corresponding legacy balance for every line in the cloud report
- Calculated the variance (legacy value minus cloud value) for all 489 line items across 18 company codes
- Built a summary table (SUMIFS/COUNTIFS) rolling the results up by company code, functioning as a pivot-style view
- Created clustered column charts comparing cloud vs. legacy values by G/L account for two company codes, to visualise the result

## Result

All 489 line items reconciled exactly, with zero variance across every company code. The new cloud system's Opex Report is accurate.

## Files

- [`Opex_Data_Reconciliation.xlsx`](./Opex_Data_Reconciliation.xlsx): full reconciliation workbook (VLOOKUP formulas, variance analysis, company code summary)
- [`Opex_Reconciliation_Charts.pptx`](./Opex_Reconciliation_Charts.pptx): graphical comparison of cloud vs. legacy balances by G/L account for company codes 2000 and 3420

## Tools used

Excel (VLOOKUP, SUMIFS, pivot-style summaries, charts), PowerPoint

## About this simulation

This is a Forage job simulation, an unofficial preview of the type of work done at Capgemini. It is not a real client engagement.
