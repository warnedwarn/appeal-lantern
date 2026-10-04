# Appeal Lantern

## A missing deadline can erase a real right

Appeal Lantern audits the remedy instructions printed in a public decision. It does not decide the underlying dispute. Instead, it asks a narrower and reusable question: does the notice accurately tell the affected person **where**, **when**, and **how** to seek review under the governing rulebook?

The filer names two different wallets: the decision issuer and an independent reviewer. The rulebook and decision must come from different HTTPS origins. The reviewer triggers the first audit; validators fetch both records, bind their SHA-256 digests, and return only closed field labels. Contract code derives `COMPLETE` or `DEFECTIVE`.

A defective notice opens one bounded cure window. Only the issuer can submit a replacement from the original authoritative decision origin. The rulebook digest must remain unchanged. A successful repair becomes `CURED`; a failed or abandoned repair becomes `UNRESOLVED`.

### State rail

`OPEN → COMPLETE`

`OPEN → DEFECTIVE → CURED | UNRESOLVED`

### Reviewer checks

- independent filer, issuer, and reviewer wallets;
- normalized HTTPS sources with separate origins;
- three to six fields selected from `FORUM`, `DEADLINE`, `METHOD`, `FORM`, `FEE`, `CONTACT`;
- exact validator agreement on source digests and every bounded output;
- permissionless expiry, so an issuer cannot stall a defective record forever.

The sample records are operator-authored fixtures. They demonstrate contract mechanics, not legal advice or an actual appeal right.

## StudioNet proof

- Contract: [`0x82e9feAd7286c33dDcfC2a6Fd000D7d3E383b930`](https://explorer-studio.genlayer.com/address/0x82e9feAd7286c33dDcfC2a6Fd000D7d3E383b930)
- Deployment: [`0x79e95d893371c5df60a5a393de3f8c00544ecdcffc347b44ce8ad3a302ac2908`](https://explorer-studio.genlayer.com/transactions/0x79e95d893371c5df60a5a393de3f8c00544ecdcffc347b44ce8ad3a302ac2908)
- Open audit: [`0x39f9255e83519fceca0183331e2e554deba2bd9ea0601ffce3f53b265382c5c6`](https://explorer-studio.genlayer.com/transactions/0x39f9255e83519fceca0183331e2e554deba2bd9ea0601ffce3f53b265382c5c6)
- Defect inspection: [`0xd723971f736d8566980cdd568363f386e20fe6ce11111bac2df4824757c0d8c5`](https://explorer-studio.genlayer.com/transactions/0xd723971f736d8566980cdd568363f386e20fe6ce11111bac2df4824757c0d8c5)
- Corrected notice: [`0x609a628e160065a9596bfa148e12d02523d57764e8c8b7f574488cbf0af7c752`](https://explorer-studio.genlayer.com/transactions/0x609a628e160065a9596bfa148e12d02523d57764e8c8b7f574488cbf0af7c752)
- Readback: `APPEAL-1791122900`, revision `1`, state `CURED`.
- Exact deployed source SHA-256: `750795797b8c03db3aae943b7ce1833458df2139184c6180ba9e38be56bc9f5d`.
