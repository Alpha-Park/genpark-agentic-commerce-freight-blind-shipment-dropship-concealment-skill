# genpark-agentic-commerce-freight-blind-shipment-dropship-concealment-skill

[![GenPark AI](https://img.shields.io/badge/GenPark-AI%20Ecosystem-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0077b5)](https://www.linkedin.com/company/92955550)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-brightgreen.svg)](https://www.python.org/)

Dropshipping blind shipment double-bill-of-lading anonymizer: supplier-shipper mask & consignee packing slip sanitization.

## Overview

Part of the **GenPark Industrial Multi-Agent Skill Matrix**. Zero external pip dependencies; built purely with standard Python library modules for instant deterministic orchestration.

- **Official Web Portal**: [https://www.genpark.ai](https://www.genpark.ai)
- **Corporate LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## Tool Specification

- **Tool Name**: `generate_blind_shipment_bol_pair`
- **Category**: `agentic_commerce`

### Method Documentation
Generate dual Bill of Lading (BOL) manifests for blind/double-blind dropship freight fulfillment.
Masks true manufacturing source identity from ultimate consignee (retail customer) and conceals end-customer pricing/identity from white-label suppliers.

## JSON-RPC 2.0 Integration

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "generate_blind_shipment_bol_pair",
    "arguments": {
    "actual_manufacturer": {
        "name": "Shenzhen Precision Plastics Co.",
        "address": "Baoan District, Shenzhen, CN"
    },
    "distributor_broker": {
        "name": "Apex OmniCommerce LLC",
        "address": "Wilmington, DE, USA"
    },
    "end_customer_consignee": {
        "name": "Metro Retail Group Store #402",
        "address": "Dallas, TX, USA"
    },
    "items_manifest": [
        {
            "sku": "APX-PL-101",
            "description": "Custom Molded Brackets",
            "cartons": 24,
            "weight_lbs": 680
        }
    ]
}
  }
}
```

## Running Self Tests

```bash
python skills.py --test
```
