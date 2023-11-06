class IP:
    def __init__(self, ip, **kwargs):
        self.ip = ip
        self.vpn = kwargs.get("vpn")
        self.asn = kwargs.get("asn")
        self.provider = kwargs.get("provider")
        self.continent = kwargs.get("continent")
        self.continentcode = kwargs.get("continentcode")
        self.country = kwargs.get("country")
        self.isocode = kwargs.get("isocode")
        self.city = kwargs.get("city")
        self.region = kwargs.get("region")
        self.regioncode = kwargs.get("regioncode")
        self.timezone = kwargs.get("timezone")
        self.latitude = kwargs.get("latitude")
        self.longitude = kwargs.get("longitude")
        self.currency = kwargs.get("currency")
        self.proxy = kwargs.get("proxy")
        self.type = kwargs.get("type")
        self.risk = kwargs.get("risk")
        self.operator = kwargs.get("operator")

    def __repr__(self):
        return f"<IP {self.ip}>"

    def __str__(self):
        return self.ip

    @classmethod
    def from_result(cls, result):
        return cls(**result.dict())

    def is_proxy(self):
        return self.proxy == "yes"

    def is_vpn(self):
        return self.vpn == "yes"

