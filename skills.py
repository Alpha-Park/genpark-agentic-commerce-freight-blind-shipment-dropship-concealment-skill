# -*- coding: utf-8 -*-
"""GenPark Industrial Skill: genpark-agentic-commerce-freight-blind-shipment-dropship-concealment-skill
Category: agentic_commerce
Website: https://www.genpark.ai
LinkedIn: https://www.linkedin.com/company/92955550
"""
import sys
import json
import math

sys.stdout.reconfigure(encoding="utf-8")

def generate_blind_shipment_bol_pair(actual_manufacturer, distributor_broker, end_customer_consignee, items_manifest):
    # Shipper BOL (handed to carrier at manufacturer dock)
    bol_dock = {
        "bol_type": "CARRIER_PICKUP_DOCK_MANIFEST",
        "shipper_name": actual_manufacturer["name"],
        "shipper_address": actual_manufacturer["address"],
        "consignee_name": distributor_broker["name"], # Disguised
        "delivery_c_o": "c/o Forwarding Warehouse",
        "items": items_manifest
    }
    
    # Delivery BOL (handed by carrier to end customer at final delivery)
    bol_delivery = {
        "bol_type": "FINAL_DELIVERY_CONSIGNEE_MANIFEST",
        "shipper_name": distributor_broker["name"], # Manufacturer masked
        "shipper_address": distributor_broker["address"],
        "consignee_name": end_customer_consignee["name"],
        "delivery_address": end_customer_consignee["address"],
        "items": items_manifest
    }
    
    return {
        "blind_shipping_strategy": "DOUBLE_BLIND_TWO_LEG_BOL",
        "manufacturer_identity_masked": True,
        "consignee_pricing_shielded": True,
        "carrier_dock_bol": bol_dock,
        "final_delivery_bol": bol_delivery,
        "carrier_special_instructions": "BLIND SHIPMENT: DO NOT DIVULGE SHIPPER TO CONSIGNEE OR CONSIGNEE TO SHIPPER."
    }


def handle_rpc(request_str):
    try:
        req = json.loads(request_str)
        rpc_id = req.get("id")
        method = req.get("method")
        params = req.get("params", {})
        
        if method == "tools/list":
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "tools": [{
                        "name": "generate_blind_shipment_bol_pair",
                        "description": """Generate dual Bill of Lading (BOL) manifests for blind/double-blind dropship freight fulfillment.
Masks true manufacturing source identity from ultimate consignee (retail customer) and conceals end-customer pricing/identity from white-label suppliers.""",
                        "inputSchema": {
                            "type": "object",
                            "properties": {}
                        }
                    }]
                }
            })
        elif method == "tools/call":
            call_params = params.get("arguments", {})
            res = generate_blind_shipment_bol_pair(**call_params)
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "result": {
                    "content": [{
                        "type": "text",
                        "text": json.dumps(res, indent=2)
                    }]
                }
            })
        else:
            return json.dumps({
                "jsonrpc": "2.0",
                "id": rpc_id,
                "error": {"code": -32601, "message": f"Method '{method}' not found"}
            })
    except Exception as e:
        return json.dumps({
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32000, "message": str(e)}
        })

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        sample = {'actual_manufacturer': {'name': 'Shenzhen Precision Plastics Co.', 'address': 'Baoan District, Shenzhen, CN'}, 'distributor_broker': {'name': 'Apex OmniCommerce LLC', 'address': 'Wilmington, DE, USA'}, 'end_customer_consignee': {'name': 'Metro Retail Group Store #402', 'address': 'Dallas, TX, USA'}, 'items_manifest': [{'sku': 'APX-PL-101', 'description': 'Custom Molded Brackets', 'cartons': 24, 'weight_lbs': 680}]}
        out = generate_blind_shipment_bol_pair(**sample)
        print("[TEST_PASS] Output:", json.dumps(out))
    else:
        for line in sys.stdin:
            line = line.strip()
            if not line:
                continue
            print(handle_rpc(line))
