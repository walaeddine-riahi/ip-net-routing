quizzes = {
  "Chapitre 0 : Rappel & Configuration de base": [
    {
      "question": "Quel type de câble utilise-t-on pour connecter un routeur à un switch ?",
      "options": ["Croisé", "Droit", "Console"],
      "answer": "Droit",
      "flashcard": "Un câble droit est utilisé pour connecter des équipements de types différents (ex: routeur à switch). Le câble croisé sert pour équipements similaires."
    },
    {
      "question": "Quelle commande active le mode de configuration globale ?",
      "options": ["enable", "configure terminal", "show running-config"],
      "answer": "configure terminal",
      "flashcard": "La commande 'configure terminal' permet d’entrer dans le mode configuration globale pour configurer le routeur."
    },
    {
      "question": "Quel câble est utilisé pour connecter deux routeurs ensemble ?",
      "options": ["Croisé", "Droit", "Console"],
      "answer": "Croisé",
      "flashcard": "Le câble croisé est utilisé pour relier deux équipements similaires, comme deux routeurs directement."
    },
    {
      "question": "Quel câble est utilisé pour relier un PC à un routeur pour configuration ?",
      "options": ["Droit", "Croisé", "Console"],
      "answer": "Console",
      "flashcard": "Le câble console sert à connecter un PC au port console du routeur pour la configuration locale."
    },
    {
      "question": "Sur quelle interface du PC branche-t-on le câble console ?",
      "options": ["USB", "RS-232", "Ethernet"],
      "answer": "RS-232",
      "flashcard": "Le câble console classique utilise une interface série RS-232 (ou adaptateur USB-série)."
    },
    {
      "question": "Sur quelle interface du routeur branche-t-on le câble console ?",
      "options": ["Ethernet", "Console", "FastEthernet"],
      "answer": "Console",
      "flashcard": "Le câble console se connecte au port console dédié du routeur."
    },
    {
      "question": "Quelle commande désactive la recherche DNS sur un routeur Cisco ?",
      "options": ["no dns-lookup", "disable dns", "no ip domain-lookup"],
      "answer": "no ip domain-lookup",
      "flashcard": "La commande 'no ip domain-lookup' empêche le routeur de tenter de résoudre les commandes inconnues en DNS."
    },
    {
      "question": "Comment configurer un message de bienvenue sur un routeur Cisco ?",
      "options": ["banner message Hello", "motd banner Hello", "banner motd #Hello#"],
      "answer": "banner motd #Hello#",
      "flashcard": "La syntaxe correcte pour le message MOTD est 'banner motd #message#' où # est le délimiteur."
    },
    {
      "question": "Quelle commande crypte tous les mots de passe ?",
      "options": ["enable encryption", "service password-encryption", "encrypt all-passwords"],
      "answer": "service password-encryption",
      "flashcard": "La commande 'service password-encryption' active le chiffrement des mots de passe en clair dans la config."
    },
    {
      "question": "Quelle commande permet de sauvegarder la configuration dans la NVRAM ?",
      "options": ["save config", "copy running-config startup-config", "write config"],
      "answer": "copy running-config startup-config",
      "flashcard": "Cette commande sauvegarde la config en cours dans la mémoire de démarrage (NVRAM)."
    },
    {
      "question": "Quelle commande permet d’entrer en mode privilégié ?",
      "options": ["login", "enable", "exec"],
      "answer": "enable",
      "flashcard": "La commande 'enable' permet d’entrer en mode privilégié pour accéder à des commandes avancées."
    },
    {
      "question": "Que permet la commande 'show running-config' ?",
      "options": ["Afficher la config sauvegardée", "Afficher la config en cours", "Modifier la config"],
      "answer": "Afficher la config en cours",
      "flashcard": "'show running-config' affiche la configuration active en mémoire (non sauvegardée)."
    }
  ],

  "Chapitre 1 : Routage statique": [
    {
      "question": "Quelle est la fonction du routage ?",
      "options": ["Configurer les interfaces", "Transférer des paquets d'une source vers une destination", "Crypter les données dans le réseau"],
      "answer": "Transférer des paquets d'une source vers une destination",
      "flashcard": "Le routage consiste à transférer les paquets au bon destinataire via les différents réseaux."
    },
    {
      "question": "Quels sont deux avantages du routage statique ?",
      "options": ["Sécurisé et faible charge CPU", "Automatique et rapide", "Multicast et compression"],
      "answer": "Sécurisé et faible charge CPU",
      "flashcard": "Le routage statique est plus sécurisé car configuré manuellement et consomme peu de ressources CPU."
    },
    {
      "question": "Que signifie 'S*' dans une table de routage Cisco ?",
      "options": ["Route par défaut", "Route flottante", "Route dynamique"],
      "answer": "Route par défaut",
      "flashcard": "'S*' désigne la route statique par défaut dans la table de routage Cisco."
    },
    {
      "question": "Quel type de route permet un chemin de secours ?",
      "options": ["Route dynamique", "Route flottante", "Route connectée"],
      "answer": "Route flottante",
      "flashcard": "Une route flottante est une route statique avec une distance administrative plus élevée, utilisée comme secours."
    },
    {
      "question": "Vers quelle interface le trafic destiné à 192.168.10.3 est-il acheminé si la route existe ?",
      "options": ["g0/0", "s0/0/0", "f0/1"],
      "answer": "g0/0",
      "flashcard": "La route indique que les paquets vers 192.168.10.3 passent par l'interface GigabitEthernet0/0."
    },
    {
      "question": "Quel mot-clé est utilisé pour une route par défaut en Cisco IOS ?",
      "options": ["default-route", "0.0.0.0 0.0.0.0", "ip default-route"],
      "answer": "0.0.0.0 0.0.0.0",
      "flashcard": "La route par défaut utilise l'adresse réseau 0.0.0.0 avec masque 0.0.0.0 pour attraper tout le trafic non spécifié."
    },
    {
      "question": "Que permet la commande 'ip route 192.168.1.0 255.255.255.0 10.0.0.2' ?",
      "options": ["Créer une route dynamique", "Ajouter une route statique vers 192.168.1.0", "Supprimer une route"],
      "answer": "Ajouter une route statique vers 192.168.1.0",
      "flashcard": "Cette commande ajoute une route statique vers le réseau 192.168.1.0 via la passerelle 10.0.0.2."
    },
    {
      "question": "Qu'est-ce qu'une route flottante ?",
      "options": ["Une route OSPF", "Une route avec distance administrative plus élevée", "Une route utilisée pour le multicast"],
      "answer": "Une route avec distance administrative plus élevée",
      "flashcard": "La route flottante sert de secours, ayant une distance administrative plus élevée que la route principale."
    },
    {
      "question": "Quelle commande affiche la table de routage ?",
      "options": ["show ip table", "show ip route", "show route-config"],
      "answer": "show ip route",
      "flashcard": "La commande 'show ip route' affiche la table de routage du routeur."
    },
    {
      "question": "Quel est l’effet de la commande 'no shutdown' sur une interface ?",
      "options": ["Elle arrête l’interface", "Elle active l’interface", "Elle vérifie l’interface"],
      "answer": "Elle active l’interface",
      "flashcard": "Par défaut, les interfaces sont désactivées; 'no shutdown' active l'interface."
    }
  ],

  "Chapitre 3 : RIP dynamique": [
    {
      "question": "Quel est le chemin optimal de R1 vers 172.16.3.0/24 ?",
      "options": ["R1-R2", "R1-R3", "R1-R2-R3"],
      "answer": "R1-R3",
      "flashcard": "Selon la métrique RIP, le chemin R1-R3 est le plus court vers 172.16.3.0/24."
    },
    {
      "question": "Combien de secondes RIP conserve-t-il une route inactive avant suppression ?",
      "options": ["180", "240", "300"],
      "answer": "240",
      "flashcard": "RIP maintient une route inactive 240 secondes avant de la retirer."
    },
    {
      "question": "Pourquoi certains sous-réseaux n’apparaissent-ils pas dans RIP ?",
      "options": ["Mauvais câble", "Routage dynamique désactivé", "Résumé automatique activé"],
      "answer": "Résumé automatique activé",
      "flashcard": "Le résumé automatique masque les sous-réseaux dans la table RIP."
    },
    {
      "question": "Quelle commande corrige ce problème ?",
      "options": ["version 2", "auto-summary", "no auto-summary"],
      "answer": "no auto-summary",
      "flashcard": "La commande 'no auto-summary' désactive le résumé automatique et affiche tous les sous-réseaux."
    },
    {
      "question": "Quelle commande affiche la table de routage RIP ?",
      "options": ["show ip route", "show running-config", "show protocols"],
      "answer": "show ip route",
      "flashcard": "'show ip route' montre toutes les routes, y compris celles apprises par RIP."
    },
    {
      "question": "Quelle version de RIP supporte les masques de sous-réseaux ?",
      "options": ["RIP v1", "RIP v2", "Les deux"],
      "answer": "RIP v2",
      "flashcard": "RIP version 2 supporte le classless routing, incluant les masques de sous-réseaux variables."
    },
    {
      "question": "Quel protocole utilise RIP pour envoyer ses messages ?",
      "options": ["TCP", "UDP", "ICMP"],
      "answer": "UDP",
      "flashcard": "RIP utilise UDP sur le port 520 pour l’échange de ses messages."
    },
    {
      "question": "Quel est le nombre maximum de sauts permis par RIP ?",
      "options": ["15", "10", "20"],
      "answer": "15",
      "flashcard": "RIP considère 16 sauts comme infini, limitant à 15 le nombre maximum de sauts."
    }
  ],

  "Chapitre 4 : OSPF Point-à-Point": [
    {
      "question": "Quelles sont deux raisons de préférer OSPF à RIP ?",
      "options": ["Mise à jour partielle et convergence rapide", "Utilisation de TCP et de ports élevés", "Peu adapté aux grands réseaux"],
      "answer": "Mise à jour partielle et convergence rapide",
      "flashcard": "OSPF envoie uniquement les mises à jour partielles et converge plus rapidement que RIP."
    },
    {
      "question": "Quelles sont les conditions pour former un voisinage OSPF ?",
      "options": ["Même masque, même zone, même MTU", "Même Hello interval, Dead interval, même zone", "Même ID routeur, même priorité, même interface"],
      "answer": "Même Hello interval, Dead interval, même zone",
      "flashcard": "Pour former un voisinage OSPF, les routeurs doivent avoir les mêmes timers Hello/Dead et appartenir à la même zone."
    },
    {
      "question": "Quelle est la formule du coût OSPF ?",
      "options": ["BP de référence / BP interface", "BP interface / BP de référence", "Distance administrative * BP"],
      "answer": "BP de référence / BP interface",
      "flashcard": "Le coût OSPF est calculé en divisant la bande passante de référence par celle de l'interface."
    },
    {
      "question": "Quelle est la distance administrative d’OSPF ?",
      "options": ["90", "100", "110"],
      "answer": "110",
      "flashcard": "La distance administrative standard d'OSPF est 110."
    },
    {
      "question": "Que signifie un voisin OSPF en état FULL/DR ?",
      "options": ["Relation complète avec DR", "Relation partielle avec BDR", "Lien inactif"],
      "answer": "Relation complète avec DR",
      "flashcard": "FULL/DR signifie que la relation avec le routeur désigné (DR) est complètement établie."
    },
    {
      "question": "Quel protocole de couche 3 utilise OSPF ?",
      "options": ["TCP", "UDP", "IP (protocole 89)"],
      "answer": "IP (protocole 89)",
      "flashcard": "OSPF utilise directement le protocole IP numéro 89 (pas TCP/UDP)."
    },
    {
      "question": "Qu’est-ce qu’un LSA dans OSPF ?",
      "options": ["Liste de sous-réseaux actifs", "Link-State Advertisement", "Level Switching Algorithm"],
      "answer": "Link-State Advertisement",
      "flashcard": "LSA est un message contenant l’état des liens, utilisé pour construire la base de données OSPF."
    },
    {
      "question": "Qu'est-ce que la zone backbone dans OSPF ?",
      "options": ["Zone 10", "Zone 0", "Zone 1"],
      "answer": "Zone 0",
      "flashcard": "La zone backbone (Zone 0) est la zone centrale obligatoire dans OSPF."
    },
    {
      "question": "Quel algorithme utilise OSPF ?",
      "options": ["Bellman-Ford", "Dijkstra", "Flooding"],
      "answer": "Dijkstra",
      "flashcard": "OSPF utilise l’algorithme de Dijkstra pour calculer les chemins les plus courts."
    },
    {
      "question": "Quel est le format de l'identifiant de routeur OSPF ?",
      "options": ["Adresse MAC", "Numéro binaire", "Adresse IP"],
      "answer": "Adresse IP",
      "flashcard": "L’identifiant de routeur OSPF est une adresse IP unique utilisée pour l’identification."
    }
  ],

  "Chapitre 5 : OSPF à accès multiple": [
    {
      "question": "Comment forcer R1 à être élu DR ?",
      "options": ["ip ospf priority 255", "router-id 0.0.0.0", "clear ospf election"],
      "answer": "ip ospf priority 255",
      "flashcard": "La priorité OSPF 255 garantit que le routeur est élu Designated Router (DR)."
    },
    {
      "question": "Si une loopback est configurée, quelle adresse sera choisie comme router-id ?",
      "options": ["Adresse IP la plus basse", "Loopback la plus haute", "Interface active la plus rapide"],
      "answer": "Loopback la plus haute",
      "flashcard": "OSPF choisit comme router-id la loopback avec la plus haute adresse IP."
    },
    {
      "question": "Pourquoi un router-id configuré manuellement n'est-il pas pris en compte immédiatement ?",
      "options": ["Il faut sauvegarder la config", "Il faut redémarrer le routeur", "Il faut réinitialiser le processus OSPF"],
      "answer": "Il faut réinitialiser le processus OSPF",
      "flashcard": "Le router-id est lu au démarrage du processus OSPF, qui doit être redémarré pour appliquer les changements."
    },
    {
      "question": "Quel état de voisinage existe entre deux routeurs non-DR/BDR ?",
      "options": ["FULL/DR", "2-WAY/DROTHER", "INIT/DROTHER"],
      "answer": "2-WAY/DROTHER",
      "flashcard": "L’état 2-WAY/DROTHER indique un voisinage établi entre deux DROTHER dans OSPF."
    },
    {
      "question": "Quelle commande réinitialise les relations OSPF ?",
      "options": ["restart ospf", "clear ip ospf process", "flush ospf neighbors"],
      "answer": "clear ip ospf process",
      "flashcard": "Cette commande redémarre le processus OSPF et réinitialise les voisins."
    },
    {
      "question": "Dans un réseau OSPF à accès multiple, quel rôle joue le DR ?",
      "options": ["Filtre les paquets", "Centralise les mises à jour OSPF", "Alloue les adresses IP"],
      "answer": "Centralise les mises à jour OSPF",
      "flashcard": "Le DR centralise et réduit le trafic de mise à jour dans un réseau multi-accès."
    },
    {
      "question": "Comment éviter qu’un routeur devienne DR ?",
      "options": ["Définir une priorité OSPF à 0", "Supprimer OSPF", "Désactiver l’interface"],
      "answer": "Définir une priorité OSPF à 0",
      "flashcard": "Une priorité OSPF de 0 empêche le routeur d’être élu DR."
    },
    {
      "question": "Quelle interface sera élue DR si toutes ont priorité égale ?",
      "options": ["Celle avec le coût le plus faible", "Celle avec l'IP la plus haute", "Celle configurée en premier"],
      "answer": "Celle avec l'IP la plus haute",
      "flashcard": "En cas d’égalité de priorité, l’IP la plus haute détermine le DR."
    }
  ],

  "Chapitre 6 : NAT & PAT": [
    {
      "question": "Quel type de NAT permet à plusieurs hôtes d’utiliser une seule IP publique ?",
      "options": ["NAT statique", "NAT dynamique", "PAT"],
      "answer": "PAT",
      "flashcard": "Le PAT utilise une seule IP publique avec différents ports pour plusieurs hôtes."
    },
    {
      "question": "Combien d’adresses publiques peuvent être attribuées en NAT dynamique ?",
      "options": ["1", "Illimité", "Selon le pool configuré"],
      "answer": "Selon le pool configuré",
      "flashcard": "Le NAT dynamique utilise un pool d'adresses publiques configuré par l’administrateur."
    },
    {
      "question": "Combien de ports peuvent être associés à une adresse IP publique en PAT ?",
      "options": ["1", "65000+", "254"],
      "answer": "65000+",
      "flashcard": "PAT peut associer plus de 65 000 ports à une seule IP publique."
    },
    {
      "question": "Quelle commande permet de lier un pool NAT à une ACL ?",
      "options": ["ip nat pool link", "ip nat inside source list 1 pool nom_du_pool", "ip nat dynamic connect"],
      "answer": "ip nat inside source list 1 pool nom_du_pool",
      "flashcard": "Cette commande associe une liste d'accès à un pool NAT pour la translation."
    },
    {
      "question": "Quelle commande affiche les traductions NAT actives ?",
      "options": ["show ip route", "show ip nat translations", "debug nat"],
      "answer": "show ip nat translations",
      "flashcard": "Cette commande liste les traductions NAT en cours sur le routeur."
    },
    {
      "question": "Que signifie l’option 'overload' dans la configuration NAT ?",
      "options": ["Permet d’utiliser plusieurs IP internes", "Autorise la translation de plusieurs connexions vers une seule IP publique", "Désactive NAT dynamique"],
      "answer": "Autorise la translation de plusieurs connexions vers une seule IP publique",
      "flashcard": "L’option 'overload' active le PAT, permettant plusieurs connexions sur une IP publique via différents ports."
    },
    {
      "question": "Quelle commande affiche le nombre de traductions actives NAT ?",
      "options": ["show ip nat statistics", "show ip route", "debug ip nat"],
      "answer": "show ip nat statistics",
      "flashcard": "Cette commande affiche des statistiques sur les traductions NAT, dont le nombre actif."
    },
    {
      "question": "Quelle commande permet de voir les interfaces NAT inside/outside ?",
      "options": ["show ip interface brief", "show ip nat interfaces", "show interfaces nat status"],
      "answer": "show ip nat interfaces",
      "flashcard": "Cette commande affiche quelles interfaces sont configurées comme inside ou outside pour NAT."
    }
  ]
}
