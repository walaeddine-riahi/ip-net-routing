chapters = {
  "Chapitre 0 : Rappel & Configuration de base": {
    "content": """
<h3>📦 Types de câbles et connexions</h3>
<ul>
<li>🟢 Console : pour configurer le routeur depuis un PC</li>
<li>🔵 Câble croisé : entre deux équipements de même famille (routeur-routeur, PC-serveur)</li>
<li>🟡 Câble droit : entre équipements de familles différentes (routeur-switch)</li>
</ul>
<img src="images/cables-router.png" width="450"/>

<h3>🔐 Modes de commande Cisco</h3>
<ol>
<li><b>Utilisateur</b> – <code>Router></code> – Lecture seule</li>
<li><b>Privilégié</b> – <code>Router#</code> – <code>enable</code></li>
<li><b>Configuration</b> – <code>Router(config)#</code> – <code>configure terminal</code></li>
</ol>

<h3>⚙️ Configuration de base</h3>
<pre>
hostname R1
no ip domain-lookup
banner motd #Bienvenue#
enable secret esprit
service password-encryption
</pre>

<h3>🔒 Mots de passe</h3>
<ul>
<li><b>Enable</b> : <code>enable password</code> / <code>enable secret</code> (crypté)</li>
<li><b>Console</b> : <code>line console 0 → password → login</code></li>
<li><b>VTY (Telnet/SSH)</b> : <code>line vty 0 4</code></li>
</ul>

<h3>💾 Sauvegarde</h3>
<pre>copy running-config startup-config</pre>

<h3>🌐 Interfaces</h3>
<pre>
interface g0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
</pre>
""",
    "flashcard": """
<h4>📗 Flashcard : Types de câbles réseau</h4>
<ul>
  <li><b>Câble Console :</b> Câble série RS-232 utilisé pour accès local à un routeur via PC.</li>
  <li><b>Câble croisé :</b> Connecte deux équipements similaires sans switch.</li>
  <li><b>Câble droit :</b> Connecte équipements différents (ex: routeur à switch).</li>
</ul>

<h4>📗 Flashcard : Modes de commande Cisco</h4>
<ol>
  <li><b>Utilisateur (Router&gt;):</b> Lecture seule.</li>
  <li><b>Privilégié (Router#):</b> Diagnostic avancé (<code>enable</code>).</li>
  <li><b>Configuration (Router(config)#):</b> Configuration réseau (<code>configure terminal</code>).</li>
</ol>

<h4>📗 Flashcard : Configuration de base</h4>
<ul>
  <li><code>hostname</code>: Nom du routeur.</li>
  <li><code>no ip domain-lookup</code>: Désactive la recherche DNS.</li>
  <li><code>banner motd</code>: Message d’accueil.</li>
  <li><code>enable secret</code>: Mot de passe crypté.</li>
  <li><code>service password-encryption</code>: Chiffre tous les mots de passe.</li>
</ul>

<h4>📗 Flashcard : Sauvegarde</h4>
<p>La config en RAM est volatile. Utilisez <code>copy running-config startup-config</code> pour la sauvegarder en NVRAM.</p>
"""
  },

  "Chapitre 1 : Routage statique": {
    "content": """
<h2>🧭 Objectifs pédagogiques</h2>
<ul>
    <li>Comprendre le rôle du routage statique</li>
    <li>Maîtriser la configuration de routes simples, par défaut, flottantes</li>
    <li>Analyser les avantages et limites dans une topologie réseau</li>
</ul>

<h2>📖 Cours enrichi</h2>
<p>Le routage statique repose sur des routes configurées manuellement. Simple, mais peu flexible.</p>

<h3>🔧 Configuration</h3>
<pre>
ip route 192.168.10.0 255.255.255.0 10.0.0.2
ip route 0.0.0.0 0.0.0.0 10.0.0.1     &lt;-- route par défaut
ip route 192.168.20.0 255.255.255.0 10.0.0.2 200 &lt;-- route flottante
</pre>

<h3>✅ Avantages</h3>
<ul>
    <li>Sécurité : pas de diffusion</li>
    <li>Prévisibilité</li>
    <li>Faible charge CPU</li>
</ul>

<h3>⚠️ Inconvénients</h3>
<ul>
    <li>Pas de tolérance aux pannes sans routes flottantes</li>
    <li>Maintenance manuelle fastidieuse</li>
</ul>
""",
    "flashcard": """
<h4>📗 Flashcard : Routage statique</h4>
<ul>
  <li>Les routes sont configurées manuellement avec la commande <code>ip route</code>.</li>
  <li>La route par défaut est définie avec <code>0.0.0.0 0.0.0.0</code>.</li>
  <li>Une route flottante est une route de secours avec une métrique plus élevée (ex: 200).</li>
  <li>Avantages : simplicité, sécurité, prévisibilité, faible charge CPU.</li>
  <li>Inconvénients : pas adaptatif, nécessite maintenance manuelle.</li>
</ul>
"""
  },

  "Chapitre 3 : RIP dynamique": {
    "content": """
<h3>🌐 Introduction au Routage Dynamique</h3>
<p>RIP : protocole à vecteur de distance, limite 15 sauts, mise à jour toutes les 30s via UDP 520.</p>

<h3>🕒 Timers RIP</h3>
<ul>
<li>Update : 30 s</li>
<li>Invalid : 180 s</li>
<li>Flush : 240 s</li>
<li>Hold Down : 180 s</li>
</ul>

<h3>🚦 Boucles de routage : solutions</h3>
<ul>
<li>Split Horizon</li>
<li>Hold Down</li>
<li>Poison Reverse</li>
<li>Métrique infinie</li>
</ul>
""",
    "flashcard": """
<h4>📗 Flashcard : RIP</h4>
<ul>
  <li>RIP utilise l'algorithme Bellman-Ford.</li>
  <li>Limite de 15 sauts maximum.</li>
  <li>Mises à jour toutes les 30 secondes (UDP port 520).</li>
  <li>Techniques anti-boucles : Split Horizon, Poison Reverse, Hold Down.</li>
</ul>
"""
  },

  "Chapitre 4 : OSPF Point-à-Point": {
    "content": """
<h3>📘 Présentation du protocole OSPF</h3>
<p>OSPF est un protocole à état de liens utilisant Dijkstra.</p>

<h3>📈 Caractéristiques d’OSPF</h3>
<ul>
<li>Supporte VLSM et CIDR</li>
<li>Hiérarchie en zones (zone 0 = backbone)</li>
<li>Mises à jour déclenchées</li>
<li>Supporte authentification MD5/SHA</li>
</ul>

<h3>🔁 Fonctionnement en 5 étapes</h3>
<ol>
<li>Découverte des voisins (Hello)</li>
<li>Échange des LSAs</li>
<li>Création de la base LSDB</li>
<li>Calcul arbre SPF (Dijkstra)</li>
<li>Génération table routage</li>
</ol>
""",
    "flashcard": """
<h4>📗 Flashcard : OSPF</h4>
<ul>
  <li>Protocole à état de liens, utilise Dijkstra.</li>
  <li>Hiérarchique avec zones, zone 0 obligatoire.</li>
  <li>Mises à jour déclenchées, pas périodiques.</li>
  <li>Étapes : Hello, échange LSAs, LSDB, calcul SPF, mise à jour table.</li>
</ul>
"""
  },

  "Chapitre 5 : OSPF à accès multiple": {
    "content": """
<h3>🌐 OSPF à Accès Multiple</h3>
<p>Dans un réseau Ethernet, plusieurs routeurs partagent un segment.</p>

<h3>🧠 Objectif</h3>
<ul>
<li>Réduire le trafic en désignant un DR</li>
<li>BDR : secours si DR échoue</li>
<li>DROTHER : autres routeurs</li>
</ul>

<h3>🔄 Élection DR / BDR</h3>
<ol>
<li>Priorité la plus haute (0-255)</li>
<li>Si égalité, router ID le plus élevé</li>
<li>DR/BDR restent stables sauf échec</li>
</ol>
""",
    "flashcard": """
<h4>📗 Flashcard : OSPF accès multiple</h4>
<ul>
  <li>DR centralise les mises à jour pour réduire le flood.</li>
  <li>BDR prend la relève si DR échoue.</li>
  <li>Priorité OSPF décide de l’élection.</li>
  <li>Router ID départage en cas d’égalité.</li>
</ul>
"""
  },

  "Chapitre 6 : NAT & PAT": {
    "content": """
<h3>🌍 NAT - Translation d’Adresses Réseau</h3>
<p>Traduction des adresses IP privées en IP publiques.</p>

<h3>🛠️ Types de NAT</h3>
<ul>
<li>NAT statique : 1:1</li>
<li>NAT dynamique : pool IP publiques</li>
<li>PAT : surcharge, plusieurs IP privées via ports uniques</li>
</ul>

<h3>⚙️ Configuration PAT</h3>
<pre>
access-list 1 permit 192.168.0.0 0.0.0.255
ip nat inside source list 1 interface g0/0 overload
</pre>
""",
    "flashcard": """
<h4>📗 Flashcard : NAT & PAT</h4>
<ul>
  <li>NAT statique : correspondance IP privée/publique fixe.</li>
  <li>NAT dynamique : pool d’IP publiques disponibles dynamiquement.</li>
  <li>PAT (overload) : partage une IP publique avec ports différents.</li>
  <li>Configuration : définir ACL, pool, interfaces inside/outside.</li>
</ul>
"""
  }
}
