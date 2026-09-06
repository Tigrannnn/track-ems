

const STAGES = {
  packing:   { label: "Packing",             pct: 12,  tone: "amber"  },
  awaiting:  { label: "Waiting to admit",    pct: 28,  tone: "slate"  },
  transit:   { label: "On the way",          pct: 58,  tone: "blue"   },
  out:       { label: "Out for delivery",    pct: 84,  tone: "orange" },
  delivered: { label: "Delivered",           pct: 100, tone: "green"  }
};

const SHIPMENTS = {
  "1569852359": {
    status: "transit",
    service: "ParcelPath Ground",
    from: "Guangzhou, China",
    to: " United Kingdom",
    address: "19 Beachfield Rd, Sandown PO36 8LR",
    eta: "13–14 calendar days",
    weight: "1.7 lbs",
    pieces: 1,
    events: [
      ["Sep 8, 2026 · ", "Out for delivery (estimated time) 17-18 September",                                "United Kingdom", "est"],
      ["Sep 5, 2026 · ", "Picked up from shipper",                               "Guangzhou, China"],
      ["Sep 4, 2026 · ", "Label created - shipment information received ",       "Guangzhou, China"]
    ]
  }
};
