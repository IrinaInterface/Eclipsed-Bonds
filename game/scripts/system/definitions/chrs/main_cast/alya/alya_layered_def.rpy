image blink_alya:
    "images/characters/main_cast/alya/layered_image_assets/pose_1/face/Alya-Naked-0-Eye_Set___Open_Neutral.png" 
        choice:
            4.5
        choice: 
            3.5 
        choice: 
            1.5 
    "images/characters/main_cast/alya/layered_image_assets/pose_1/face/Alya-Naked-0-Eye_Set___Closed_Neutral.png" 
        .15 
        repeat

layeredimage alya:
    #zoom 1.5

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
            