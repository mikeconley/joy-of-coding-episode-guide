---
layout: default
date: 2024-07-03
number: 371
---

# Episode 371: Jul 3rd, 2024

## Links
* [Watch this episode on Air Mozilla](https://mzl.la/joy-of-coding-2024-07-03)
* [Joplin Agenda](https://mikeconley.ca/joc/agendas/Episode-0371.html)

## Topics
* Designing and writing tests for the OSKeyStore recovery mechanism
  - Firefox has the ability to store payment methods (credit cards)
  - We never want to store the credit cards in plaintext on the filesystem
  - So therefore, we must encrypt the credit cards, and only decrypt them on demand
  - How does this encryption work? It's actually quite similar to how other browsers (specifically Chrome-based browsers) do it.
  - OSKeyStore is a JavaScript module, and it wraps an XPCOM component that is (perhaps confusingly) also called OSKeyStore, but within the JS module the XPCOM component is called nativeOSKeyStore.
  - How does nativeOSKeyStore work? Well, it uses the underlying OS's secret storage mechanism to hold on to a single secret.
    - Windows: DPAPI
    - macOS: KeyChain
    - Linux/GTK: libsecret
  - Say you're saving a credit card for the first time - you've never done it before. Firefox will randomly generate a "secret" set of bytes with high-entropy, and store it in the underlying secure storage.
  - You use the secret as the key to encrypt things. So the secret acts as a symmetric key
  - Credit cards are in a file called autofill-profiles.json
  - This all implies a very interesting conundrum for backups! How do you back up credit cards, and make it so that those backups can occur silently in the background, but also so that the backups are portable across devices
  - When we create a backup, a user can choose to have that backup encrypted or not encrypted.
  - If they choose to not encrypt their backup, we're done - we're not even going to store credit cards in it, so nothing to do.
  - If they did choose to encrypt their backup, then what we'll do is this: when enabling encrypted backups, then ask the user to authenticate to the native OSKeyStore, and we exfiltrate the secret and then we store it in the encrypted backup, encrypted using one of the keys derived from the backup password.
  - Note: this is only as secure as the user's backup password. We need to encourage users to use a very strong one.
  - Then at recovery time, we create a secondary temporary OSKeyStore instance, unwrap the original secret, and then use the temporary OSKeyStore to decrypt the credit cards, and then we re-encrypt them using the "local" OSKeyStore (the one that is used on the current machine). Then we overwrite the original autofill-profiles.json, and then move that file into the new recovery profile.
  - Ideas for tests:
    - Update the integration test to ensure that we don't accidentally overwrite any real/useful secrets on the machine the test is running on.
    - Make sure that CredentialsAndSecurityBackupResource will do the decryption and re-encryption properly and produce encrypted bytes for the cards
      - Making sure we don't accidentally store a plaintext credit card number inside of autofill-profiles.json during recovery in CredentialsAndSecurityBackupResource
      - Make sure this will work if the secret is common between the device that was backed up, and the device that was recovered on, or if the secret is different between the two.
* Must end at precisely 2:30ET due to a meeting. Sorry!


* [Rate this episode](https://forms.gle/tFjRn2B37jPDGmGu9)

## Chat
* [Join us on Matrix!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist)

## Other
* [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
* [npb hacks](https://www.twitch.tv/BackToTheCode) on the SpiderMonkey JS engine
* [Compiler Compiler](https://www.twitch.tv/codehag) live stream
* Try out Mozilla [VPN](https://vpn.mozilla.org/)
* How mconley uses [Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
* [Fission](https://firefox-source-docs.mozilla.org/dom/dom/Fission.html) - Read more about it
* [mozconfigwrapper](https://github.com/ahal/mozconfigwrapper) - A Wrapper to keep different mozconfigs
* [MyQOnly](https://addons.mozilla.org/en-US/firefox/addon/myqonly/) Mikes Addon for showing how many reviews are in your review queue - [Source at Github](https://github.com/mikeconley/myqonly)
* [Mike's Firefox Color Theme](https://addons.mozilla.org/en-US/firefox/addon/electricbluegaloo/)
* Check if a service you are using, has been part of a breach via [Firefox Monitor](https://monitor.firefox.com/breaches)
* [Codetribute](https://codetribute.mozilla.org/) - Help contribute to Firefox, good mentored bugs for You.
  - First, [Create](https://bugzilla.mozilla.org/createaccount.cgi) a Mozilla Bugzilla account.

