# SeMPyRO enrichment plan for v2.1.0

`Health-RI_v2.1.0_sempyro_plan.xlsx` is the review plan for adding the SeMPyRO columns to
`../Health-RI_v2.1.0.xlsx`. It was generated with `metadata-automation sempyro-enrichment-plan`
([Health-RI/metadata-automation#36](https://github.com/Health-RI/metadata-automation/pull/36)):

```bash
metadata-automation sempyro-enrichment-plan \
  --previous-excel inputs/HealthRI_v2.0.2.xlsx \
  -i Documents/Health-RI_v2.1.0.xlsx \
  -o Documents/sempyro_enrichment/Health-RI_v2.1.0_sempyro_plan.xlsx
```

Review the sheet `plan` (filter on `status`, start with `NEEDS_HUMAN`), fill in `final_value` where needed and
tick `reviewed (x)`. The plan is bound to the Excel it was made from; regenerate it when the Excel changes.
