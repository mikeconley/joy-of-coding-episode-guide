**Reminder - no plan survives breakfast.**

[Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)

- Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
- [Here’s a contributing guide!](https://github.com/mikeconley/joy-of-coding-episode-guide/blob/master/CONTRIBUTING.md)
- [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!

**Today**

* Designing and writing tests for the OSKeyStore recovery mechanism
	* Firefox has the ability to store payment methods (credit cards)
	* We _never_ want to store the credit cards in plaintext on the filesystem
	* So therefore, we must encrypt the credit cards, and only decrypt them on demand
	* How does this encryption work? It's actually quite similar to how other browsers (specifically Chrome-based browsers) do it.
	* OSKeyStore is a JavaScript module, and it wraps an XPCOM component that is (perhaps confusingly) also called OSKeyStore, but within the JS module the XPCOM component is called nativeOSKeyStore.
	* How does nativeOSKeyStore work? Well, it uses the underlying OS's secret storage mechanism to hold on to a _single secret_.
		* Windows: DPAPI
		* macOS: KeyChain
		* Linux/GTK: libsecret
	* Say you're saving a credit card for the first time - you've never done it before. Firefox will randomly generate a "secret" set of bytes with high-entropy, and store it in the underlying secure storage.
	* You use the secret as the _key_ to encrypt things. So the secret acts as a symmetric key
	* Credit cards are in a file called autofill-profiles.json
	* This all implies a very interesting conundrum for backups! How do you back up credit cards, and make it so that those backups can occur silently in the background, but also so that the backups are *portable across devices*
	* When we create a backup, a user can choose to have that backup encrypted or not encrypted.
	* If they choose to not encrypt their backup, we're done - we're not even going to store credit cards in it, so nothing to do.
	* If they _did_ choose to encrypt their backup, then what we'll do is this: when enabling encrypted backups, _then_ ask the user to authenticate to the native OSKeyStore, and we _exfiltrate the secret_ and then we store it in the encrypted backup, encrypted using one of the keys derived from the backup password.
	* Note: this is only as secure as the user's backup password. We need to encourage users to use a very strong one. 
	* Then at recovery time, we create a _secondary temporary OSKeyStore instance_, unwrap the original secret, and then use the temporary OSKeyStore to decrypt the credit cards, and then we _re-encrypt them_ using the "local" OSKeyStore (the one that is used on the current machine). Then we overwrite the original autofill-profiles.json, and then move that file into the new recovery profile.
	* Ideas for tests:
		* Update the integration test to _ensure that we don't accidentally overwrite any real/useful secrets on the machine the test is running on_.
		* Make sure that CredentialsAndSecurityBackupResource will do the decryption and re-encryption properly and produce encrypted bytes for the cards
			* Making sure we don't accidentally store a plaintext credit card number inside of autofill-profiles.json during recovery in CredentialsAndSecurityBackupResource
			* Make sure this will work if the secret is _common_ between the device that was backed up, and the device that was recovered on, or if the secret is _different_ between the two.
		* 
* Must end at precisely 2:30ET due to a meeting. Sorry!

**[Rate this episode](https://forms.gle/tFjRn2B37jPDGmGu9)**

**Chat**

- [Join us in the Livehacking room on Mozilla’s Matrix instance!](https://matrix.to/#/!enWuAmKDOEEPYejXRk:mozilla.org?via=mozilla.org&via=raim.ist) Here’s [documentation on how to join](https://wiki.mozilla.org/Matrix). I’m only sorta monitoring the Twitch chat. A bot will try to bridge Matrix and Twitch (joc-bridgebot).

**Links**

- [Felicia Bacon](https://www.youtube.com/channel/UCMtqVykGztIYmj7OpFf7oeQ/videos)
- [nbp hacks on the SpiderMonkey JS engine](https://www.twitch.tv/BackToTheCode)
- [Alessandro Castellani has been streaming himself livehacking on Thunderbird](https://www.youtube.com/c/AlessandroCastellani/videos)
- [emilio hacks on Firefox!](https://www.youtube.com/channel/UCYbsdvH4_52BFAijFVgYGgA)
- [Compiler Compiler - watch a Mozilla engineer hack on the SpiderMonkey JavaScript engine!](https://www.twitch.tv/codehag)
- [How mconley uses Mercurial](https://mikeconley.github.io/documents/How_mconley_uses_Mercurial_for_Mozilla_code)
- [Andreas Kling hacks on a custom browser engine for a hand-rolled OS called SerenityOS](https://www.youtube.com/playlist?list=PLMOpZvQB55be0Nfytz9q2KC_drvoKtkpS)
- [The Joy of Coding: Community-Run Episode guide](https://mikeconley.github.io/joy-of-coding-episode-guide/)
    - Feel free to send [pull requests](https://help.github.com/articles/about-pull-requests/) to the [repo](https://github.com/mikeconley/joy-of-coding-episode-guide)!
    - [Here’s the guide for creating pull requests that smurfd used and recommends](https://akrabat.com/the-beginners-guide-to-contributing-to-a-github-project/%20)!
- [I've been mirroring the episodes to YouTube](https://www.youtube.com/playlist?list=PLmaFLMwlbk8wKMvfEEzp9Hfdlid8VYpL5)
- [Code Therapy with Danny O’Brien](https://www.youtube.com/channel/UCDShi-SQdFVRnQrMla9G_kQ)
- Watch a developer put together a Windows game from scratch (no third-part engines) - really great explanations: https://handmadehero.org/
- [/r/WatchPeopleCode](https://www.reddit.com/r/WatchPeopleCode) for more livehacking!

**Glossary**

- BHR - “Background Hang Reporter”, a thing that records information about when Firefox performs poorly and sends it over Telemetry
- e10s ("ee ten ESS") - short for [Electrolysis, which is the multi-process Firefox project](https://wiki.mozilla.org/Electrolysis)
- CPOW ("ka-POW" or sometimes "SEE-pow") = Cross-Process Object Wrapper. [See this blog post.](http://mikeconley.ca/blog/2015/02/17/on-unsafe-cpow-usage-in-firefox-desktop-and-why-is-my-nightly-so-sluggish-with-e10s-enabled/)
- Deserialize - "turn a serialized object back into the complex object”
- Serialize - "turn a complex object into something that can be represented as primitives, like strings, integers, etc
- Regression - something that made behaviour worse rather than better. Regress means to “go backward”, more or less.
- l10n - localization
- a11y - accessibility
- i18n - internationalization
- k8s - kubernetes

**Feedback**

- [@mconley@mozilla.social on Mastodon](https://mozilla.social/@mconley)
- [@mike_conley on Twitter](https://twitter.com/mike_conley)
- You can chat with me on [Matrix](https://wiki.mozilla.org/Matrix) at @mconley:mozilla.org
- [mikeconley.ca/blog](http://mikeconley.ca/blog/)
- mconley at mozilla dot com