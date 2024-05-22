from pytmx import TiledMap
import pygame

from player import Perso, Pnj
from player import Game_Sprite as GS


# Constants

MAP_WIDTH = 70
MAP_HEIGHT = 50

WINDOW_WIDTH = 64*16
WINDOW_HEIGHT = 64*9

TILE_SIZE = 64

SCALE_FACTOR = 2

SPRITE_HEIGHT = 52
SPRITE_WIDTH = 32

#MAIN DESIGN
main_char = pygame.image.load("main_char.png")

main_wback = main_char.subsurface((0,512,832,64))
main_back_array = [main_wback.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_back_array += [main_wback.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wfront = main_char.subsurface((0,640,832,64))
main_front_array = [main_wfront.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_front_array += [main_wfront.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wleft = main_char.subsurface((0,576,832,64))
main_left_array = [main_wleft.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_left_array += [main_wleft.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wright = main_char.subsurface((0,704,832,64))
main_right_array = [main_wright.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_right_array += [main_wright.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

#LOOKING
main_acc = main_char.subsurface((0,1280,384,64))
main_acc_array = [main_acc.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,5) :
    main_acc_array += [main_acc.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
#PYJAMA
main_char_pyj = pygame.image.load("main_character_pyjama.png")

main_wb_pyj = main_char_pyj.subsurface((0,512,832,64))
main_back_pyj = [main_wb_pyj.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_back_pyj += [main_wb_pyj.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wf_pyj = main_char_pyj.subsurface((0,640,832,64))
main_front_pyj = [main_wf_pyj.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_front_pyj += [main_wf_pyj.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wl_pyj = main_char_pyj.subsurface((0,576,832,64))
main_left_pyj = [main_wl_pyj.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_left_pyj += [main_wl_pyj.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

main_wr_pyj = main_char_pyj.subsurface((0,704,832,64))
main_right_pyj = [main_wr_pyj.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    main_right_pyj += [main_wr_pyj.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

#PNJ
baby = pygame.image.load("BabyBundles.png")
baby_turkish = [baby.subsurface((0,48,SPRITE_WIDTH,32)),baby.subsurface((32,32,SPRITE_WIDTH,32)),baby.subsurface((64,48,SPRITE_WIDTH,32)),
                pygame.transform.flip(baby.subsurface((32,32,SPRITE_WIDTH,32)),True,True),baby.subsurface((32,128,32,32))]
#baby_turkish = [pygame.transform.flip(baby.subsurface((32,32,SPRITE_WIDTH,32)),False,True),baby.subsurface((32,32,SPRITE_WIDTH,32)),baby.subsurface((64,48,SPRITE_WIDTH,32)),pygame.transform.flip(baby.subsurface((32,32,SPRITE_WIDTH,32)),True,False)]

athena = pygame.image.load("athena.png")
athena_vener = [athena.subsurface((16,651,SPRITE_WIDTH,SPRITE_HEIGHT))]

androm = pygame.image.load("andromaque.png")
androm_d = androm.subsurface((0,128,832,64))
androm_dance = [androm_d.subsurface((0,11,SPRITE_HEIGHT,SPRITE_HEIGHT))]
for i in range(1,6) :
    androm_dance += [androm_d.subsurface((64*i,63-SPRITE_HEIGHT,SPRITE_HEIGHT,SPRITE_HEIGHT))]
andro_back = main_char_pyj.subsurface((0,512,832,64))
andro_b = [andro_back.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    andro_b += [andro_back.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

hecu = pygame.image.load("hecube.png")
hecu_d = hecu.subsurface((0,128,832,64))
hecu_dance = [hecu_d.subsurface((0,11,SPRITE_HEIGHT,SPRITE_HEIGHT))]
for i in range(1,6) :
    hecu_dance += [hecu_d.subsurface((64*i,63-SPRITE_HEIGHT,SPRITE_HEIGHT,SPRITE_HEIGHT))]
hecu_back = hecu.subsurface((0,512,832,64))
hecu_b = [hecu_back.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    hecu_b += [hecu_back.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

cass = pygame.image.load("cassandre.png")
cass_d = cass.subsurface((0,128,832,64))
cass_dance = [cass_d.subsurface((0,11,SPRITE_HEIGHT,SPRITE_HEIGHT))]
for i in range(1,6) :
    cass_dance += [cass_d.subsurface((0 + 64*i,63-SPRITE_HEIGHT,SPRITE_HEIGHT,SPRITE_HEIGHT))]
cass_back = cass.subsurface((0,512,832,64))
cass_b = [cass_back.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    cass_b += [cass_back.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

poly = pygame.image.load("polyxene.png")
poly_d = poly.subsurface((0,128,832,64))
poly_dance = [poly_d.subsurface((0,11,SPRITE_HEIGHT,SPRITE_HEIGHT))]
for i in range(1,6) :
    poly_dance += [poly_d.subsurface((64*i,63-SPRITE_HEIGHT,SPRITE_HEIGHT,SPRITE_HEIGHT))]
poly_back = poly.subsurface((0,512,832,64))
poly_b = [poly_back.subsurface((16,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]
for i in range(1,7) :
    poly_b += [poly_back.subsurface((16 + 64*i,63-SPRITE_HEIGHT,SPRITE_WIDTH,SPRITE_HEIGHT))]

troy_horse = pygame.image.load("troy_horse.png")
cheval = troy_horse.subsurface((576,0,256,384))



class Scene:
    def __init__(self, map_filename):
        self.map = Map(MAP_WIDTH, MAP_HEIGHT)
        self.map.load_tmx(map_filename)
        self.player = Perso(GS.me, 4128, 2848,[main_front_array,main_back_array,main_left_array,main_right_array,
                                                main_front_pyj,main_back_pyj,main_left_pyj,main_right_pyj,main_acc_array])
        #self.cassandre = Pnj(GS.pnj,WINDOW_WIDTH//2 + 64,WINDOW_HEIGHT//2 + 64,cass_dance)
        self.filter1 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (0, 0, 0), speed=1)
        self.filter1.enabled = False
        self.troyenne_once = True
        self.boat_once = False
        self.athena_once = False
        self.room_once = False
        self.filter2 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (0, 0, 0), speed=0.01)
        self.filter2.enabled = True
        self.filter2.disable()
        self.filter3 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (175, 30, 30), speed=0.01, max_alpha=50)
        self.filter3.enabled = False

        # For displaying text on the screen
        self.font = pygame.font.Font("AUGUSTUS.ttf", 20)   # credit: Manfred Klein, https://www.dafont.com/fr/augustus.font
        self.text_color = (255, 255, 255)  # White text color
        self.background_color = (139, 69, 19)  # Brown background color
        self.display_text = False
        self.text_to_display = "Error: Text not set!"
        
        self.enable_dialogue = True
        self.dialogue_1 = [
            "Aie, ma tête... ",
            "Mais... Mais où je suis moi?",
            "Ça me revient, l\'assaut de Troie! Mais où sont passés les autres? Où est mon armée troyenne... je veux dire achéenne... Non, troyenne...",
            "Le coup que j'ai reçu devait être plus fort que je ne le pensais, je n'arrive même pas à me souvenir de mon camp.",
            "Je devrais explorer les environs, trouver des indices, ça devrait m'aider à me rafraichir la mémoire."
        ]
        self.dialogue_2 = [
            "Oh un cheval en bois... Mais oui c'est ça le cheval de bois ! Quelle ruse malicieuse ! Il me semble que l'idée venait d'Ulysse et qu'Epeos a dirigé la construction. Mais... Mais... ",
            "Je suis sûr de louper quelque chose..."
        ]
        self.dialogue_2_2 = [
            "... des lances cachées en son sein...",
            "Une ruse malicieuse... Ou bien une trahison écoeurante! Transformer une offrande en arme, quelle immondice.",
            "Tout est si flou, je ne sais plus quoi croire... Il faudrait que je continue de chercher."
        ]
        self.dialogue_3 = [
            "Qu'est-ce que c'est que ça ? Un bébé ? Qu'est-ce qu'un bébé pouvait bien faire là ? "
        ]
        self.dialogue_4 = [
            "Ça me revient. Ulysse nous a prévenu qu'il était dangereux de laisser le fils d'Hector vivre. On pourrait dire que c'était nécessaire.",
            "Mais quand bien même... tuer un bébé, c'est barbare, peu importe qui est son père. Pauvre Andromaque.",
            "Andromaque... qu'est-il arrivé à elle et aux autres? Argh ma tête... Il me semble que le campement était dressé un peu plus loin, je devrais aller y jeter un coup d'oeil."
        ]
        self.dialogue_5 = [
            "Mais attends, c'est ma tente celle-là ? Ou bien celle-ci ? Ou bien ai-je vraiment logé ici ?",
            "Nous sommes les Troyennes, à toi de retrouver quel personnage nous a arraché à notre peuple, et nous fit sienne à titre de \"récompense particulière\".",
            "Polyxène : J'ai péri égorgée sur le tombeau d\'Achille, offerte au mort sans vie.",
            "Andromaque : J'ai assisté à la mise à mort de mon fils, laissant sa dépouille à ma mère, forcée de suivre Néoptolème.",
            "Cassandre : Prétresse d'Apollon et fille de Priam, j'ai tenté de mettre en garde mon peuple, en vain. Souillée par Ajax, enlevée par Agamemnon, je finis par trouver la mort grâce à sa femme, Clytemnestre.",
            "Hécube : Epouse de Priam, j'ai vu ma descendance et mon peuple souffrir et être décimé, abusé sous mes propres yeux.",
        ]
        self.dialogue_6 = [
            "Forcément, les plus grandes tentes appartenaient à nos chefs. Et ils ont du se partager le butin... dont les femmes des troyens.",
            "Essayons de nous souvenir... où ont-elles été emmenées?",
            "Tiens, les cendres ont l'air encore chaudes. Peut-être que je me suis évanoui moins longtemps que je pensais... Mais peut-être qu'ils viennent de partir tous. Il faut que je fonce à la plage, les bateaux sont peut-être encore là."
        ]
        self.dialogue_6_1 = [
            "C'est vrai!",
            "Polyxène-Achille: Un grand héros comme Achille se doit d'être accompagné dans la mort... mais quand même, quelle barbarie."
        ]
        self.dialogue_6_2 = [
            "C'est vrai!",
            "Andromaque-Neoptolème: Son bébé mort, son mari mort... Andromaque a été embarquée par Neoptolème... Je crois qu'il voulait l'épouser."
        ]
        self.dialogue_6_3 = [
            "C'est vrai!",
            "Hécube-Ulysse: Pauvre Hécube, après avoir perdu toute sa famille elle est partie à bord du navire d'Ulysse."
        ]
        self.dialogue_6_4 = [
            "C'est vrai!",
            "Cassandre-Agamemnon: La prêtresse d'Apollon a prononcé une prophetie avant d'être emmenée... un destin funeste à chacun pour le retour outre mer."
        ]
        self.dialogue_7_1 = [
            "Bon je commence à y voir plus clair... Mais ?!? C'est le bateau des Danéens au loin ? Vite, une longue vue..."
        ]
        self.dialogue_7_2 = [
            "Oh mais j'entends des voix ? Une discussion entre les dieux ? Tendons l'oreille...",
            "Athéna : Face à l'affront d'Ajax envers Cassandre dans mon temple, désormais Poséidon je veux, unie à toi, châtier ceux qui ne l'ont ni puni ni blamé.",
            "Athéna frappa d\'un trait de foudre le navire d\'Ajax. [...] Ajax trouva refuge sur un rocher. [...] Poséidon l\'entendit, et d\'un coup de trident fit éclater le rocher. Ajax tomba dans la mer et mourut.",
            "Les naufragés avalent par gorgées l\'eau affreuse à boire de la mer grondante ; puis, rendant l\'âme, ils sont emportés sur l\'onde. Les captives s\'abandonnent à la joie alors même qu\'elles expirent."
        ]
        self.dialogue_7_3 = [
            "Mais oui je vois des navires au loin, sûrement ceux des Danaéens. Vite une longue vue...",
            "Oh mais j'entends des voix ? Une discussion entre les dieux ? Tendons l'oreille...",
            "Athéna : Face à l'affront d'Ajax envers Cassandre dans mon temple, désormais Poséidon je veux, unie à toi, châtier ceux qui ne l'ont ni puni ni blamé.",
            "Athéna frappa d\'un trait de foudre le navire d\'Ajax. [...] Ajax trouva refuge sur un rocher. [...] Poséidon l\'entendit, et d\'un coup de trident fit éclater le rocher. Ajax tomba dans la mer et mourut.",
            "Les naufragés avalent par gorgées l\'eau affreuse à boire de la mer grondante ; puis, rendant l\'âme, ils sont emportés sur l\'onde. Les captives s\'abandonnent à la joie alors même qu\'elles expirent."
        ]
        self.dialogue_8_choix = [
            "Qui sont les véritables vainqueurs de la guerre de Troie?"
        ]   
        self.dialogue_9 = [
            "Et c'est à travers les textes de Virgile, Homère ou bien Euripide et de leur diversité d'approche des moment clé de cette guerre que nous avons pu nous rendre compte comment des textes relatant un même conflit peuvent-être utilisés à des fin diverses",
        ]
        self.dialogue_10 = [
            "Quel rêve étrange… Cette présentation de SHS m\'a vraiment bouleversé l\'esprit !  En tout cas, moi je pense que j'aurais été du côté des vainqueurs. ",
            "Merci d'avoir participé ! ",
            "CREDITS:",
            "Assets: ",
            "LPC compatible Ancient Greek Architecture, par Wolthera van Hövell tot Westerflier [Creative Commons Attribution v4.0 International]",
            "LPC Tile Atlas, par Casper Nilsson, Daniel Eddeland, Johann CHARLOT, Lanea Zimmerman [CC-BY-SA 3.0, GNU GPL 3.0]",
            "LPC Submissions Merged, par DeadlyEssence01 [CC-BY-SA 3.0, GPL 3.0, GPL 2.0]",
            "[LPC] Signposts, graves, line cloths and scare crow, par Reemax [CC-BY-SA]",
            "LPC Babies, Death's Darling [CC-BY-SA 3.0]",
            "Générateur de personnage LPC: ",
            "Universal LPC Spritesheet Generator, par bluecarrot16, Benjamin K. Smith (BenCreating), Evert, Eliza Wyatt (ElizaWy), TheraHedwig, MuffinElZangano, Durrani, Johannes Sj?lund (wulax), Stephen Challener (Redshrike) [Creative Commons Attribution-ShareAlike 3.0]",
            "Musiques: ",
            "Le maître de l'olympe OST par Impression Games",
            "Ready pixel one par Pix [CC0]",  
            "Searching for a body par Pix [CC0]",
            "Rape me de Nirvana (8-bit cover par Нік Чема  Nick Chema Music)",
            "Merci à ",
            "Euripide",
            "Virgile",  
            "Quintus de Smyrne",
            "Eschyle",
            "Homère",
            "Pseudo-Apollodore",
            "Pour le script"
        ]
        self.current_dialogue = self.dialogue_1
        self.current_text_number = 0


        self.option_select = OptionsSelectTroyennes("Qui faut-il donner à Achille ?")
        self.troyennes_minigame = False
        self.minigame_progress = 0

        self.update_scene = False

        self.lauch_baby = False

        self.show_png = False
        self.boat_scene = False
        self.chambre_scene = False
        self.png_x = -800
        self.png_y = -400
        self.png_boat = pygame.image.load("boat.png")
        png_chambre_unscaled = pygame.image.load("chambre.png")

        # Scale the image
        original_width, original_height = png_chambre_unscaled.get_size()
        scaled_width = int(original_width * WINDOW_WIDTH/original_width)
        scaled_height = int(original_height * WINDOW_HEIGHT*2/3/original_height)
        self.png_chambre = pygame.transform.scale(png_chambre_unscaled, (scaled_width, scaled_height))
        self.current_png = self.png_boat

        #self.current_dialogue = self.dialogue_7_1
        #self.player.x = 1000
        #self.player.y = 1000

        self.fill_screen_black = False

    def check_update_scene(self):
        new_scene = self
#        print(self.current_text_number)

        if self.boat_scene and self.png_y > -750:
            self.png_y -= 3
        elif self.boat_scene :
            if not self.boat_once :
                self.cassandre = Pnj(GS.pnj,560,150,cass_dance)
                self.hecube = Pnj(GS.pnj,470,150,hecu_dance)
                self.polyxene = Pnj(GS.pnj,560,250,poly_dance)
                self.andromaque = Pnj(GS.pnj,470,250,androm_dance)
                self.boat_once = True
            if not self.athena_once and self.current_text_number == 1:
                self.athena = Pnj(GS.pnj,WINDOW_WIDTH - 64,WINDOW_HEIGHT -192,athena_vener)
                self.athena_once = True
            self.cassandre.dance()
            self.hecube.dance()
            self.polyxene.dance()
            self.andromaque.dance()
        if self.current_dialogue == self.dialogue_1 and self.player.x < 3231 and self.player.y < 2125:
            self.current_dialogue = self.dialogue_2
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_2 and self.player.x < 2940 and self.player.y < 1675 and self.player.x > 2800 and self.player.y > 1500:
            self.current_dialogue = self.dialogue_2_2
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_2_2 and self.player.x < 2000 and self.player.y < 923 and self.player.x > 1600 and self.player.y > 700:
            self.current_dialogue = self.dialogue_3
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_3 and self.lauch_baby == True:
            self.lauch_baby = False
            self.update_scene = True
            self.player.kill()
            new_scene = BabyScene("map_destroyed_sans_bebe.tmx")
            self.current_dialogue = self.dialogue_4
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_4 and self.player.x < 1712 and self.player.y > 2062:
            self.player.x = 1000
            self.player.y = 2700
            self.current_dialogue = self.dialogue_5
            self.current_text_number = 0
            self.enable_dialogue = True
            self.troyennes_minigame = True
            self.filter2.enabled = True
            self.filter2.disable()
        elif self.current_dialogue == self.dialogue_5 :
            if self.current_text_number == 1 and self.troyenne_once:
                self.troyenne_once = False
                self.cassandre = Pnj(GS.pnj,560,150,cass_dance)
                self.hecube = Pnj(GS.pnj,480,150,hecu_dance)
                self.polyxene = Pnj(GS.pnj,400,150,poly_dance)
                self.andromaque = Pnj(GS.pnj,320,150,androm_dance)
            if self.current_text_number >= 1 :    
                self.cassandre.dance()
                self.hecube.dance()
                self.polyxene.dance()
                self.andromaque.dance()
            if self.current_text_number >= 5:
                self.cassandre.kill()
                self.hecube.kill()
                self.polyxene.kill()
                self.andromaque.kill()
        elif self.troyennes_minigame == True and self.minigame_progress >= 4 and self.enable_dialogue == False:
            self.troyennes_minigame = False
            self.option_select.enabled = False
            self.current_dialogue = self.dialogue_6
            self.current_text_number = 0
            self.enable_dialogue = True
            self.filter2.enabled = True
            self.filter2.disable()
        elif self.current_dialogue == self.dialogue_6 and self.player.y < 700 and self.current_dialogue != self.dialogue_7_1:
            self.troyennes_minigame = False
            self.option_select.enabled = False
            self.current_dialogue = self.dialogue_7_1
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_7_1 and self.player.y < 500:
            self.show_png = True
            self.boat_scene = True
            self.player.kill()
            self.current_dialogue = self.dialogue_7_2
            self.current_text_number = 0
            self.enable_dialogue = True
            self.filter3.enabled = True
            #self.filter3.enable()
        elif self.current_dialogue == self.dialogue_7_2 and self.current_text_number == 3:
            self.fill_screen_black = True
            self.show_png = False
            self.boat_scene = False
            self.chambre_scene = False
            self.enable_dialogue = False
            self.option_select = OptionsSelectEnd(self.dialogue_8_choix[0])
            self.option_select.enabled = True
            self.current_text_number = 0
            #self.filter3.disable()
            self.enable_dialogue = False
        elif self.current_dialogue == self.dialogue_7_2 and self.option_select.text_to_display == self.dialogue_8_choix[0] and self.option_select.enabled == False:
            self.current_dialogue = self.dialogue_9
            self.current_text_number = 0
            self.enable_dialogue = True
        elif self.current_dialogue == self.dialogue_9 and self.current_text_number == 1:
            self.fill_screen_black = False
            self.show_png = True
            self.boat_scene = False
            self.png_x = 0
            self.png_y = 0
            self.chambre_scene = True
            self.current_dialogue = self.dialogue_10
            self.current_text_number = 0
            self.enable_dialogue = True
        return new_scene

    
    def handle_input(self):
        self.filter1.update_animation()
        self.filter2.update_animation()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            if not self.display_text and not self.enable_dialogue and not self.option_select.enabled:
                self.player.move_up(self.map.tiles)
        if keys[pygame.K_DOWN]:
            if not self.display_text and not self.enable_dialogue and not self.option_select.enabled:
                self.player.move_down(self.map.tiles)
        if keys[pygame.K_LEFT]:
            if not self.display_text and not self.enable_dialogue and not self.option_select.enabled:
                self.player.move_left(self.map.tiles)
        if keys[pygame.K_RIGHT]:
            if not self.display_text and not self.enable_dialogue and not self.option_select.enabled:
                self.player.move_right(self.map.tiles)
        if keys[pygame.K_SPACE]:
            for tile in self.map.interactable_tiles:
                if (self.player.x - self.player.x_size//2 > tile.x*TILE_SIZE - self.player.x_size - self.player.sign_sensitivity and self.player.x - self.player.x_size//2 < tile.x*TILE_SIZE + TILE_SIZE + self.player.sign_sensitivity and self.player.y - self.player.y_size//2 > tile.y*TILE_SIZE - self.player.y_size - self.player.sign_sensitivity and self.player.y - self.player.y_size//2 < tile.y*TILE_SIZE + TILE_SIZE + self.player.sign_sensitivity):
                    interact_type, interact_data = tile.interact()
                    if interact_type == "sign":
                        self.filter1.enable()
                        self.display_text = True
                        self.text_to_display = interact_data
        if keys[pygame.K_ESCAPE]:
            self.display_text = False
            self.filter1.disable()

#        if keys[pygame.K_c]:
#            self.player.pyj = not self.player.pyj
#            self.cassandre.move(64,64)

        self.positions = [(325, 2458), (329, 3034), (1416, 2458), (1414, 3034)]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
#                    print(self.minigame_progress)
                    if self.option_select.enabled:
                        if self.option_select.current_option == 0:
                            if not self.troyennes_minigame:
                                self.option_select.enabled = False
                            elif self.player.x < 500 and self.player.x > 250 and self.player.y < 2500 and self.player.y > 2400:
                                self.option_select.enabled = False
                                self.current_dialogue = self.dialogue_6_1
                                self.polyxene = Pnj(GS.pnj,300,500,poly_b)
                                
                                self.minigame_progress += 1
                                self.current_text_number = 0
                                self.enable_dialogue = True
                        elif self.option_select.current_option == 1:
                            if not self.troyennes_minigame:
                                self.option_select.enabled = False
                            elif self.player.x < 500 and self.player.x > 250 and self.player.y < 3150 and self.player.y > 2950:
                                self.option_select.enabled = False
                                self.current_dialogue = self.dialogue_6_2
                                self.andromaque = Pnj(GS.pnj,300,500,andro_b)
                                self.minigame_progress += 1
                                self.current_text_number = 0
                                self.enable_dialogue = True
                        elif self.option_select.current_option == 2:
                            if self.player.x < 1550 and self.player.x > 1250 and self.player.y < 2500 and self.player.y > 2400:
                                self.option_select.enabled = False
                                self.current_dialogue = self.dialogue_6_4
                                self.cassandre = Pnj(GS.pnj,550,500,cass_b)
                                self.minigame_progress += 1
                                self.current_text_number = 0
                                self.enable_dialogue = True
                        elif self.option_select.current_option == 3:
                            if self.player.x < 1550 and self.player.x > 1250 and self.player.y < 3150 and self.player.y > 2950:
                                self.option_select.enabled = False
                                self.current_dialogue = self.dialogue_6_3
                                self.hecube = Pnj(GS.pnj,550,500,hecu_b)
                                self.minigame_progress += 1
                                self.current_text_number = 0
                                self.enable_dialogue = True 
                    elif not self.option_select.enabled and self.troyennes_minigame and self.player.x < 450 and self.player.x > 300 and self.player.y < 2500 and self.player.y > 2400:
                        self.option_select.text_to_display = "Qui faut-il donner à Achille ?"
                        self.option_select.enabled = True
                    elif not self.option_select.enabled and self.troyennes_minigame and self.player.x < 450 and self.player.x > 300 and self.player.y < 3150 and self.player.y > 2950:
                        self.option_select.text_to_display = "Qui faut-il donner à Neoptolème ?"
                        self.option_select.enabled = True
                    elif not self.option_select.enabled and self.troyennes_minigame and self.player.x < 1500 and self.player.x > 1300 and self.player.y < 2500 and self.player.y > 2400:
                        self.option_select.text_to_display = "Qui faut-il donner à Agamemnon ?"
                        self.option_select.enabled = True
                    elif not self.option_select.enabled and self.troyennes_minigame and self.player.x < 1500 and self.player.x > 1300 and self.player.y < 3150 and self.player.y > 2950:
                        self.option_select.text_to_display = "Qui faut-il donner à Ulysse ?"
                        self.option_select.enabled = True
                    


                
                if event.key == pygame.K_k:
                    if self.enable_dialogue == False:
                        self.current_dialogue = self.dialogue_2
                        self.enable_dialogue = True
                    elif self.enable_dialogue == True:
                        self.enable_dialogue = False
                        self.current_text_number = 0
                
                if event.key == pygame.K_l:
                    if self.option_select.enabled and not self.enable_dialogue:
                        self.option_select.enabled = False
                    elif not self.enable_dialogue:
                        self.option_select.enabled = True

                if event.key == pygame.K_RIGHT:
                    if self.enable_dialogue and self.current_dialogue == self.dialogue_9:
                        self.current_text_number += 1
                    elif self.enable_dialogue and self.current_text_number < len(self.current_dialogue) - 1 :
                        if self.current_dialogue == self.dialogue_6_1 or self.current_dialogue == self.dialogue_6_2 or self.current_dialogue == self.dialogue_6_3 or self.current_dialogue == self.dialogue_6_4 :
                            if not self.hecube.update_pos() and not self.polyxene.update_pos() and not self.andromaque.update_pos() and not self.cassandre.update_pos():
                                self.current_text_number += 1
                        else :
                            self.current_text_number += 1
                    elif self.option_select.enabled:
                        self.option_select.current_option = (self.option_select.current_option + 1) % 4
                    else:
                        if self.current_dialogue == self.dialogue_3:
                            self.lauch_baby = True
                        self.enable_dialogue = False
                if event.key == pygame.K_LEFT:
                    if self.option_select.enabled:
                        self.option_select.current_option = (self.option_select.current_option - 1) % 4
        return True
    
    def render(self, window):
#        print(self.player.x,self.player.y)
        self.map.render(window, (self.player.x - WINDOW_WIDTH//2, self.player.y - WINDOW_HEIGHT//2))
        self.player.render(window)
        if self.boat_scene and self.show_png:
            window.blit(self.png_boat, (self.png_x, self.png_y))
        elif self.chambre_scene and self.show_png:
            window.blit(self.png_boat, (self.png_x, self.png_y))
            window.blit(self.png_chambre, (self.png_x, self.png_y-20))
        GS.me.update()
        GS.pnj.update()
        GS.pnj.draw(window)
        GS.me.draw(window)

            
        if not self.filter2.enabled:
            self.filter1.apply(window)
        if not self.filter1.enabled:
            self.filter2.apply(window)
        if self.filter3.enabled:
            self.filter3.apply(window)
        if self.fill_screen_black:
            window.fill((0, 0, 0))
        if self.display_text:
            self.show_text(window, self.text_to_display)
        elif self.enable_dialogue:
            self.show_dialogue(window)
        elif self.option_select.enabled:
            self.option_select.render(window)
        

    def show_text(self, window, text):
        # Create a rectangle for the background
        text_surface = self.font.render(text, True, self.text_color)
        text_rect = text_surface.get_rect(center=(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2))
        
        background_rect = pygame.Rect(0, 0, text_rect.width + 20, text_rect.height + 20)  # Adjust size as needed
        background_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        # Draw shadow-like effect
        shadow_offset = 3
        shadow_rect = background_rect.move(shadow_offset, shadow_offset)
        pygame.draw.rect(window, (0, 0, 0), shadow_rect)

        # Draw background rectangle
        pygame.draw.rect(window, self.background_color, background_rect)

        # Render text
        text_rect.center = background_rect.center
        window.blit(text_surface, text_rect)

    def show_dialogue(self, window):
#Baby crouch
        if (self.current_text_number == 0 and  self.current_dialogue == self.dialogue_3) or self.player.image == self.player.images[8][0] or self.player.image == self.player.images[8][1] or self.player.image == self.player.images[8][2]:
            self.player.anim_crouch()
#Third head movement
        if (self.current_text_number == 0 and  self.current_dialogue == self.dialogue_2_2) :
            self.player.anim_crouch()
        if self.current_text_number < len(self.current_dialogue):
            text = [self.current_dialogue[self.current_text_number]]

        else:
            text = []
#First head movement       
        if (self.current_text_number == 1 and  self.current_dialogue == self.dialogue_1) :
            self.player.image = self.player.images[2][0]
        if (self.current_text_number == 2 and  self.current_dialogue == self.dialogue_1) :
            self.player.image = self.player.images[3][0]
        if (self.current_text_number == 3 and  self.current_dialogue == self.dialogue_1) :
            self.player.image = self.player.images[0][0]
#Second head movement       
        if (self.current_text_number == 0 and  self.current_dialogue == self.dialogue_2) :
            self.player.image = self.player.images[2][0]
        if (self.current_text_number == 1 and  self.current_dialogue == self.dialogue_2) :
            self.player.image = self.player.images[3][0]
#poly move
        if (self.current_dialogue == self.dialogue_6_1):
            self.polyxene.move(300,200)
            if not self.polyxene.update_pos() :
                self.polyxene.kill()
        if (self.current_dialogue == self.dialogue_6_2):
            self.andromaque.move(300,250)
            if not self.andromaque.update_pos() :
                self.andromaque.kill()
        if (self.current_dialogue == self.dialogue_6_3):
            self.hecube.move(550,250)
            if not self.hecube.update_pos() :
                self.hecube.kill()
        if (self.current_dialogue == self.dialogue_6_4):
            self.cassandre.move(550,200)
            if not self.cassandre.update_pos() :
                self.cassandre.kill()
        if self.current_dialogue == self.dialogue_9 and not self.room_once:
            self.athena.kill()
            self.cassandre.kill()
            self.hecube.kill()
            self.polyxene.kill()
            self.andromaque.kill()
            self.room_once = True
            self.player = Perso(GS.me,WINDOW_WIDTH//2,WINDOW_HEIGHT//2,[main_front_array,main_back_array,main_left_array,main_right_array,
                                                main_front_pyj,main_back_pyj,main_left_pyj,main_right_pyj,main_acc_array])    
            self.player.image = self.player.images[4][self.player.animation]
            self.player.pyj = True
        margin_bottom = 32
        box_height = WINDOW_HEIGHT // 3
        border_size = 8
        shadow_offset = 2
        dark_brown = (79, 45, 0)
        shadow_color = (10, 10, 10)  # Black for the shadow
        arrow_color = self.text_color

        # Calculate the y-coordinate of the top of the dialogue box
        box_top = WINDOW_HEIGHT - box_height - margin_bottom

        # Create a rectangle for the dialogue box
        box_width = WINDOW_WIDTH - 192
        box_rect = pygame.Rect(0, 0, box_width, box_height)
        box_rect.center = (WINDOW_WIDTH // 2, box_top + box_height // 2)

        # Create the dialogue box surface with shadow
        box_surface = pygame.Surface((box_width, box_height))
        box_surface.fill(self.background_color)
        box_surface_shadow = pygame.Surface((box_width, box_height))
        box_surface_shadow.fill(shadow_color)

        # Draw the shadow
        window.blit(box_surface_shadow, (box_rect.x + shadow_offset, box_rect.y + shadow_offset))
        # Draw the border
        pygame.draw.rect(window, dark_brown, (box_rect.x - border_size, box_rect.y - border_size, box_width + 2 * border_size, box_height + 2 * border_size))
        # Draw the dialogue box
        window.blit(box_surface, box_rect)

        # Calculate the maximum width for text wrapping
        max_text_width = box_width - 20  # Adding some padding

        # Split text into lines that fit within the max_text_width
        wrapped_lines = []
        for sentence in text:
            words = sentence.split(' ')
            line = ""
            for word in words:
                test_line = line + word + " "
                if self.font.size(test_line)[0] > max_text_width:
                    wrapped_lines.append(line)
                    line = word + " "
                else:
                    line = test_line
            wrapped_lines.append(line)

        # Calculate the height of each line of text
        line_height = self.font.get_linesize()
        total_text_height = line_height * len(wrapped_lines)

        # Calculate the starting y-coordinate of the text
        text_y = box_rect.top + (box_height - total_text_height) // 2

        # Render and display each line of text with shadow
        for line in wrapped_lines:
            text_surface = self.font.render(line, True, self.text_color)
            text_surface_shadow = self.font.render(line, True, shadow_color)

            # Calculate the x-coordinate of the text
            text_x = box_rect.left + (box_width - text_surface.get_width()) // 2

            # Display the shadow and the text
            window.blit(text_surface_shadow, (text_x + shadow_offset, text_y + shadow_offset))
            window.blit(text_surface, (text_x, text_y))
            text_y += line_height

        arrow_size = 20  # Size of the arrow
        arrow_x = box_rect.right - arrow_size - 10
        arrow_y = box_rect.bottom - arrow_size - 10

        arrow_points = [
            (arrow_x, arrow_y),
            (arrow_x + arrow_size, arrow_y + arrow_size // 2),
            (arrow_x, arrow_y + arrow_size)
        ]

        pygame.draw.polygon(window, arrow_color, arrow_points)   

class OptionsSelectEnd:
    def __init__(self, text):
        self.font = pygame.font.Font("AUGUSTUS.ttf", 20)   # credit: Manfred Klein, https://www.dafont.com/fr/augustus.font
        self.text_color = (255, 255, 255)  # White text color
        self.background_color = (139, 69, 19)  # Brown background color
        self.dark_brown = (79, 45, 0)
        self.enabled = False
        self.text_to_display = text
        self.option1 = "Les Achéens"
        self.option2 = "Les Troyens"
        self.current_option = 0

    def render(self, window):
        margin_bottom = 32
        box_height = WINDOW_HEIGHT // 3
        border_size = 8
        shadow_offset = 2
        shadow_color = (0, 0, 0)  # Black for the shadow

        # Calculate the y-coordinate of the top of the dialogue box
        box_top = WINDOW_HEIGHT - box_height - margin_bottom

        # Create a rectangle for the dialogue box
        box_width = WINDOW_WIDTH - 192
        box_rect = pygame.Rect(0, 0, box_width, box_height)
        box_rect.center = (WINDOW_WIDTH // 2, box_top + box_height // 2)

        # Create the dialogue box surface with shadow
        box_surface = pygame.Surface((box_width, box_height))
        box_surface.fill(self.background_color)
        box_surface_shadow = pygame.Surface((box_width, box_height))
        box_surface_shadow.fill(shadow_color)

        # Draw the shadow
        window.blit(box_surface_shadow, (box_rect.x + shadow_offset, box_rect.y + shadow_offset))
        # Draw the border
        pygame.draw.rect(window, self.dark_brown, (box_rect.x - border_size, box_rect.y - border_size, box_width + 2 * border_size, box_height + 2 * border_size))
        # Draw the dialogue box
        window.blit(box_surface, box_rect)

        # Render and display the text
        text_surface = self.font.render(self.text_to_display, True, self.text_color)
        text_surface_shadow = self.font.render(self.text_to_display, True, shadow_color)
        
        # Calculate the text position
        text_x = box_rect.left + (box_width - text_surface.get_width()) // 2
        text_y = box_rect.top + 40  # Padding from the top

        # Display the shadow and the text
        window.blit(text_surface_shadow, (text_x + shadow_offset, text_y + shadow_offset))
        window.blit(text_surface, (text_x, text_y))

        # Render the options
        option1_surface = self.font.render(self.option1, True, self.text_color)
        option2_surface = self.font.render(self.option2, True, self.text_color)
        option1_surface_shadow = self.font.render(self.option1, True, shadow_color)
        option2_surface_shadow = self.font.render(self.option2, True, shadow_color)

        # Calculate the options positions
        options_y = text_y + text_surface.get_height() + 40  # Padding below the text
        option1_x = box_rect.left + box_width // 3 - option1_surface.get_width() // 2
        option2_x = box_rect.left + 2 * box_width // 3 - option2_surface.get_width() // 2

        # Display the shadow and the options
        window.blit(option1_surface_shadow, (option1_x + shadow_offset, options_y + shadow_offset))
        window.blit(option1_surface, (option1_x, options_y))
        window.blit(option2_surface_shadow, (option2_x + shadow_offset, options_y + shadow_offset))
        window.blit(option2_surface, (option2_x, options_y))

        # Draw rectangle around the current selected option
        if self.current_option == 0:
            pygame.draw.rect(window, (255, 255, 255), (option1_x - 5, options_y - 5, option1_surface.get_width() + 10, option1_surface.get_height() + 10), 4)
        elif self.current_option == 1:
            pygame.draw.rect(window, (255, 255, 255), (option2_x - 5, options_y - 5, option2_surface.get_width() + 10, option2_surface.get_height() + 10), 4)

        
class BabyScene(Scene):
    def __init__(self, map_filename):
        super().__init__(map_filename)
        self.player = Perso(GS.me, 1880, 782,[main_front_array,main_back_array,main_left_array,main_right_array,main_front_pyj,main_back_pyj,main_left_pyj,main_right_pyj])
        self.baby = Pnj(GS.pnj,470, 275, baby_turkish)
        self.player.image = self.player.images[2][0]
        self.lunch_bb_scene = False
        self.lunch_bb = False
        self.start = 0
        self.count = 0
        self.end_bb_scene = False
        self.filter2 = Filter((WINDOW_WIDTH, WINDOW_HEIGHT), (0, 0, 0), speed=0.01)
        self.filter2.enabled = True
        self.filter2.disable()

        self.dialogue_10 = [
            "Cliquez sur la barre d'espace aussi souvent que possible pour lancer le bébé !"
        ]

        self.current_dialogue = self.dialogue_10
        self.enable_dialogue = True
        self.current_text_number = 0

        self.font = pygame.font.Font("AUGUSTUS.ttf", 20)   # credit: Manfred Klein, https://www.dafont.com/fr/augustus.font
        self.text_color = (255, 255, 255)  # White text color
        self.background_color = (139, 69, 19)  # Brown background color
        self.display_text = False
        self.text_to_display = "Error: Text not set!"

    def render(self, window):
        self.map.render(window, (self.player.x - WINDOW_WIDTH//2, self.player.y - WINDOW_HEIGHT//2))
        self.player.render(window)
        #self.count_click()
        if not self.baby.update_pos() and self.lunch_bb == True :
            self.end_bb_scene = True
            self.baby.image = self.baby.images[4]
        GS.me.update()
        GS.pnj.update()
        GS.pnj.draw(window)
        GS.me.draw(window)
        if self.enable_dialogue:
            self.show_dialogue(window)

    def handle_input(self):
        if self.end_bb_scene :
            return True
        keys = pygame.key.get_pressed()

        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYUP and self.lunch_bb_scene == False:
                if event.key == pygame.K_RIGHT:
                    if self.enable_dialogue:
                        self.enable_dialogue = False
                        self.current_text_number = 0
                elif event.key == pygame.K_SPACE :
                    self.start = pygame.time.get_ticks()
                    self.lunch_bb_scene = True
            elif event.type == pygame.KEYUP and self.lunch_bb_scene == True:
                if event.key == pygame.K_SPACE :
                    self.count += 1
                    
        if self.lunch_bb_scene:
            if pygame.time.get_ticks() - self.start >= 10000 and self.lunch_bb == False:
                self.lunch_bb = True
                self.baby.move(self.baby.x - self.count*10,285)  
            if self.lunch_bb :                
                self.baby.rot()

        return True

    
    
    def check_update_scene(self):
        new_scene = self
        if (self.end_bb_scene) :
            keys = pygame.key.get_pressed()  
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN and (event.key == pygame.K_UP or event.key == pygame.K_DOWN or event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT) :
                    self.baby.kill()
                    new_scene = Scene("map_final_final_sans_bebe.tmx")
                    new_scene.player.x = 1830
                    new_scene.player.y = 782
                    new_scene.current_dialogue = new_scene.dialogue_4
                    new_scene.enable_dialogue = True
                    self.player.kill()
        return new_scene
    
    def show_dialogue(self, window):

        if self.current_text_number < len(self.current_dialogue):
            text = [self.current_dialogue[self.current_text_number]]

        else:
            text = []

        margin_bottom = 32
        box_height = WINDOW_HEIGHT // 3
        border_size = 8
        shadow_offset = 2
        dark_brown = (79, 45, 0)
        shadow_color = (10, 10, 10)  # Black for the shadow
        arrow_color = self.text_color

        # Calculate the y-coordinate of the top of the dialogue box
        box_top = WINDOW_HEIGHT - box_height - margin_bottom

        # Create a rectangle for the dialogue box
        box_width = WINDOW_WIDTH - 192
        box_rect = pygame.Rect(0, 0, box_width, box_height)
        box_rect.center = (WINDOW_WIDTH // 2, box_top + box_height // 2)

        # Create the dialogue box surface with shadow
        box_surface = pygame.Surface((box_width, box_height))
        box_surface.fill(self.background_color)
        box_surface_shadow = pygame.Surface((box_width, box_height))
        box_surface_shadow.fill(shadow_color)

        # Draw the shadow
        window.blit(box_surface_shadow, (box_rect.x + shadow_offset, box_rect.y + shadow_offset))
        # Draw the border
        pygame.draw.rect(window, dark_brown, (box_rect.x - border_size, box_rect.y - border_size, box_width + 2 * border_size, box_height + 2 * border_size))
        # Draw the dialogue box
        window.blit(box_surface, box_rect)

        # Calculate the maximum width for text wrapping
        max_text_width = box_width - 20  # Adding some padding

        # Split text into lines that fit within the max_text_width
        wrapped_lines = []
        for sentence in text:
            words = sentence.split(' ')
            line = ""
            for word in words:
                test_line = line + word + " "
                if self.font.size(test_line)[0] > max_text_width:
                    wrapped_lines.append(line)
                    line = word + " "
                else:
                    line = test_line
            wrapped_lines.append(line)

        # Calculate the height of each line of text
        line_height = self.font.get_linesize()
        total_text_height = line_height * len(wrapped_lines)

        # Calculate the starting y-coordinate of the text
        text_y = box_rect.top + (box_height - total_text_height) // 2

        # Render and display each line of text with shadow
        for line in wrapped_lines:
            text_surface = self.font.render(line, True, self.text_color)
            text_surface_shadow = self.font.render(line, True, shadow_color)

            # Calculate the x-coordinate of the text
            text_x = box_rect.left + (box_width - text_surface.get_width()) // 2

            # Display the shadow and the text
            window.blit(text_surface_shadow, (text_x + shadow_offset, text_y + shadow_offset))
            window.blit(text_surface, (text_x, text_y))
            text_y += line_height

        arrow_size = 20  # Size of the arrow
        arrow_x = box_rect.right - arrow_size - 10
        arrow_y = box_rect.bottom - arrow_size - 10

        arrow_points = [
            (arrow_x, arrow_y),
            (arrow_x + arrow_size, arrow_y + arrow_size // 2),
            (arrow_x, arrow_y + arrow_size)
        ]

        pygame.draw.polygon(window, arrow_color, arrow_points)   



class OptionsSelectTroyennes:
    def __init__(self, text):
        self.font = pygame.font.Font("AUGUSTUS.ttf", 20)  # credit: Manfred Klein, https://www.dafont.com/fr/augustus.font
        self.text_color = (255, 255, 255)  # White text color
        self.background_color = (139, 69, 19)  # Brown background color
        self.dark_brown = (79, 45, 0)
        self.enabled = False
        self.text_to_display = text
        self.options = ["Polyxène", "Andromaque", "Cassandre", "Hécube"]
        self.current_option = 0
        self.option_size_y = 70
        self.option_size_x = 210

    def render(self, window):
        margin_bottom = 32
        box_height = WINDOW_HEIGHT // 3
        border_size = 8
        shadow_offset = 2
        shadow_color = (0, 0, 0)  # Black for the shadow
        margin_between_box = 30

        # Calculate the y-coordinate of the top of the dialogue box
        box_top = WINDOW_HEIGHT - box_height - margin_bottom

        # Create a rectangle for the dialogue box
        box_width = WINDOW_WIDTH - 32
        box_rect = pygame.Rect(0, 0, box_width, box_height)
        box_rect.center = (WINDOW_WIDTH // 2, box_top + box_height // 2)

        # Create the dialogue box surface with shadow
        box_surface = pygame.Surface((box_width, box_height))
        box_surface.fill(self.background_color)
        box_surface_shadow = pygame.Surface((box_width, box_height))
        box_surface_shadow.fill(shadow_color)

        # Draw the shadow
        window.blit(box_surface_shadow, (box_rect.x + shadow_offset, box_rect.y + shadow_offset))
        # Draw the border
        pygame.draw.rect(window, self.dark_brown, (box_rect.x - border_size, box_rect.y - border_size, box_width + 2 * border_size, box_height + 2 * border_size))
        # Draw the dialogue box
        window.blit(box_surface, box_rect)

        # Render and display the text
        text_surface = self.font.render(self.text_to_display, True, self.text_color)
        text_surface_shadow = self.font.render(self.text_to_display, True, shadow_color)
        
        # Calculate the text position
        text_x = box_rect.left + (box_width - text_surface.get_width()) // 2
        text_y = box_rect.top + 20  # Padding from the top

        # Display the shadow and the text
        window.blit(text_surface_shadow, (text_x + shadow_offset, text_y + shadow_offset))
        window.blit(text_surface, (text_x, text_y))

        # Calculate the position of the options
        options_y = text_y + text_surface.get_height() + 40  # Padding below the text
        options_x_start = box_rect.left + (box_width - (4 * self.option_size_x + 3 * margin_between_box)) // 2  # Centering options horizontally with padding

        # Render the options and draw them
        for i, option in enumerate(self.options):
            option_surface = self.font.render(option, True, self.text_color)
            option_surface_shadow = self.font.render(option, True, shadow_color)

            option_x = options_x_start + i * (self.option_size_x + margin_between_box)  # Spacing options evenly
            option_y = options_y

            # Draw the square for the option
            pygame.draw.rect(window, self.background_color, (option_x - 5, option_y - 5, self.option_size_x, self.option_size_y))
            # Highlight the current selected option
            if self.current_option == i:
                pygame.draw.rect(window, (255, 255, 255), (option_x - 5, option_y - 5, self.option_size_x, self.option_size_y), 4)

            # Calculate the position to center the text within the option box
            text_x_centered = option_x + (self.option_size_x - option_surface.get_width()) // 2
            text_y_centered = option_y + (self.option_size_y - option_surface.get_height()) // 2

            # Draw the option shadow
            window.blit(option_surface_shadow, (text_x_centered + shadow_offset, text_y_centered + shadow_offset))
            # Draw the option
            window.blit(option_surface, (text_x_centered, text_y_centered))
    
    

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[None for _ in range(width)] for _ in range(height)]
        self.interactable_tiles = []

    def load_tmx(self, filename):

        tmxdata = TiledMap(filename)

        tile_properties_cache = {}
        image_path, _, _ = tmxdata.get_tile_image(0, 0, 0)
        image = pygame.image.load(image_path)

        for x in range(tmxdata.width):  
            for y in range(tmxdata.height):
                gid = tmxdata.get_tile_gid(x, y, 0)

                if gid not in tile_properties_cache:
                    tile_properties_cache[gid] = tmxdata.get_tile_properties_by_gid(gid)
                

                _, tile_sizes, _ = tmxdata.get_tile_image(x, y, 0)

                properties = tile_properties_cache[gid]
                im = (image, tile_sizes, "")

                tile_type = properties["type"]
                if tile_type == "Sign":
                    self.tiles[y][x] = Sign(x, y, im, "Hello I am a sign!")
                    self.interactable_tiles.append(self.tiles[y][x])
                elif tile_type == "wall":
                    self.tiles[y][x] = Wall(x, y, im)
                else:
                    self.tiles[y][x] = Floor(x, y, im)
        

    def render(self, window, offset=(0, 0)):
        for row in self.tiles:
            for tile in row:
                if tile is not None:
                    tile.render(window, offset)

class Filter:
    def __init__(self, window_size, color, speed=0.05, constant_alpha=-1, max_alpha=255):
        self.window_size = window_size
        self.color = color
        self.constant_alpha = constant_alpha
        self.speed = speed
        self.enabled = False
        self.animation_progress = 1
        self.direction = "in"
        self.animating = False
        self.max_alpha = max_alpha

    def apply(self, window):
        if self.enabled or self.is_animating():
            # Create a grayscale surface of the same size as the window
            gray_surface = pygame.Surface(self.window_size).convert()
            gray_surface.fill(self.color)  # Fill with gray color
            if self.constant_alpha != -1:
                gray_surface.set_alpha(self.constant_alpha)
            else:
                gray_surface.set_alpha(int(self.max_alpha * self.animation_progress))  # Set transparency to 128 (50% opacity)

            # Blit the grayscale surface onto the window
            window.blit(gray_surface, (0, 0))

    def update_animation(self):
        # Update animation progress based on direction and speed
        if self.direction == "in":
            self.animation_progress += self.speed
        elif self.direction == "out":
            self.animation_progress -= self.speed
        

        # Clamp animation progress to [0, 1]
        self.animation_progress = max(0, min(1, self.animation_progress))


        self.animating = self.animation_progress > 0 and self.animation_progress < 1

    def enable(self):
        if self.enabled == False:
            self.direction = "in"
            self.animation_progress = 0
            self.enabled = True

    def disable(self):
        if self.enabled == True:
            self.direction = "out"
            self.animation_progress = 1
            self.enabled = False

    def is_animating(self):
        return self.animating

    


class Tile:
    def __init__(self, walkable, x, y, image_data):
        self.walkable = walkable
        self.x = x 
        self.y = y
        image, (image_x, image_y, image_width, image_height), _ = image_data
        cropped_image = self.crop_image(image, image_x, image_y, image_width, image_height)
        self.image = pygame.transform.scale(cropped_image, (image_width * 2, image_height * 2))
    
    def crop_image(self, image, x, y, width, height):
        cropped_rect = pygame.Rect(x, y, width, height)
        cropped_image = pygame.Surface(cropped_rect.size)
        cropped_image.blit(image, (0, 0), cropped_rect)
        return cropped_image
    
    def render(self, window, offset=(0, 0)):
        offset = (min(offset[0], TILE_SIZE*MAP_WIDTH-WINDOW_WIDTH), min(offset[1], TILE_SIZE*MAP_HEIGHT-WINDOW_HEIGHT))
        offset = (max(offset[0], 0), max(offset[1], 0))
        window.blit(self.image, (self.x * TILE_SIZE - offset[0], self.y * TILE_SIZE - offset[1]))

    def is_walkable(self):
        return self.walkable


class Wall(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(False, x, y, image_data)

class Wall_Fence_1(Wall):
    def __init__(self, x, y, image_data):
        super().__init__(x, y, image_data)


class Interactable(Tile):
    def __init__(self, walkable, x, y, image_data):
        super().__init__(walkable, x, y, image_data)

    def interact(self):
        pass

class Sign(Interactable):
    def __init__(self, x, y, image_data, message):
        super().__init__(False, x, y, image_data)
        self.message = message

    def interact(self):
        return "sign", self.message

class Floor(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)


class Door(Tile):
    def __init__(self, x, y, image_data):
        super().__init__(True, x, y, image_data)

    def interact(self, player_x, player_y, player_direction):
        if (player_x*TILE_SIZE < self.x*TILE_SIZE + TILE_SIZE and player_x*TILE_SIZE > self.x*TILE_SIZE - TILE_SIZE) and (player_y*TILE_SIZE < self.y*TILE_SIZE + TILE_SIZE and player_y*TILE_SIZE > self.y*TILE_SIZE - TILE_SIZE):
            print("You opened the door!")