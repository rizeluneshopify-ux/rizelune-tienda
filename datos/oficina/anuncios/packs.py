# Paquetes de producción: formato de los anuncios ganadores, con los productos de Rizelune.
SER = "the rizelune serum from the attached photo (a small clear glass dropper bottle with golden oil, white dropper cap and a white label reading «rizelune» with a small crescent moon), exactly as in the reference: same shape, colours and label text"
SCR = "the rizelune scalp scrub from the attached photo (a round jar with a matte white lid and a sage-green label reading «rizelune»), exactly as in the reference"
OIL = "the rizelune facial oil from the attached photo (a glass dropper bottle with golden oil and its cream box with a pink crescent moon), exactly as in the reference"
ALL3 = "the three rizelune products from the attached photos (the sage-green scrub jar, the serum dropper bottle and the facial oil with its cream box), exactly as in the references, with every label unchanged and readable"
REAL = "Shot on an iPhone, natural light, real skin and hair texture with pores and flyaways, no beauty retouching, no CGI look."
NOTXT = "No on-screen text, no subtitles, no added logos, no watermark."
IA = "Escenas creadas con IA."
FOTOS = {
 'serum': 'la foto del sérum (rizelune-referencia-serum.jpg)',
 'exf': 'la foto del tarro verde (rizelune-referencia-exfoliante.jpg)',
 'tex': 'la foto de la textura (rizelune-referencia-textura.jpg)',
 'oil': 'la foto del aceite con su caja (rizelune-referencia-aceite.jpg)',
}
def adj(*k): return 'Adjunta ' + ', '.join(FOTOS[x] for x in k) + '.'
ADJ3 = 'Adjunta las 4 fotos de referencia (sérum, tarro verde, textura y aceite).'

P = {}

P['ad-crown'] = dict(prod_orden=1, fase='Black Week', titulo='Ritual Completo · 79,99 €', formato='Imagen 1:1 y 9:16', producto='Los tres',
 basado_en='Crown Affair: «The Best Sellers Trio», sus 3 productos desde arriba sobre verde con un círculo de precio (anuncio activo en Meta).',
 herramienta='ChatGPT (imagen) + Canva para el precio', adjuntar=ADJ3,
 planos=[
  dict(nombre='Foto 1:1 · el trío desde arriba', tipo='Foto', prompt=f"Square 1:1 top-down product photo for a premium skincare brand. On a seamless, soft sage-green paper background lie {ALL3}, arranged in a loose diagonal from top-left to bottom-right: the scrub jar with its white lid resting beside it so the creamy texture shows, the serum bottle standing upright with its dropper, and the facial oil standing next to its cream box with the pink moon. A few fresh rosemary sprigs and two mint leaves scattered naturally between them. Soft diffused studio light from the top left, gentle realistic contact shadows, true-to-life colours, crisp focus on every label. Leave empty space at the top for a headline and a clear round area on the right for a price badge. No added text, no bags or extra products, no watermark."),
  dict(nombre='Foto 9:16 · versión historias', tipo='Foto', prompt="Repeat exactly the same scene, products and lighting, but in vertical 9:16 format, with more plain sage-green background above and below the products so there is room for text. Keep every label identical. No text."),
 ],
 textos=['BLACK WEEK', 'Ritual Completo', '79,99 €', 'Por separado: 97,97 €', 'Del 23 al 30 de noviembre'],
 voz='',
 copy=dict(principal="Los tres, juntos 🖤\nSérum y exfoliante de romero y menta + aceite facial con bakuchiol.\n\nRitual Completo: 79,99 € (por separado, 97,97 €).\nSolo del 23 al 30 de noviembre. Envío gratis a península y Baleares.\n\nImagen creada con IA.", titulo='Ritual Completo · 79,99 €', boton='Comprar'),
 montaje='En Canva: título arriba en verde oscuro, círculo crema con «79,99 €» a la derecha y debajo, pequeño, «Por separado: 97,97 €» (sin tachar: lo exige la ley). La versión 9:16 para historias y reels.')

