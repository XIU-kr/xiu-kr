<div align="center">

<img src="./assets/readme-hero.svg" alt="XIU — a curious developer from Seoul" width="100%">

</div>

<br>

> *"이걸 더 편하게 쓸 수 있을 텐데."*
> When that thought arrives, I build the fix.

I'm a self-taught developer in Seoul shipping things across **AI tooling**, **game-server infrastructure**, **church technology**, and the **open web**. Most of what I build started because I wanted to use it myself — and most of it is still running.

<br>

---

## ⌗ &nbsp; Selected Work

<table>
<tr>
<td width="50%" valign="top">

### №&nbsp;01 &nbsp; Vora&nbsp;AI

<sub>`flagship` &nbsp;·&nbsp; `typescript` &nbsp;·&nbsp; `react` &nbsp;·&nbsp; `big-lama` &nbsp;·&nbsp; `sam`</sub>

A **Photoshop-class AI image editor** running entirely in the browser. 18+ tools — Big-LaMa inpainting, SAM segmentation, layer masks, adjustment layers, clone stamp, healing brush, bezier paths. GPU-accelerated, non-destructive, offline-capable.

</td>
<td width="50%" valign="top">

### №&nbsp;02 &nbsp; Quon

<sub>`vanilla js` &nbsp;·&nbsp; `kotlin` &nbsp;·&nbsp; `compose` &nbsp;·&nbsp; `camerax` &nbsp;·&nbsp; `ml kit`</sub>

A **free, ad-light QR generator** on the web (`quon.xiu.kr`) and as a native Android app. Seven QR types, full design customization, real-time camera scanning. Built because every other generator was buried in ads.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### №&nbsp;03 &nbsp; bbangyadan

<sub>`discord.js` &nbsp;·&nbsp; `express` &nbsp;·&nbsp; `mysql` &nbsp;·&nbsp; `ejs` &nbsp;·&nbsp; `pm2`</sub>

A complete **Discord clan operations platform** — point shop & inventory, dynamic voice channels, voice activity tracking, embed template editor, OP.GG / Valorant tier auto-sync, KST cron schedulers, separate TTS bot pool. One Node process, MySQL-backed, zero-downtime via PM2.

</td>
<td width="50%" valign="top">

### №&nbsp;04 &nbsp; Phos

<sub>`python` &nbsp;·&nbsp; `react` &nbsp;·&nbsp; `fastapi` &nbsp;·&nbsp; `python-pptx`</sub>

A **worship-PPT auto-generator** that assembles slides from 645 hymn lyrics and the Korean Revised Bible against the week's worship program. Built because copy-pasting hymn lyrics every Saturday was unbearable.

</td>
</tr>
<tr>
<td width="50%" valign="top">

### №&nbsp;05 &nbsp; CornerBrand

<sub>`typescript` &nbsp;·&nbsp; `docker` &nbsp;·&nbsp; `local-first`</sub>

A **local-first web app** that adds corner logos to images, PDFs, and PPTX files. Real-time preview, zero uploads, multiple export formats. Designed for sensitive internal documents that should never leave the device.

</td>
<td width="50%" valign="top">

### №&nbsp;06 &nbsp; CS2&nbsp;Plugins

<sub>`c#` &nbsp;·&nbsp; `counterstrikesharp` &nbsp;·&nbsp; `discord`</sub>

Three open-source plugins for the `cs2.kr` community server:
**GrenadeBoost** — custom physics for grenade boosting.
**AutoRestart** — timezone-aware scheduled restarts.
**DU-NicknameSync** — Steam ↔ Discord nickname auto-sync.

</td>
</tr>
</table>

<br>

---

## ⌗ &nbsp; Stack

```text
$ xiu --stack

  language     typescript · javascript · kotlin · c# · python · php · swift
  frontend     react · jetpack compose · vanilla js · pwa · ejs · tailwind
  backend      node.js · express · fastapi · counterstrikesharp · mysql
  ai · ml      big-lama · sam · ml kit · camerax · zxing
  mobile       android (compose · camerax · ml kit · play billing · admob)
  infra        docker · pterodactyl · cloudflare · opnsense · pm2 · nginx
  cms          rhymix · wordpress · woocommerce
```

<br>

---

## ⌗ &nbsp; Infrastructure

I design and operate a **multi-layered server architecture** for everything I run.
Game servers, web services, and church platforms all sit behind the same hardware-firewall-and-edge stack.

```text
   ┌── cloudflare ─────────── ddos · cdn · edge security · dns
   │
   ├── opnsense ────────────── hardware firewall  ·  game-server protection
   │
   ├── docker ──────────────── containerized services
   │   ├── pterodactyl ────── game server management panel
   │   ├── nginx ──────────── reverse proxy · http cache
   │   └── pm2 ─────────────── node process supervisor
   │
   └── monitoring ──────────── real-time status · auto alerts · backups
```

<br>

---

## ⌗ &nbsp; Live

<table>
<thead>
  <tr>
    <th align="left">Platform</th>
    <th align="left">Description</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td><a href="https://xiu.kr"><code>xiu.kr</code></a></td>
    <td>Developer portfolio &nbsp;·&nbsp; <em>this site</em></td>
  </tr>
  <tr>
    <td><a href="https://quon.xiu.kr"><code>quon.xiu.kr</code></a></td>
    <td>Free multilingual QR code generator</td>
  </tr>
  <tr>
    <td><a href="https://bbangyadan.kr"><code>bbangyadan.kr</code></a></td>
    <td>Discord clan operations web panel</td>
  </tr>
  <tr>
    <td><a href="https://cs2.kr"><code>cs2.kr</code></a></td>
    <td>500+ member CS2 community server</td>
  </tr>
  <tr>
    <td><a href="https://dongtanms.kr"><code>dongtanms.kr</code></a></td>
    <td>Dongtan Myungsung Church platform</td>
  </tr>
  <tr>
    <td><a href="https://repentanceheaven.kr"><code>repentanceheaven.kr</code></a></td>
    <td>Mission organization website</td>
  </tr>
  <tr>
    <td><a href="https://shop.repentanceheaven.kr"><code>shop.repentanceheaven.kr</code></a></td>
    <td>Mission shop &nbsp;·&nbsp; prayer guides & pastoral books, proceeds fund missionary work</td>
  </tr>
</tbody>
</table>

<br>

---

<div align="center">

<br>

◈ &nbsp; ◈ &nbsp; ◈

<br>

**Open to project collaborations, technical questions, or just saying hello.**

<br>

<a href="mailto:contact@xiu.kr">
  <img src="https://img.shields.io/badge/email-contact%40xiu.kr-d4a016?style=flat-square&labelColor=07070b" alt="email">
</a>
&nbsp;
<a href="https://github.com/XIU-kr">
  <img src="https://img.shields.io/badge/github-XIU--kr-d4a016?style=flat-square&labelColor=07070b&logo=github&logoColor=d4a016" alt="github">
</a>
&nbsp;
<a href="https://linkedin.com/in/xiukr">
  <img src="https://img.shields.io/badge/linkedin-xiukr-d4a016?style=flat-square&labelColor=07070b&logo=linkedin&logoColor=d4a016" alt="linkedin">
</a>
&nbsp;
<a href="https://discord.com/users/xiu_kr">
  <img src="https://img.shields.io/badge/discord-xiu__kr-d4a016?style=flat-square&labelColor=07070b&logo=discord&logoColor=d4a016" alt="discord">
</a>

<br><br>

<sub><code>xiu.kr</code> &nbsp; · &nbsp; <em>built with curiosity</em> &nbsp; · &nbsp; <code>2026</code></sub>

</div>
