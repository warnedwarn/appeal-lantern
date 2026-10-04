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