P['ad-biossance'] = dict(prod_orden=2, fase='Black Week', titulo='Black Week en movimiento', formato='Vídeo 9:16 · 6 s', producto='Los tres',
 basado_en='Biossance: sus productos quietos con gotas resbalando por el cristal y la oferta encima («Static to video», varias versiones activas en Meta).',
 herramienta='ChatGPT o Gemini (foto) → Kling o Veo (vídeo)', adjuntar=ADJ3,
 planos=[
  dict(nombre='Paso 1 · Foto de lujo', tipo='Foto', prompt=f"Vertical 9:16 luxury still life for a skincare campaign. {ALL3[0].upper() + ALL3[1:]} stand together on a warm beige travertine stone block, against a deep, softly lit warm-brown background. A few drops of golden oil and tiny water droplets sit on the glass, one rosemary sprig lies on the stone. Warm side light with a soft glow and gentle reflections on the glass, high-end, calm and elegant. Leave clean empty space in the top third for text. No added text, no watermark."),
  dict(nombre='Paso 2 · Vídeo 6 s', tipo='Vídeo', prompt=f"Vertical 9:16, 6 seconds, starting exactly from the attached image. Static camera with an extremely slow push-in. Tiny droplets slowly run down the glass of the bottles, a single golden drop falls from the serum dropper onto the stone, and warm light shimmers softly across the products. The products and their labels stay perfectly still, sharp and unchanged. Audio: soft ambient tone and a delicate drip, no music, no voice. {NOTXT}"),
 ],
 textos=['0–2 s · BLACK WEEK', '2–4 s · Ritual Completo', '4–6 s · 79,99 € · por separado 97,97 €', 'Final · Hasta el 30 de noviembre'],
 voz='',
 copy=dict(principal="Black Week en Rizelune 🖤\nEl Ritual Completo (sérum + exfoliante + aceite facial) a 79,99 €. Por separado, 97,97 €.\nDel 23 al 30 de noviembre, con envío gratis a península y Baleares.\n\nEscenas creadas con IA.", titulo='Los tres por 79,99 €', boton='Comprar'),
 montaje='En CapCut: textos grandes centrados en la parte de arriba, en blanco o crema, uno detrás de otro. Música suave tipo «lujo» o sin música.')

