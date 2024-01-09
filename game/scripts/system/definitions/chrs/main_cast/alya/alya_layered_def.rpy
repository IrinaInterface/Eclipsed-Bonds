define alya = Character(name="Alya",image_tag="alya",voice_tag="alya")

image blink_alya:
    "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Open_Neutral.png" 
    choice:
        4.5
    choice: 
        3.5 
    choice: 
        1.5 
    "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Closed_Neutral.png" 
    .15 
    repeat

layeredimage alya:
    zoom 1.25
    yanchor 0.9

    group back_hair:
        attribute hair_bow_pony_back default:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/back/Alya-Clothing_Preset_62-Bow_Ponytails-0.png"
        attribute hair_down_back:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/back/Alya-Clothing_Preset_62-Down-0.png"
        attribute hair_nobow_pony_back:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/back/Alya-Clothing_Preset_62-No_Bow_Ponytails-0.png"

    always:
        "images/characters/main_cast/alya/layered_image_assets/pose_1/base/Alya-Naked-Bald-0.png"
    
    group eyes:
        attribute eye_blink default:
            "blink_alya"
        attribute eye_open_neutral:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Open_Neutral.png"
        attribute eye_open_sad:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Open_Sad.png"
        attribute eye_open_mad:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Open_Mad.png"
        attribute eye_closed_neutral:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Closed_Neutral.png"
        attribute eye_closed_sad:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Closed_Sad.png"
        attribute eye_closed_mad:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Closed_Mad.png"
        attribute eye_happy:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/eye_set/Alya-Naked-0-Eye_Set___Happy.png"
    
    group mouth:
        attribute mouth_angry:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Angry.png"
        attribute mouth_angry_talk:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Angry_Talk.png"
        attribute mouth_grin:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Grin.png"
        attribute mouth_sad:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Sad.png"
        attribute mouth_sad_talk:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Sad_Talk.png"
        attribute mouth_smile default:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Smile.png"
        attribute mouth_smirk:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Smirk.png"
        attribute mouth_surprise:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Surprise.png"
        attribute mouth_talk:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/mouth_set/Alya-Naked-0-Mouth_Set___Talk.png"
    
    group face_extras:
        attribute face_blush default:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/extras/Alya-Naked-0-Extras___Blush.png"
        attribute face_fullblush:
            "/images/characters/main_cast/alya/layered_image_assets/pose_1/face/extras/Alya-Naked-0-Extras___Full_Blush.png"
        attribute face_gloom:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/extras/Alya-Naked-0-Extras___Gloom.png"
        attribute face_pale:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/face/extras/Alya-Naked-0-Extras___Pale.png"
    
    group front_hair:
        attribute hair_bow_pony_front default:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/front/Alya-Clothing_Preset_62-Bow_Ponytails-0.png"
        attribute hair_down_front:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/front/Alya-Clothing_Preset_62-Down-0.png"
        attribute hair_nobow_pony_front:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/hair/front/Alya-Clothing_Preset_62-No_Bow_Ponytails-0.png"
    
    group outfit_underwear:
        attribute underwear default:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/underwear/Alya-Clothing_Preset_2-Bald-0.png"
        attribute bikini_frill:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/underwear/Alya-Clothing_Preset_55-Bald-0.png"
        attribute bikini_plain:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/underwear/Alya-Clothing_Preset_56-Bald-0.png"
    
    group outfit_sailoruni:
        attribute sailoruni:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/sailoruni/Alya-Clothing_Preset_3-Bald-0.png"
        attribute sailoruni_indoorshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/sailoruni/Alya-Clothing_Preset_4-Bald-0.png"
        attribute sailoruni_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/sailoruni/Alya-Clothing_Preset_5-Bald-0.png"
        attribute sailoruni_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/sailoruni/Alya-Clothing_Preset_6-Bald-0.png"
    
    group outfit_workuni:
        attribute workuni:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_7-Bald-0.png"
        attribute workuni_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_8-Bald-0.png"
        attribute workuni_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_9-Bald-0.png"
        attribute workuni_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_10-Bald-0.png"
        attribute workuni_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_11-Bald-0.png"
        attribute workuni_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_12-Bald-0.png"
        attribute workuni_nobow:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_13-Bald-0.png"
        attribute workuni_nobow_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_14-Bald-0.png"
        attribute workuni_nobow_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_15-Bald-0.png"
        attribute workuni_nobow_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_16-Bald-0.png"
        attribute workuni_nobow_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_17-Bald-0.png"
        attribute workuni_nobow_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_18-Bald-0.png"
        attribute workuni_noblazer:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_19-Bald-0.png"
        attribute workuni_noblazer_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_20-Bald-0.png"
        attribute workuni_noblazer_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_21-Bald-0.png"
        attribute workuni_noblazer_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_22-Bald-0.png"
        attribute workuni_noblazer_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_23-Bald-0.png"
        attribute workuni_noblazer_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_24-Bald-0.png"
        attribute workuni_noblazer_nobow:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_25-Bald-0.png"
        attribute workuni_noblazer_nobow_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_26-Bald-0.png"
        attribute workuni_noblazer_nobow_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_27-Bald-0.png"
        attribute workuni_noblazer_nobow_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_28-Bald-0.png"
        attribute workuni_noblazer_nobow_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_29-Bald-0.png"
        attribute workuni_noblazer_nobow_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_30-Bald-0.png"
        attribute workuni_noblazer_novest:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_31-Bald-0.png"
        attribute workuni_noblazer_novest_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_32-Bald-0.png"
        attribute workuni_noblazer_novest_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_33-Bald-0.png"
        attribute workuni_noblazer_novest_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_34-Bald-0.png"
        attribute workuni_noblazer_novest_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_35-Bald-0.png"
        attribute workuni_noblazer_novest_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_36-Bald-0.png"
        attribute workuni_noblazer_novest_nobow:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_37-Bald-0.png"
        attribute workuni_noblazer_novest_nobow_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_38-Bald-0.png"
        attribute workuni_noblazer_novest_nobow_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_39-Bald-0.png"
        attribute workuni_noblazer_novest_nobow_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_40-Bald-0.png"
        attribute workuni_noblazer_novest_nobow_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_41-Bald-0.png"
        attribute workuni_noblazer_novest_nobow_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_42-Bald-0.png"
        attribute workuni_noblazer_novest_untucked:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_43-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_44-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_45-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_46-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_47-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_48-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_49-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_50-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_51-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow_loosecollar:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_52-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow_loosecollar_noshoes:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_53-Bald-0.png"
        attribute workuni_noblazer_novest_untucked_nobow_loosecollar_barelegs:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/workuni/Alya-Clothing_Preset_54-Bald-0.png"
    
    group outfit_casual:
        attribute casual_spring:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/casual/Alya-Clothing_Preset_57-Bald-0.png"
        attribute casual_spring_cardigan:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/casual/Alya-Clothing_Preset_58-Bald-0.png"
        attribute casual_summer:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/casual/Alya-Clothing_Preset_59-Bald-0.png"
    
    group outfit_special:
        attribute special_christmas:
            "images/characters/main_cast/alya/layered_image_assets/pose_1/outfits/special/Alya-Clothing_Preset_62-Bald-0.png"