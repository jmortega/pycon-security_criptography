str = """
      TmljZSBzdGFydC4g
      IFN1cmUgaG9wZSB5
      b3UgdGhpbmsgaXQg
      d2FzIHN0dXBpZCBz
      aW1wbGUuIAoKU2Vu
      ZCBhbiBlLW1haWwg
      dG8gZm9vQGNoYWxs
      ZW5nZS4weDQxNDE0
      MTQxLmNvbS4gQSBy
      ZXBseSB3aWxsIGJl
      IHNlbnQgdG8gdGhl
      IHJlcGx5LXRvIGFk
      ZHJlc3MgY29udGFp
      bmluZyB0aGUgVVJM
      IG9mIHRoZSBzZWNv
      bmQgdGFzay4K
      """

print("Encoded String: %s" % str)
print("Decoded String: %s" % str.decode('base64','strict'))