P['ad-divi'] = dict(prod_orden=3, fase='Black Week', titulo='Mi estante de los domingos', formato='Vídeo 9:16 · 8–10 s', producto='Los tres',
 basado_en='Divi: un estante de baño real y una mano que coge el sérum (187 anuncios activos en Meta, unos 15 nuevos por semana).',
 herramienta='ChatGPT o Gemini (foto) → Veo o Kling (vídeo)', adjuntar=ADJ3,
 planos=[
  dict(nombre='Paso 1 · Foto del estante', tipo='Foto', prompt=f"Vertical 9:16 iPhone photo of a real, lived-in bathroom shelf in the evening: white countertop, a small potted rosemary plant, a wooden hairbrush, a silicone scalp massager, a lit candle in an amber glass and a folded linen towel. On the counter stand {ALL3}, labels facing the camera: the serum in front, the scrub jar on the left, the facial oil and its box on the right. Warm lamp light mixed with a little blue-hour light from a window, the edge of the mirror visible, natural everyday clutter, slightly imperfect framing. {REAL} No people, no added text, no watermark."),
  dict(nombre='Paso 2 · Vídeo: la mano coge el sérum', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, starting exactly from the attached image. Handheld iPhone feel with tiny natural movement. After one second a woman's hand with short natural nails enters from the right, picks up the serum bottle, unscrews the dropper and lifts it so a golden drop hangs from the tip, then the hand leaves the frame. The other products stay perfectly still with their labels unchanged; the candle flame flickers naturally. Audio: quiet bathroom room tone and the soft click of the dropper, no music, no voice. {NOTXT}"),
 ],
 textos=['0–2 s · Mi estante de los domingos 🕯️', '2–6 s · 3 productos · 1 ritual', 'Final · Black Week: los tres por 79,99 €'],
 voz='',
 copy=dict(principal="Domingo noche, móvil fuera y ritual 🕯️\n1. Exfoliante en la ducha\n2. Sérum de romero y menta en la raíz\n3. Aceite facial con bakuchiol\n\nBlack Week: el Ritual Completo a 79,99 € (por separado, 97,97 €).\n\nEscenas creadas con IA.", titulo='Tu ritual de domingo', boton='Comprar'),
 montaje='Después de la Black Week cambia el último texto por «Ritual Completo · rizelune.com».')

P['ad-arey'] = dict(prod_orden=4, fase='Siempre', titulo='«Tu cara tiene rutina de noche. Tu cuero cabelludo, no.»', formato='Imagen 4:5', producto='Sérum',
 basado_en='Arey: chica de perfil con el frasco pegado a la raíz y el texto «tienes rutina de noche para la cara; tu cuero cabelludo se queda fuera» (activo en Meta).',
 herramienta='ChatGPT (imagen) + Canva', adjuntar=adj('serum'),
 planos=[
  dict(nombre='Foto 4:5', tipo='Foto', prompt=f"Vertical 4:5 beauty campaign photo. A woman in her late 20s with long, glossy dark-brown hair, in profile facing right, eyes closed and smiling softly. With her left hand she lifts her hair at the crown; with her right hand she holds {SER} upright against her hair, close to the roots, label facing the camera and perfectly readable. Plain warm-grey studio wall, soft window light from the left, gentle shadows, natural skin texture with visible pores, minimal makeup, shot on an 85 mm lens. Leave clean empty space on the right half for text. No added text, no watermark."),
 ],
 textos=['Tu cara tiene rutina de noche.', 'Tu cuero cabelludo, no.', 'Sérum de romero y menta · 2 noches por semana'],
 voz='',
 copy=dict(principal="Tienes rutina de noche para la cara. ¿Y para la raíz? 🌙\nNuestro sérum de romero y menta se aplica en el cuero cabelludo, raya a raya, 2 noches por semana antes de lavarte el pelo.\n\nImagen creada con IA.", titulo='Tu ritual de noche, también en la raíz', boton='Comprar'),
 montaje='Texto a la derecha, en el hueco de pared: la primera frase en verde oscuro, la segunda igual de grande y la tercera pequeña debajo.')

P['ad-numerado'] = dict(prod_orden=5, fase='Siempre', titulo='Cómo usar el sérum según tu cuero cabelludo', formato='Vídeo 9:16 · 20–25 s', producto='Sérum',
 basado_en='«How to use rosemary hair oil» (1,1 M de visitas): chica a cámara contando pasos con los dedos y un texto por paso.',
 herramienta='Mejor grabado por ti o una amiga. Si no: Veo en Gemini (2 clips)', adjuntar=adj('serum'),
 planos=[
  dict(nombre='Clip 1 · Pasos 1 y 2', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, filmed on an iPhone propped on a shelf, natural daylight from a window, cosy bedroom softly out of focus behind her. A woman in her late 20s with long dark hair and a plain black top looks at the camera and talks naturally in Spanish from Spain, friendly and relaxed, raising one finger and then two as she counts. She holds {SER} at chest height, label facing the camera, unchanged. She says: «Uno: si tu cuero cabelludo es seco, déjalo toda la noche. Dos: si es normal, una hora antes de lavarte.» Natural lip movement, {REAL} No music. {NOTXT}"),
  dict(nombre='Clip 2 · Pasos 3 y 4', tipo='Vídeo', prompt=f"Same woman, same room, same light and framing as the previous clip, vertical 9:16, 8 seconds. She raises three fingers and then four as she counts, talking naturally in Spanish from Spain while holding the same bottle, label unchanged. She says: «Tres: si es graso, media hora. Y cuatro: si es sensible, quince minutos y solo una vez por semana.» Natural lip movement, {REAL} No music. {NOTXT}"),
 ],
 textos=['0–2 s · Cómo usar el sérum según tu cuero cabelludo 👇', '1. Seco → toda la noche', '2. Normal → 1 hora antes de lavarte', '3. Graso → 30 minutos', '4. Sensible → 15 minutos, 1 vez por semana', 'Final · Siempre en la piel, raya a raya · Haz el test en rizelune.com'],
 voz="Cómo usar el sérum según tu cuero cabelludo.\nUno: si es seco, déjalo toda la noche y lávate el pelo por la mañana.\nDos: si es normal, una hora antes de lavarte.\nTres: si es graso, media hora.\nY cuatro: si es sensible, quince minutos y solo una vez por semana.\nSiempre en la piel, raya a raya, no en el pelo. Y si dudas, haz el test en la web.",
 copy=dict(principal="¿Cuánto tiempo dejar el sérum de romero? Depende de tu cuero cabelludo 👇\nSeco: toda la noche. Normal: 1 hora. Graso: 30 minutos. Sensible: 15 minutos, 1 vez por semana.\nEn la web tienes un test de 4 preguntas que te dice tus gotas exactas.", titulo='Cómo usar el sérum de romero', boton='Más información'),
 montaje='Si lo grabas tú: móvil apoyado, luz de ventana, di el guion con tus palabras y pon cada texto cuando lo digas. Si usas IA, une los 2 clips y añade «Escenas creadas con IA» al texto del anuncio.')

P['ad-diario'] = dict(prod_orden=6, fase='Siempre', titulo='Domingo noche = ritual', formato='Vídeo 9:16 · 12–15 s', producto='Sérum',
 basado_en='Clienta de Mielle (108 mil visitas): grabado desde atrás, pelo con pinzas, cuentagotas en la raya y textos tipo diario.',
 herramienta='Veo en Gemini (2 clips)', adjuntar=adj('serum'),
 planos=[
  dict(nombre='Clip 1 · Gotas en la raya', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, handheld iPhone footage filmed by a friend from behind, at home in the evening, warm lamp light. A woman with long, straight light-brown hair sits on a bed; her dry hair is divided into sections held with two claw clips, with a clean parting down the middle. A hand holding the glass dropper of {SER} places small drops of golden oil directly on the skin along the parting, moving from front to back. When the bottle is visible its label stays unchanged. Real hair texture, natural movement, real-time speed. Audio: soft room tone and a faint rustle of hair, no music, no voice. {NOTXT}"),
  dict(nombre='Clip 2 · Masaje con las yemas', tipo='Vídeo', prompt=f"Vertical 9:16, 6 seconds, same woman, same room and same light as the previous clip, filmed from behind slightly closer. Both hands massage her scalp with the fingertips in small, slow circles along the parting, then she lets one clip out and her hair falls naturally. {REAL} Audio: soft rustle of hair, no music, no voice. {NOTXT}"),
 ],
 textos=['domingo noche = ritual 🌿', 'pelo seco, raya a raya', '6–8 gotas directo en la piel, no en el pelo', '2–3 minutos de masaje', 'y a la ducha (o a dormir si es seco)'],
 voz='',
 copy=dict(principal="Mi domingo noche, versión cuero cabelludo 🌿\nPelo seco, raya a raya, 6–8 gotas en la piel y 2–3 minutos de masaje. Luego, champú como siempre.\nSérum de romero y menta, en rizelune.com.\n\nEscenas creadas con IA.", titulo='Sérum de romero y menta', boton='Comprar'),
 montaje='Textos blancos pequeños, sin fondo, como en el original (estilo InShot). Un sonido tranquilo de moda.')

P['ad-kitsch'] = dict(prod_orden=7, fase='Siempre', titulo='3 errores muy comunes con el aceite de romero', formato='Vídeo 9:16 · 25 s con voz', producto='Sérum',
 basado_en='Kitsch: «3 errores que impiden que el pelo esté fuerte», con voz en off, cortes rápidos y un texto por error (4 versiones activas en Meta).',
 herramienta='Veo o Kling (5 clips) + tu voz en CapCut', adjuntar=adj('serum'),
 planos=[
  dict(nombre='Clip 1 · Gancho', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, iPhone footage in a bright bathroom. Close-up of a woman's hand picking up {SER} from a white counter next to a small rosemary sprig and turning it slightly towards the camera, label readable and unchanged. {REAL} No audio except room tone. {NOTXT}"),
  dict(nombre='Clip 2 · Error 1: en el pelo', tipo='Vídeo', prompt=f"Vertical 9:16, 5 seconds, close-up from above of a clean parting in dry brown hair. The glass dropper of {SER} releases two golden drops directly onto the skin of the parting (not on the lengths). Soft daylight. {REAL} {NOTXT}"),
  dict(nombre='Clip 3 · Error 2: aceite esencial puro', tipo='Vídeo', prompt=f"Vertical 9:16, 5 seconds, a white bathroom counter with a tiny unlabeled amber essential-oil bottle lying next to some rosemary sprigs; a hand gently pushes it aside and sets {SER} in its place, label facing the camera, unchanged. Soft daylight. {REAL} {NOTXT}"),
  dict(nombre='Clip 4 · Error 3: sin masaje', tipo='Vídeo', prompt=f"Vertical 9:16, 5 seconds, close-up of a woman's fingertips massaging her scalp in small slow circles along a parting in dark-brown hair, seen from slightly above. {REAL} {NOTXT}"),
  dict(nombre='Clip 5 · Cierre', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, {SER} standing on a light wooden shelf next to a rosemary sprig and a lit candle, very slow push-in, warm evening light, label perfectly still and unchanged. {NOTXT}"),
 ],
 textos=['0–3 s · 3 errores muy comunes con el aceite de romero', 'Error 1 · Ponerlo en el pelo → va en la piel, raya a raya', 'Error 2 · Usar aceite esencial puro → siempre diluido (el sérum ya viene listo)', 'Error 3 · No masajear → 2–3 minutos con las yemas', 'Final · Antes del lavado, 2 veces por semana'],
 voz="Tres errores muy comunes con el aceite de romero.\nUno: ponerlo en el pelo. Va en la piel, raya a raya.\nDos: usar aceite esencial puro. Hay que diluirlo siempre; nuestro sérum ya viene listo para usar.\nTres: no masajear. Dos o tres minutos con las yemas, en círculos pequeños.\nAntes del lavado, dos veces por semana.",
 copy=dict(principal="3 errores muy comunes con el aceite de romero (y cómo evitarlos) 👇\n1. Ponerlo en el pelo: va en la piel, raya a raya.\n2. Usar aceite esencial puro: siempre diluido. El sérum ya viene listo.\n3. No masajear: 2–3 minutos con las yemas.\n\nEscenas creadas con IA.", titulo='Úsalo bien: 3 errores comunes', boton='Más información'),
 montaje='Graba tu voz con el móvil leyendo el guion y ponla encima en CapCut. Cada clip dura lo que la frase de cada error. Subtítulos automáticos de CapCut.')

P['ad-mitos'] = dict(prod_orden=8, fase='Siempre', titulo='¿Qué mito del cuero cabelludo te crees?', formato='Carrusel 4:5 · 4 imágenes', producto='Sérum y exfoliante',
 basado_en='Briogeo: «Desmontando mitos del cuero cabelludo, un exfoliante cada vez. ¿Qué mito te crees?» (Instagram).',
 herramienta='ChatGPT (4 fotos) + Canva', adjuntar=adj('serum', 'exf', 'tex'),
 planos=[
  dict(nombre='Foto 1 · Portada', tipo='Foto', prompt=f"Vertical 4:5 product photo on a seamless soft sage-green background: {SCR} with the lid off showing its creamy texture, and {SER} standing next to it, with a rosemary sprig. Soft studio light, gentle shadow, lots of empty space in the top half for text. No text, no watermark."),
  dict(nombre='Foto 2 · Mito del aceite', tipo='Foto', prompt=f"Vertical 4:5, same sage-green background and light as the previous image: {SER} lying on its side with the dropper beside it and one golden drop on the background. Empty space in the top half for text. No text, no watermark."),
  dict(nombre='Foto 3 · Mito del exfoliante', tipo='Foto', prompt=f"Vertical 4:5, same sage-green background and light: a small scoop of the scrub (same colour and texture as in the attached texture photo) on a wooden spatula next to {SCR}. Empty space in the top half for text. No text, no watermark."),
  dict(nombre='Foto 4 · Mito de las gotas', tipo='Foto', prompt=f"Vertical 4:5, same sage-green background and light: close-up of the glass dropper of {SER} with six golden drops lined up on the background. Empty space in the top half for text. No text, no watermark."),
 ],
 textos=['1 · ¿Qué mito del cuero cabelludo te crees? 👀', '2 · MITO: el aceite engrasa el pelo. REALIDAD: se aplica antes del lavado y se va con el champú.', '3 · MITO: exfoliar es solo para pelo graso. REALIDAD: también vale para cuero cabelludo normal o seco. 1 vez por semana (cada 2 si es sensible).', '4 · MITO: más gotas, mejor. REALIDAD: 6–8 gotas para toda la cabeza.'],
 voz='',
 copy=dict(principal="Desmontando mitos del cuero cabelludo, uno a uno 😉\n¿Cuál te creías tú? Cuéntanoslo en comentarios 👇\n\nImágenes creadas con IA.", titulo='Mitos del cuero cabelludo', boton='Más información'),
 montaje='En Canva: «MITO» en rojo apagado y «REALIDAD» en verde oscuro, letra grande arriba. Sube las 4 como carrusel en este orden.')

P['ad-exfoliar'] = dict(prod_orden=9, fase='Siempre', titulo='Una vez por semana, en la ducha', formato='Vídeo 9:16 · 15 s', producto='Exfoliante',
 basado_en='«Cómo exfoliar tu cuero cabelludo en casa» (371 mil visitas, en español): cara muy cerca, melena y masaje con espuma en la ducha.',
 herramienta='Veo en Gemini (3 clips) + CapCut', adjuntar=adj('exf', 'tex'),
 planos=[
  dict(nombre='Clip 1 · Gancho en el espejo', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, iPhone selfie footage in a bathroom with soft daylight. A woman in her late 20s with long dark hair parts her hair at the roots with her fingers, checks it closely in the mirror with a slightly unconvinced look, then glances at the camera. {REAL} No talking, no music. {NOTXT}"),
  dict(nombre='Clip 2 · Masaje en la ducha', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, close-up in a shower with warm light and a little steam. Wet dark hair seen from slightly above and behind. Two hands with short natural nails massage the scrub (same colour and texture as in the attached texture photo) into the wet scalp in small, gentle circles, and a light foam forms. {SCR[0].upper() + SCR[1:]}, open, sits on the shower shelf in a corner of the frame, label unchanged. {REAL} Audio: running water and a gentle scrubbing sound, no music, no voice. {NOTXT}"),
  dict(nombre='Clip 3 · Aclarado y melena', tipo='Vídeo', prompt=f"Vertical 9:16, 5 seconds, the same woman rinses her hair under the shower, then a quick cut to her in a bathrobe running her fingers through her clean, damp, shiny hair in front of the mirror, relaxed. {REAL} Audio: water then quiet room tone, no music, no voice. {NOTXT}"),
 ],
 textos=['0–3 s · Cuando la raíz se engrasa a los dos días…', 'una vez por semana, en la ducha:', 'tamaño de una nuez, masaje suave', '5 minutos (hasta 15 si es graso) y aclara', 'Final · Exfoliante de romero y menta 🌿'],
 voz='',
 copy=dict(principal="Una vez por semana, en la ducha 🚿\nUna cantidad del tamaño de una nuez, masaje suave, 5 minutos y aclara. Después, tu champú.\nExfoliante capilar de romero y menta.\n\nEscenas creadas con IA.", titulo='Exfoliante de romero y menta', boton='Comprar'),
 montaje='Subtítulos grandes en el centro, palabra a palabra, como el original (CapCut → Subtítulos automáticos con tu voz leyendo los textos).')

P['ad-asmr'] = dict(prod_orden=10, fase='Siempre', titulo='Sube el volumen 🎧', formato='Vídeo 9:16 · 10–12 s', producto='Exfoliante',
 basado_en='Twelve12 Beauté (5,3 M de visitas): plano muy cerca de la raya mientras le limpian el cuero cabelludo, casi sin texto, con sonido.',
 herramienta='Veo en Gemini (genera también el sonido)', adjuntar=adj('exf', 'tex'),
 planos=[
  dict(nombre='Clip 1 · Exfoliante en la raya', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, macro close-up from above of a clean straight parting in dark-brown hair, soft warm bathroom light. Bare fingertips with short natural nails place a small amount of the scrub (same colour and texture as in the attached texture photo) along the parting and massage it in slow, small circles; the fine natural grains are visible on the skin and slowly spread. Very satisfying, slow and steady camera, shallow depth of field. Audio: crisp ASMR sounds of the gritty scrub and fingertips on the scalp, no music, no voice. {NOTXT}"),
  dict(nombre='Clip 2 · El tarro', tipo='Vídeo', prompt=f"Vertical 9:16, 3 seconds, {SCR} on a wet stone surface in a shower, a fingertip scoops some scrub from the open jar, water droplets around, warm light, label unchanged. Audio: soft scoop sound and water drops, no music. {NOTXT}"),
 ],
 textos=['🎧 sube el volumen', 'exfoliante de romero y menta', '1 vez por semana'],
 voz='',
 copy=dict(principal="🎧 Con sonido.\nExfoliante capilar de romero y menta, una vez por semana en la ducha.\n\nEscenas creadas con IA.", titulo='Exfoliante de romero y menta', boton='Comprar'),
 montaje='Pocos textos, el sonido muy alto. Primero el clip 1 y al final 2–3 segundos del clip 2.')

P['ad-bakuchiol'] = dict(prod_orden=11, fase='Siempre', titulo='¿Qué me pongo por la noche?', formato='Vídeo 9:16 · 12 s', producto='Aceite facial',
 basado_en='Vídeo de bakuchiol (74 mil visitas): responde a «¿qué usas en lugar del retinol?» con subtítulos grandes y enseña el bote.',
 herramienta='Veo en Gemini (2 clips)', adjuntar=adj('oil'),
 planos=[
  dict(nombre='Clip 1 · Aplicándolo', tipo='Vídeo', prompt=f"Vertical 9:16, 8 seconds, iPhone footage at night at a small vanity lit by a warm lamp and a candle. A woman in her early 30s with clean bare skin and her hair tied back looks in the mirror, places 3 drops of golden oil from the dropper of {OIL} onto her fingertips and gently presses it into her cheeks and forehead with light taps, avoiding the eyes. The bottle and its cream box stand on the vanity, labels unchanged. Calm and unhurried. {REAL} Audio: quiet room tone and a soft exhale, no music, no voice. {NOTXT}"),
  dict(nombre='Clip 2 · La gota', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, macro close-up of a single golden drop falling from the glass dropper of {OIL} onto a fingertip, warm candlelight behind, the cream box with the pink moon softly out of focus, label unchanged. {NOTXT}"),
 ],
 textos=['Arriba todo el vídeo · ¿Qué me pongo por la noche si el retinol me parece demasiado?', 'Aceite facial con bakuchiol, un activo de origen vegetal', '3–4 gotas, cada noche, a toquecitos', 'y por la mañana, protector solar'],
 voz='',
 copy=dict(principal="¿Qué ponerte por la noche si el retinol te parece demasiado? 🌙\nAceite facial con bakuchiol y rosa mosqueta: 3–4 gotas cada noche, a toquecitos. Por la mañana, protector solar.\n\nEscenas creadas con IA.", titulo='Aceite facial con bakuchiol', boton='Comprar'),
 montaje='La pregunta fija arriba durante todo el vídeo, como el original; el resto de textos van saliendo abajo. Subtítulos en blanco y rosa.')

P['ad-gisou'] = dict(prod_orden=12, fase='Siempre', titulo='Mi ritual de los domingos (los tres)', formato='Vídeo 9:16 · 15–20 s', producto='Los tres',
 basado_en='Gisou: creadora frente al espejo con el pelo suelto y después cortes rápidos de cada paso de su rutina con los productos (activo en Meta).',
 herramienta='Veo en Gemini (5 clips) + CapCut', adjuntar=ADJ3,
 planos=[
  dict(nombre='Clip 1 · Espejo', tipo='Vídeo', prompt=f"Vertical 9:16, 3 seconds, iPhone footage of a woman in her late 20s with long, glossy brown hair in front of a bathroom mirror, running both hands through her hair and letting it fall, relaxed smile, face partly turned away. Warm morning light. {REAL} {NOTXT}"),
  dict(nombre='Clip 2 · Sérum (pelo seco)', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, close-up from above: the glass dropper of {SER} places golden drops along a parting in dry hair, then fingertips start a small circular massage. {REAL} {NOTXT}"),
  dict(nombre='Clip 3 · Exfoliante en la ducha', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, in the shower: two hands massage the scrub (same colour and texture as in the attached texture photo) into wet hair at the roots; {SCR} sits on the shower shelf, label unchanged. Warm light, light steam. {REAL} {NOTXT}"),
  dict(nombre='Clip 4 · Toalla', tipo='Vídeo', prompt=f"Vertical 9:16, 3 seconds, the same woman wraps her clean hair in a white towel and smiles at the mirror. {REAL} {NOTXT}"),
  dict(nombre='Clip 5 · Aceite facial de noche', tipo='Vídeo', prompt=f"Vertical 9:16, 4 seconds, at night by candlelight, the same woman presses facial oil into her cheek with light taps; {OIL} stands on the vanity, label unchanged. {REAL} {NOTXT}"),
 ],
 textos=['mi ritual de los domingos 🌿', '1. sérum en la raíz, con el pelo seco', '2. exfoliante en la ducha', '3. aceite facial antes de dormir', 'Final · Ritual Completo en rizelune.com'],
 voz='',
 copy=dict(principal="Mi ritual de los domingos, en 3 pasos 🌿\n1. Sérum de romero y menta en la raíz\n2. Exfoliante en la ducha\n3. Aceite facial con bakuchiol antes de dormir\n\nEl Ritual Completo, en rizelune.com.\n\nEscenas creadas con IA.", titulo='Tu ritual en 3 pasos', boton='Comprar'),
 montaje='Cortes rápidos al ritmo de una canción de moda, un texto por paso. En la Black Week cambia el final por «Los tres por 79,99 €».')
