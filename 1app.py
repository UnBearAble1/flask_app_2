# Import Flask and dependencies
from flask import Flask, redirect, url_for, render_template

# Create an app, being sure to pass __name__
app = Flask(__name__)

@app.route("/")
def Home():
	return render_template("Home.html")

@app.route("/persistent-damage")
def Persistent_Damage():
	return render_template("persistent-damage.html")

@app.route("/frightened")
def Frightened():
	return render_template("frightened.html")

@app.route("/dazzled")
def Dazzled():
	return render_template("dazzled.html")

@app.route("/controlled")
def Controlled():
	return render_template("controlled.html")

@app.route("/undetected")
def Undetected():
	return render_template("undetected.html")

@app.route("/enfeebled")
def Enfeebled():
	return render_template("enfeebled.html")

@app.route("/clumsy")
def Clumsy():
	return render_template("clumsy.html")

@app.route("/petrified")
def Petrified():
	return render_template("petrified.html")

@app.route("/paralyzed")
def Paralyzed():
	return render_template("paralyzed.html")

@app.route("/grabbed")
def Grabbed():
	return render_template("grabbed.html")

@app.route("/unconscious")
def Unconscious():
	return render_template("unconscious.html")

@app.route("/quickened")
def Quickened():
	return render_template("quickened.html")

@app.route("/blinded")
def Blinded():
	return render_template("blinded.html")

@app.route("/deafened")
def Deafened():
	return render_template("deafened.html")

@app.route("/concealed")
def Concealed():
	return render_template("concealed.html")

@app.route("/wounded")
def Wounded():
	return render_template("wounded.html")

@app.route("/stupefied")
def Stupefied():
	return render_template("stupefied.html")

@app.route("/invisible")
def Invisible():
	return render_template("invisible.html")

@app.route("/fascinated")
def Fascinated():
	return render_template("fascinated.html")

@app.route("/unnoticed")
def Unnoticed():
	return render_template("unnoticed.html")

@app.route("/fleeing")
def Fleeing():
	return render_template("fleeing.html")

@app.route("/immobilized")
def Immobilized():
	return render_template("immobilized.html")

@app.route("/sickened")
def Sickened():
	return render_template("sickened.html")

@app.route("/observed")
def Observed():
	return render_template("observed.html")

@app.route("/confused")
def Confused():
	return render_template("confused.html")

@app.route("/prone")
def Prone():
	return render_template("prone.html")

@app.route("/encumbered")
def Encumbered():
	return render_template("encumbered.html")

@app.route("/doomed")
def Doomed():
	return render_template("doomed.html")

@app.route("/slowed")
def Slowed():
	return render_template("slowed.html")

@app.route("/restrained")
def Restrained():
	return render_template("restrained.html")

@app.route("/fatigued")
def Fatigued():
	return render_template("fatigued.html")

@app.route("/drained")
def Drained():
	return render_template("drained.html")

@app.route("/hidden")
def Hidden():
	return render_template("hidden.html")

@app.route("/broken")
def Broken():
	return render_template("broken.html")

@app.route("/stunned")
def Stunned():
	return render_template("stunned.html")

@app.route("/aid")
def Aid():
	return render_template("aid.html")

@app.route("/drop-prone")
def Drop_Prone():
	return render_template("drop-prone.html")

@app.route("/maneuver-in-flight")
def Maneuver_In_Flight():
	return render_template("maneuver-in-flight.html")

@app.route("/escape")
def Escape():
	return render_template("escape.html")

@app.route("/avert-gaze")
def Avert_Gaze():
	return render_template("avert-gaze.html")

@app.route("/ready")
def Ready():
	return render_template("ready.html")

@app.route("/sense-motive")
def Sense_Motive():
	return render_template("sense-motive.html")

@app.route("/fly")
def Fly():
	return render_template("fly.html")

@app.route("/point-out")
def Point_Out():
	return render_template("point-out.html")

@app.route("/mount")
def Mount():
	return render_template("mount.html")

@app.route("/tumble-through")
def Tumble_Through():
	return render_template("tumble-through.html")

@app.route("/stand")
def Stand():
	return render_template("stand.html")

@app.route("/take-cover")
def Take_Cover():
	return render_template("take-cover.html")

@app.route("/strike")
def Strike():
	return render_template("strike.html")

@app.route("/delay")
def Delay():
	return render_template("delay.html")

@app.route("/crawl")
def Crawl():
	return render_template("crawl.html")

@app.route("/recall-knowledge")
def Recall_Knowledge():
	return render_template("recall-knowledge.html")

@app.route("/dismiss")
def Dismiss():
	return render_template("dismiss.html")

@app.route("/burrow")
def Burrow():
	return render_template("burrow.html")

@app.route("/seek")
def Seek():
	return render_template("seek.html")

@app.route("/step")
def Step():
	return render_template("step.html")

@app.route("/interact")
def Interact():
	return render_template("interact.html")

@app.route("/leap")
def Leap():
	return render_template("leap.html")

@app.route("/balance")
def Balance():
	return render_template("balance.html")

@app.route("/squeeze")
def Squeeze():
	return render_template("squeeze.html")

@app.route("/grab-an-edge")
def Grab_an_Edge():
	return render_template("grab-an-edge.html")

@app.route("/decipher-writing")
def Decipher_Writing():
	return render_template("decipher-writing.html")

@app.route("/arrest-a-fall")
def Arrest_a_Fall():
	return render_template("arrest-a-fall.html")

@app.route("/release")
def Release():
	return render_template("release.html")

@app.route("/stride")
def Stride():
	return render_template("stride.html")

@app.route("/raise-a-shield")
def Raise_a_Shield():
	return render_template("raise-a-shield.html")

@app.route("/acrobatics-dex")
def Acrobatics__DEX_():
	return render_template("acrobatics-dex.html")

@app.route("/climb")
def Climb():
	return render_template("climb.html")

@app.route("/force-open")
def Force_Open():
	return render_template("force-open.html")

@app.route("/high-jump")
def High_Jump():
	return render_template("high-jump.html")

@app.route("/long-jump")
def Long_Jump():
	return render_template("long-jump.html")

@app.route("/identify-alchemy")
def Identify_Alchemy():
	return render_template("identify-alchemy.html")

@app.route("/crafting-int")
def Crafting__INT_():
	return render_template("crafting-int.html")

@app.route("/manipulate")
def Manipulate():
	return render_template("manipulate.html")

@app.route("/auditory")
def Auditory():
	return render_template("auditory.html")

@app.route("/linguistic")
def Linguistic():
	return render_template("linguistic.html")

@app.route("/concentrate")
def Concentrate():
	return render_template("concentrate.html")

@app.route("/visual")
def Visual():
	return render_template("visual.html")

@app.route("/secret")
def Secret():
	return render_template("secret.html")

@app.route("/exploration")
def Exploration():
	return render_template("exploration.html")

@app.route("/impersonate")
def Impersonate():
	return render_template("impersonate.html")

@app.route("/mental")
def Mental():
	return render_template("mental.html")

@app.route("/create-a-diversion")
def Create_a_Diversion():
	return render_template("create-a-diversion.html")

@app.route("/lie")
def Lie():
	return render_template("lie.html")

@app.route("/feint")
def Feint():
	return render_template("feint.html")

@app.route("/request")
def Request():
	return render_template("request.html")

@app.route("/disposition-and-attitude")
def Disposition_and_Attitude():
	return render_template("disposition-and-attitude.html")

@app.route("/emotion")
def Emotion():
	return render_template("emotion.html")

@app.route("/coerce")
def Coerce():
	return render_template("coerce.html")

@app.route("/fear")
def Fear():
	return render_template("fear.html")

@app.route("/demoralize")
def Demoralize():
	return render_template("demoralize.html")

@app.route("/lore-int")
def Lore__INT_():
	return render_template("lore-int.html")

@app.route("/long-term-rest")
def Long_Term_Rest():
	return render_template("long-term-rest.html")

@app.route("/earn-income")
def Earn_Income():
	return render_template("earn-income.html")

@app.route("/gather-information")
def Gather_Information():
	return render_template("gather-information.html")

@app.route("/treat-poison")
def Treat_Poison():
	return render_template("treat-poison.html")

@app.route("/treat-disease")
def Treat_Disease():
	return render_template("treat-disease.html")

@app.route("/command-an-animal")
def Command_an_Animal():
	return render_template("command-an-animal.html")

@app.route("/nature-wis")
def Nature__WIS_():
	return render_template("nature-wis.html")

@app.route("/occultism-int")
def Occultism__INT_():
	return render_template("occultism-int.html")

@app.route("/move")
def Move():
	return render_template("move.html")

@app.route("/performance-chr")
def Performance__CHR_():
	return render_template("performance-chr.html")

@app.route("/religion-wis")
def Religion__WIS_():
	return render_template("religion-wis.html")

@app.route("/subsist")
def Subsist():
	return render_template("subsist.html")

@app.route("/create-forgery")
def Create_Forgery():
	return render_template("create-forgery.html")

@app.route("/society-int")
def Society__INT_():
	return render_template("society-int.html")

@app.route("/conceal-an-object")
def Conceal_an_Object():
	return render_template("conceal-an-object.html")

@app.route("/hide")
def Hide():
	return render_template("hide.html")

@app.route("/sneak")
def Sneak():
	return render_template("sneak.html")

@app.route("/stealth-dex")
def Stealth__DEX_():
	return render_template("stealth-dex.html")

@app.route("/cover")
def Cover():
	return render_template("cover.html")

@app.route("/sense-direction")
def Sense_Direction():
	return render_template("sense-direction.html")

@app.route("/cover-tracks")
def Cover_Tracks():
	return render_template("cover-tracks.html")

@app.route("/survival-wis")
def Survival__WIS_():
	return render_template("survival-wis.html")

@app.route("/track")
def Track():
	return render_template("track.html")

@app.route("/palm-an-object")
def Palm_an_Object():
	return render_template("palm-an-object.html")

@app.route("/steal")
def Steal():
	return render_template("steal.html")

@app.route("/pick-a-lock")
def Pick_a_Lock():
	return render_template("pick-a-lock.html")

@app.route("/thievery-dex")
def Thievery__DEX_():
	return render_template("thievery-dex.html")

@app.route("/difficult-terrain")
def Difficult_Terrain():
	return render_template("difficult-terrain.html")

@app.route("/environmental-damage")
def Environmental_Damage():
	return render_template("environmental-damage.html")

@app.route("/temperature")
def Temperature():
	return render_template("temperature.html")

@app.route("/cursed")
def Cursed():
	return render_template("cursed.html")

@app.route("/destiny")
def Destiny():
	return render_template("destiny.html")

@app.route("/divine-curse")
def Divine_Curse():
	return render_template("divine-curse.html")

@app.route("/dread")
def Dread():
	return render_template("dread.html")

@app.route("/delusions")
def Delusions():
	return render_template("delusions.html")

@app.route("/clueless")
def Clueless():
	return render_template("clueless.html")

@app.route("/charitable")
def Charitable():
	return render_template("charitable.html")

@app.route("/drug-addiction")
def Drug_Addiction():
	return render_template("drug-addiction.html")

@app.route("/easily-overstimulated")
def Easily_Overstimulated():
	return render_template("easily-overstimulated.html")

@app.route("/callous")
def Callous():
	return render_template("callous.html")

@app.route("/bad-temper")
def Bad_Temper():
	return render_template("bad-temper.html")

@app.route("/code-of-honor")
def Code_of_Honor():
	return render_template("code-of-honor.html")

@app.route("/disciples-of-faith")
def Disciples_of_Faith():
	return render_template("disciples-of-faith.html")

@app.route("/bloodlust")
def Bloodlust():
	return render_template("bloodlust.html")

@app.route("/amnesia")
def Amnesia():
	return render_template("amnesia.html")

@app.route("/easy-to-read")
def Easy_to_Read():
	return render_template("easy-to-read.html")

@app.route("/curious")
def Curious():
	return render_template("curious.html")

@app.route("/dyslexia")
def Dyslexia():
	return render_template("dyslexia.html")

@app.route("/compulsive-behavior")
def Compulsive_Behavior():
	return render_template("compulsive-behavior.html")

@app.route("/cowardice")
def Cowardice():
	return render_template("cowardice.html")

@app.route("/enemies")
def Enemies():
	return render_template("enemies.html")

@app.route("/flashbacks")
def Flashbacks():
	return render_template("flashbacks.html")

@app.route("/frightens-animals")
def Frightens_Animals():
	return render_template("frightens-animals.html")

@app.route("/gluttony")
def Gluttony():
	return render_template("gluttony.html")

@app.route("/greed")
def Greed():
	return render_template("greed.html")

@app.route("/gullibility")
def Gullibility():
	return render_template("gullibility.html")

@app.route("/honesty")
def Honesty():
	return render_template("honesty.html")

@app.route("/impulsiveness")
def Impulsiveness():
	return render_template("impulsiveness.html")

@app.route("/resting")
def Resting():
	return render_template("resting.html")

@app.route("/insomniac")
def Insomniac():
	return render_template("insomniac.html")

@app.route("/jealousy")
def Jealousy():
	return render_template("jealousy.html")

@app.route("/kleptomania")
def Kleptomania():
	return render_template("kleptomania.html")

@app.route("/lecherousness")
def Lecherousness():
	return render_template("lecherousness.html")

@app.route("/loner")
def Loner():
	return render_template("loner.html")

@app.route("/magic-susceptibility")
def Magic_Susceptibility():
	return render_template("magic-susceptibility.html")

@app.route("/miserliness")
def Miserliness():
	return render_template("miserliness.html")

@app.route("/no-sense-of-humor")
def No_Sense_of_Humor():
	return render_template("no-sense-of-humor.html")

@app.route("/no-sense-of-smelltaste")
def No_Sense_of_Smell_Taste():
	return render_template("no-sense-of-smelltaste.html")

@app.route("/nocturnal")
def Nocturnal():
	return render_template("nocturnal.html")

@app.route("/non-iconographic")
def Non_Iconographic():
	return render_template("non-iconographic.html")

@app.route("/obsession")
def Obsession():
	return render_template("obsession.html")

@app.route("/odious-personal-habit")
def Odious_Personal_Habit():
	return render_template("odious-personal-habit.html")

@app.route("/on-the-edge")
def On_the_Edge():
	return render_template("on-the-edge.html")

@app.route("/deafness")
def Deafness():
	return render_template("deafness.html")

@app.route("/motion-sickness")
def Motion_Sickness():
	return render_template("motion-sickness.html")

@app.route("/chronic-pain")
def Chronic_Pain():
	return render_template("chronic-pain.html")

@app.route("/fragile")
def Fragile():
	return render_template("fragile.html")

@app.route("/farsighted")
def Farsighted():
	return render_template("farsighted.html")

@app.route("/one-arm")
def One_Arm():
	return render_template("one-arm.html")

@app.route("/bad-back")
def Bad_Back():
	return render_template("bad-back.html")

@app.route("/leg-disability")
def Leg_Disability():
	return render_template("leg-disability.html")

@app.route("/physically-off-putting")
def Physically_Off_Putting():
	return render_template("physically-off-putting.html")

@app.route("/alcoholism")
def Alcoholism():
	return render_template("alcoholism.html")

@app.route("/numb")
def Numb():
	return render_template("numb.html")

@app.route("/natural-climate-cold")
def Natural_Climate__Cold():
	return render_template("natural-climate-cold.html")

@app.route("/mute")
def Mute():
	return render_template("mute.html")

@app.route("/hemophilia")
def Hemophilia():
	return render_template("hemophilia.html")

@app.route("/klutz")
def Klutz():
	return render_template("klutz.html")

@app.route("/low-pain-threshold")
def Low_Pain_Threshold():
	return render_template("low-pain-threshold.html")

@app.route("/dependency")
def Dependency():
	return render_template("dependency.html")

@app.route("/cannot-speak")
def Cannot_Speak():
	return render_template("cannot-speak.html")

@app.route("/hard-of-hearing")
def Hard_of_Hearing():
	return render_template("hard-of-hearing.html")

@app.route("/extra-sleep")
def Extra_Sleep():
	return render_template("extra-sleep.html")

@app.route("/fat")
def Fat():
	return render_template("fat.html")

@app.route("/bad-grip")
def Bad_Grip():
	return render_template("bad-grip.html")

@app.route("/light-sleeper")
def Light_Sleeper():
	return render_template("light-sleeper.html")

@app.route("/blindness")
def Blindness():
	return render_template("blindness.html")

@app.route("/neurological-disorder")
def Neurological_Disorder():
	return render_template("neurological-disorder.html")

@app.route("/one-eye")
def One_Eye():
	return render_template("one-eye.html")

@app.route("/natural-climate-hot")
def Natural_Climate__Hot():
	return render_template("natural-climate-hot.html")

@app.route("/nearsighted")
def Nearsighted():
	return render_template("nearsighted.html")

@app.route("/depressed")
def Depressed():
	return render_template("depressed.html")

@app.route("/guilt-complex")
def Guilt_Complex():
	return render_template("guilt-complex.html")

@app.route("/mood-swings")
def Mood_Swings():
	return render_template("mood-swings.html")

@app.route("/pacifism")
def Pacifism():
	return render_template("pacifism.html")

@app.route("/paranoia")
def Paranoia():
	return render_template("paranoia.html")

@app.route("/phantom-voices")
def Phantom_Voices():
	return render_template("phantom-voices.html")

@app.route("/phobias")
def Phobias():
	return render_template("phobias.html")

@app.route("/post-combat-shakes")
def Post_Combat_Shakes():
	return render_template("post-combat-shakes.html")

@app.route("/pyromania")
def Pyromania():
	return render_template("pyromania.html")

@app.route("/restricted-diet")
def Restricted_Diet():
	return render_template("restricted-diet.html")

@app.route("/restricted-vision")
def Restricted_Vision():
	return render_template("restricted-vision.html")

@app.route("/resistance")
def Resistance():
	return render_template("resistance.html")

@app.route("/weakness")
def Weakness():
	return render_template("weakness.html")

@app.route("/revulsion")
def Revulsion():
	return render_template("revulsion.html")

@app.route("/sadism")
def Sadism():
	return render_template("sadism.html")

@app.route("/secret-3536570")
def Secret():
	return render_template("secret-3536570.html")

@app.route("/selfless")
def Selfless():
	return render_template("selfless.html")

@app.route("/sense-of-duty")
def Sense_of_Duty():
	return render_template("sense-of-duty.html")

@app.route("/short-attention-span")
def Short_Attention_Span():
	return render_template("short-attention-span.html")

@app.route("/short-life-span")
def Short_Life_Span():
	return render_template("short-life-span.html")

@app.route("/shyness")
def Shyness():
	return render_template("shyness.html")

@app.route("/sleepwalker")
def Sleepwalker():
	return render_template("sleepwalker.html")

@app.route("/sleepy")
def Sleepy():
	return render_template("sleepy.html")

@app.route("/slow-healer")
def Slow_Healer():
	return render_template("slow-healer.html")

@app.route("/social-stigma")
def Social_Stigma():
	return render_template("social-stigma.html")

@app.route("/split-personality")
def Split_Personality():
	return render_template("split-personality.html")

@app.route("/stubbornness")
def Stubbornness():
	return render_template("stubbornness.html")

@app.route("/stuttering")
def Stuttering():
	return render_template("stuttering.html")

@app.route("/supersensitive")
def Supersensitive():
	return render_template("supersensitive.html")

@app.route("/susceptible")
def Susceptible():
	return render_template("susceptible.html")

@app.route("/trademark")
def Trademark():
	return render_template("trademark.html")

@app.route("/trickster")
def Trickster():
	return render_template("trickster.html")

@app.route("/truthfulness")
def Truthfulness():
	return render_template("truthfulness.html")

@app.route("/uncontrollable-appetite")
def Uncontrollable_Appetite():
	return render_template("uncontrollable-appetite.html")

@app.route("/unhealing")
def Unhealing():
	return render_template("unhealing.html")

@app.route("/unluckiness")
def Unluckiness():
	return render_template("unluckiness.html")

@app.route("/vow")
def Vow():
	return render_template("vow.html")

@app.route("/vulnerability")
def Vulnerability():
	return render_template("vulnerability.html")

@app.route("/weakness-4510561")
def Weakness():
	return render_template("weakness-4510561.html")

@app.route("/workaholic")
def Workaholic():
	return render_template("workaholic.html")

@app.route("/vengeful-hatred")
def Vengeful_Hatred():
	return render_template("vengeful-hatred.html")

@app.route("/striking-retribution")
def Striking_Retribution():
	return render_template("striking-retribution.html")

@app.route("/tomb-watchers-glare")
def Tomb_Watchers_Glare():
	return render_template("tomb-watchers-glare.html")

@app.route("/ghost-touch")
def Ghost_Touch():
	return render_template("ghost-touch.html")

@app.route("/incorporeal")
def Incorporeal():
	return render_template("incorporeal.html")

@app.route("/harmlessly-cute")
def Harmlessly_Cute():
	return render_template("harmlessly-cute.html")

@app.route("/impersenator")
def Impersenator():
	return render_template("impersenator.html")

@app.route("/elude-trouble")
def Elude_Trouble():
	return render_template("elude-trouble.html")

@app.route("/kneecap")
def Kneecap():
	return render_template("kneecap.html")

@app.route("/recognize-ambush")
def Recognize_Ambush():
	return render_template("recognize-ambush.html")

@app.route("/scamper")
def Scamper():
	return render_template("scamper.html")

@app.route("/skittering-scuttle")
def Skittering_Scuttle():
	return render_template("skittering-scuttle.html")

@app.route("/vengeance")
def Vengeance():
	return render_template("vengeance.html")

@app.route("/incredible-ferocity")
def Incredible_Ferocity():
	return render_template("incredible-ferocity.html")

@app.route("/rampaging-ferocity")
def Rampaging_Ferocity():
	return render_template("rampaging-ferocity.html")

@app.route("/undying-ferocity")
def Undying_Ferocity():
	return render_template("undying-ferocity.html")

@app.route("/rapid-instincts")
def Rapid_Instincts():
	return render_template("rapid-instincts.html")

@app.route("/twitchy")
def Twitchy():
	return render_template("twitchy.html")

@app.route("/threatening-approach")
def Threatening_Approach():
	return render_template("threatening-approach.html")

@app.route("/predators-growl")
def Predators_Growl():
	return render_template("predators-growl.html")

@app.route("/ancestral-performer")
def Ancestral_Performer():
	return render_template("ancestral-performer.html")

@app.route("/ancestral-ties")
def Ancestral_Ties():
	return render_template("ancestral-ties.html")

@app.route("/ancestral-warden")
def Ancestral_Warden():
	return render_template("ancestral-warden.html")

@app.route("/palpable-enmity")
def Palpable_Enmity():
	return render_template("palpable-enmity.html")

@app.route("/skilled-surge")
def Skilled_Surge():
	return render_template("skilled-surge.html")

@app.route("/iron-born")
def Iron_Born():
	return render_template("iron-born.html")

@app.route("/ageless-patience")
def Ageless_Patience():
	return render_template("ageless-patience.html")

@app.route("/scavengers-search")
def Scavengers_Search():
	return render_template("scavengers-search.html")

@app.route("/shapechangers-intuition")
def Shapechangers_Intuition():
	return render_template("shapechangers-intuition.html")

@app.route("/watchful")
def Watchful():
	return render_template("watchful.html")

@app.route("/defiance-unto-death")
def Defiance_Unto_Death():
	return render_template("defiance-unto-death.html")

@app.route("/ancestral-suspicion")
def Ancestral_Suspicion():
	return render_template("ancestral-suspicion.html")

@app.route("/doughtiness")
def Doughtiness():
	return render_template("doughtiness.html")

@app.route("/irrepressible")
def Irrepressible():
	return render_template("irrepressible.html")

@app.route("/stone-face")
def Stone_Face():
	return render_template("stone-face.html")

@app.route("/unwavering-mein")
def Unwavering_Mein():
	return render_template("unwavering-mein.html")

@app.route("/verve")
def Verve():
	return render_template("verve.html")

@app.route("/willful-and-proud")
def Willful_and_Proud():
	return render_template("willful-and-proud.html")

@app.route("/ceaseless-shadows")
def Ceaseless_Shadows():
	return render_template("ceaseless-shadows.html")

@app.route("/war-marcher")
def War_marcher():
	return render_template("war-marcher.html")

@app.route("/keep-up-appearances")
def Keep_Up_Appearances():
	return render_template("keep-up-appearances.html")

@app.route("/easily-dismissed")
def Easily_Dismissed():
	return render_template("easily-dismissed.html")

@app.route("/aerolist")
def Aerolist():
	return render_template("aerolist.html")

@app.route("/skittering-sneak")
def Skittering_Sneak():
	return render_template("skittering-sneak.html")

@app.route("/sense-allies")
def Sense_Allies():
	return render_template("sense-allies.html")

@app.route("/fox-trick")
def Fox_Trick():
	return render_template("fox-trick.html")

@app.route("/protective-surge")
def Protective_Surge():
	return render_template("protective-surge.html")

@app.route("/defiant-yell")
def Defiant_Yell():
	return render_template("defiant-yell.html")

@app.route("/intuitive-cooperation")
def Intuitive_Cooperation():
	return render_template("intuitive-cooperation.html")

@app.route("/drag-down")
def Drag_Down():
	return render_template("drag-down.html")

@app.route("/palegic-aptitude")
def Palegic_Aptitude():
	return render_template("palegic-aptitude.html")

@app.route("/riptide")
def Riptide():
	return render_template("riptide.html")

@app.route("/cliff-hanger")
def Cliff_Hanger():
	return render_template("cliff-hanger.html")

@app.route("/quick-hands")
def Quick_Hands():
	return render_template("quick-hands.html")

@app.route("/expert-drill-sergeant")
def Expert_Drill_Sergeant():
	return render_template("expert-drill-sergeant.html")

@app.route("/graceful-guidance")
def Graceful_Guidance():
	return render_template("graceful-guidance.html")

@app.route("/wary-of-enchantment")
def Wary_of_Enchantment():
	return render_template("wary-of-enchantment.html")

@app.route("/hustle")
def Hustle():
	return render_template("hustle.html")

@app.route("/eye-for-treasure")
def Eye_for_Treasure():
	return render_template("eye-for-treasure.html")

@app.route("/junk-tinker")
def Junk_Tinker():
	return render_template("junk-tinker.html")

@app.route("/reinforcement")
def Reinforcement():
	return render_template("reinforcement.html")

@app.route("/tinkering-fingers")
def Tinkering_Fingers():
	return render_template("tinkering-fingers.html")

@app.route("/courteous-comeback")
def Courteous_Comeback():
	return render_template("courteous-comeback.html")

@app.route("/elemental-adept")
def Elemental_Adept():
	return render_template("elemental-adept.html")

@app.route("/scalding-spit")
def Scalding_Spit():
	return render_template("scalding-spit.html")

@app.route("/cautious-crawler")
def Cautious_Crawler():
	return render_template("cautious-crawler.html")

@app.route("/hustler")
def Hustler():
	return render_template("hustler.html")

@app.route("/pack-rat")
def Pack_Rat():
	return render_template("pack-rat.html")

@app.route("/warren-navigator")
def Warren_Navigator():
	return render_template("warren-navigator.html")

@app.route("/avoid-notice")
def Avoid_Notice():
	return render_template("avoid-notice.html")

@app.route("/agile")
def Agile():
	return render_template("agile.html")

@app.route("/attached")
def Attached():
	return render_template("attached.html")

@app.route("/backstabber")
def Backstabber():
	return render_template("backstabber.html")

@app.route("/backswing")
def Backswing():
	return render_template("backswing.html")

@app.route("/brutal")
def Brutal():
	return render_template("brutal.html")

@app.route("/climbing")
def Climbing():
	return render_template("climbing.html")

@app.route("/concealable")
def Concealable():
	return render_template("concealable.html")

@app.route("/deadly")
def Deadly():
	return render_template("deadly.html")

@app.route("/disarm-weapon-trait")
def Disarm__weapon_trait_():
	return render_template("disarm-weapon-trait.html")

@app.route("/fatal")
def Fatal():
	return render_template("fatal.html")

@app.route("/finesse")
def Finesse():
	return render_template("finesse.html")

@app.route("/forceful")
def Forceful():
	return render_template("forceful.html")

@app.route("/free-hand")
def Free_Hand():
	return render_template("free-hand.html")

@app.route("/grapple-weapon-trait")
def Grapple__weapon_trait_():
	return render_template("grapple-weapon-trait.html")

@app.route("/hampering")
def Hampering():
	return render_template("hampering.html")

@app.route("/jousting")
def Jousting():
	return render_template("jousting.html")

@app.route("/modular")
def Modular():
	return render_template("modular.html")

@app.route("/nonlethal")
def Nonlethal():
	return render_template("nonlethal.html")

@app.route("/parry")
def Parry():
	return render_template("parry.html")

@app.route("/propulsive")
def Propulsive():
	return render_template("propulsive.html")

@app.route("/range")
def Range():
	return render_template("range.html")

@app.route("/ranged-trip")
def Ranged_Trip():
	return render_template("ranged-trip.html")

@app.route("/reach")
def Reach():
	return render_template("reach.html")

@app.route("/reload")
def Reload():
	return render_template("reload.html")

@app.route("/repeating")
def Repeating():
	return render_template("repeating.html")

@app.route("/shove-3653080")
def Shove():
	return render_template("shove-3653080.html")

@app.route("/sweep")
def Sweep():
	return render_template("sweep.html")

@app.route("/tethered")
def Tethered():
	return render_template("tethered.html")

@app.route("/thrown")
def Thrown():
	return render_template("thrown.html")

@app.route("/trip-weapon-trait")
def Trip__weapon_trait_():
	return render_template("trip-weapon-trait.html")

@app.route("/twin")
def Twin():
	return render_template("twin.html")

@app.route("/two-hand")
def Two_Hand():
	return render_template("two-hand.html")

@app.route("/unarmed")
def Unarmed():
	return render_template("unarmed.html")

@app.route("/versatile")
def Versatile():
	return render_template("versatile.html")

@app.route("/volley")
def Volley():
	return render_template("volley.html")

@app.route("/disarm-resist")
def Disarm_Resist():
	return render_template("disarm-resist.html")

@app.route("/improvisational-defender")
def Improvisational_Defender():
	return render_template("improvisational-defender.html")

@app.route("/razzle-dazzle")
def Razzle_Dazzle():
	return render_template("razzle-dazzle.html")

@app.route("/returning-throw")
def Returning_Throw():
	return render_template("returning-throw.html")

@app.route("/shoulder-slam")
def Shoulder_Slam():
	return render_template("shoulder-slam.html")

@app.route("/agonizing-rebuke")
def Agonizing_Rebuke():
	return render_template("agonizing-rebuke.html")

@app.route("/cultural-specialty")
def Cultural_Specialty():
	return render_template("cultural-specialty.html")

@app.route("/dynamic-linguistics")
def Dynamic_Linguistics():
	return render_template("dynamic-linguistics.html")

@app.route("/extraplanar-study")
def Extraplanar_Study():
	return render_template("extraplanar-study.html")

@app.route("/seer")
def Seer():
	return render_template("seer.html")

@app.route("/know-your-own")
def Know_Your_Own():
	return render_template("know-your-own.html")

@app.route("/adroit-manipulation")
def Adroit_Manipulation():
	return render_template("adroit-manipulation.html")

@app.route("/no-evidence")
def No_Evidence():
	return render_template("no-evidence.html")

@app.route("/silent-step")
def Silent_Step():
	return render_template("silent-step.html")

@app.route("/super-sneaky")
def Super_Sneaky():
	return render_template("super-sneaky.html")

@app.route("/very-sneaky")
def Very_Sneaky():
	return render_template("very-sneaky.html")

@app.route("/adapted-cantrip")
def Adapted_Cantrip():
	return render_template("adapted-cantrip.html")

@app.route("/feed-on-pain")
def Feed_on_Pain():
	return render_template("feed-on-pain.html")

@app.route("/intuitive-illusions")
def Intuitive_Illusions():
	return render_template("intuitive-illusions.html")

@app.route("/magic-rider")
def Magic_Rider():
	return render_template("magic-rider.html")

@app.route("/star-orb")
def Star_Orb():
	return render_template("star-orb.html")

@app.route("/sheltering-slab")
def Sheltering_Slab():
	return render_template("sheltering-slab.html")

@app.route("/stonecunning")
def Stonecunning():
	return render_template("stonecunning.html")

@app.route("/loud-singer")
def Loud_Singer():
	return render_template("loud-singer.html")

@app.route("/mask-of-fear")
def Mask_of_Fear():
	return render_template("mask-of-fear.html")

@app.route("/mask-of-pain")
def Mask_of_Pain():
	return render_template("mask-of-pain.html")

@app.route("/mask-of-rejection")
def Mask_of_Rejection():
	return render_template("mask-of-rejection.html")

@app.route("/clan-protector")
def Clan_Protector():
	return render_template("clan-protector.html")

@app.route("/clans-edge")
def Clans_Edge():
	return render_template("clans-edge.html")

@app.route("/protective-sheath")
def Protective_Sheath():
	return render_template("protective-sheath.html")

@app.route("/titan-slinger")
def Titan_Slinger():
	return render_template("titan-slinger.html")

@app.route("/steady-on-stone")
def Steady_on_Stone():
	return render_template("steady-on-stone.html")

@app.route("/environmental-climber")
def Environmental_Climber():
	return render_template("environmental-climber.html")

@app.route("/superior-environmental-climber")
def Superior_Environmental_Climber():
	return render_template("superior-environmental-climber.html")

@app.route("/cobble-dancer")
def Cobble_Dancer():
	return render_template("cobble-dancer.html")

@app.route("/environment-craft")
def Environment_Craft():
	return render_template("environment-craft.html")

@app.route("/natural-scout")
def Natural_Scout():
	return render_template("natural-scout.html")

@app.route("/swift-stalker")
def Swift_Stalker():
	return render_template("swift-stalker.html")

@app.route("/terrain-runner")
def Terrain_Runner():
	return render_template("terrain-runner.html")

@app.route("/terrain-stalker")
def Terrain_Stalker():
	return render_template("terrain-stalker.html")

@app.route("/wintertouched")
def Wintertouched():
	return render_template("wintertouched.html")

@app.route("/uncanny-agility")
def Uncanny_Agility():
	return render_template("uncanny-agility.html")

@app.route("/animal-class-elocutionist")
def Animal_Class_Elocutionist():
	return render_template("animal-class-elocutionist.html")

@app.route("/true-animal-elocutionist")
def True_Animal_Elocutionist():
	return render_template("true-animal-elocutionist.html")

@app.route("/unsettling-to-animals")
def Unsettling_to_Animals():
	return render_template("unsettling-to-animals.html")

@app.route("/airy-step")
def Airy_Step():
	return render_template("airy-step.html")

@app.route("/blazing-aura")
def Blazing_Aura():
	return render_template("blazing-aura.html")

@app.route("/continuous-assault")
def Continuous_Assault():
	return render_template("continuous-assault.html")

@app.route("/energy-blessed")
def Energy_Blessed():
	return render_template("energy-blessed.html")

@app.route("/harness-shroud")
def Harness_Shroud():
	return render_template("harness-shroud.html")

@app.route("/shroud-cloud")
def Shroud_Cloud():
	return render_template("shroud-cloud.html")

@app.route("/heat-wave")
def Heat_Wave():
	return render_template("heat-wave.html")

@app.route("/hydraulic-deflection")
def Hydraulic_Deflection():
	return render_template("hydraulic-deflection.html")

@app.route("/elemental-maneuvers")
def Elemental_Maneuvers():
	return render_template("elemental-maneuvers.html")

@app.route("/improved-elemental-bulwark")
def Improved_Elemental_Bulwark():
	return render_template("improved-elemental-bulwark.html")

@app.route("/mist-strider")
def Mist_Strider():
	return render_template("mist-strider.html")

@app.route("/radiance")
def Radiance():
	return render_template("radiance.html")

@app.route("/tetraelemental-assault")
def Tetraelemental_Assault():
	return render_template("tetraelemental-assault.html")

@app.route("/cloak-of-poison")
def Cloak_of_Poison():
	return render_template("cloak-of-poison.html")

@app.route("/graceful-step")
def Graceful_Step():
	return render_template("graceful-step.html")

@app.route("/hopping-stride")
def Hopping_Stride():
	return render_template("hopping-stride.html")

@app.route("/light-step")
def Light_Step():
	return render_template("light-step.html")

@app.route("/lower-their-guard")
def Lower_Their_Guard():
	return render_template("lower-their-guard.html")

@app.route("/invigorating-fear")
def Invigorating_Fear():
	return render_template("invigorating-fear.html")

@app.route("/expert-dynamic-skill")
def Expert_Dynamic_Skill():
	return render_template("expert-dynamic-skill.html")

@app.route("/true-dynamic-skill")
def True_Dynamic_Skill():
	return render_template("true-dynamic-skill.html")

@app.route("/universal-dynamic-skill")
def Universal_Dynamic_Skill():
	return render_template("universal-dynamic-skill.html")

@app.route("/eclectic-obsession")
def Eclectic_Obsession():
	return render_template("eclectic-obsession.html")

@app.route("/incredible-improvisation")
def Incredible_Improvisation():
	return render_template("incredible-improvisation.html")

@app.route("/guiding-luck")
def Guiding_Luck():
	return render_template("guiding-luck.html")

@app.route("/harbingers-hex")
def Harbingers_Hex():
	return render_template("harbingers-hex.html")

@app.route("/jinxed")
def Jinxed():
	return render_template("jinxed.html")

@app.route("/lucky-defense")
def Lucky_Defense():
	return render_template("lucky-defense.html")

@app.route("/quick-curse")
def Quick_Curse():
	return render_template("quick-curse.html")

@app.route("/superstition")
def Superstition():
	return render_template("superstition.html")

@app.route("/jinx-glutton")
def Jinx_Glutton():
	return render_template("jinx-glutton.html")

@app.route("/lucky-break")
def Lucky_Break():
	return render_template("lucky-break.html")

@app.route("/sense-for-trouble")
def Sense_for_Trouble():
	return render_template("sense-for-trouble.html")

@app.route("/shared-luck-8064152")
def Shared_Luck():
	return render_template("shared-luck-8064152.html")

@app.route("/tradition-bane")
def Tradition_Bane():
	return render_template("tradition-bane.html")

@app.route("/kneel-for-no-man-or-god")
def Kneel_for_no_Man_or_God():
	return render_template("kneel-for-no-man-or-god.html")

@app.route("/magic-resistance")
def Magic_Resistance():
	return render_template("magic-resistance.html")

@app.route("/speak-with-plants")
def Speak_With_Plants():
	return render_template("speak-with-plants.html")

@app.route("/counteracting")
def Counteracting():
	return render_template("counteracting.html")

@app.route("/purge-sins")
def Purge_Sins():
	return render_template("purge-sins.html")

@app.route("/bright-fletchling")
def Bright_Fletchling():
	return render_template("bright-fletchling.html")

@app.route("/earth-sense")
def Earth_Sense():
	return render_template("earth-sense.html")

@app.route("/search1")
def Search():
	return render_template("search1.html")

@app.route("/spirit-soother")
def Spirit_Soother():
	return render_template("spirit-soother.html")

@app.route("/extinguish-light")
def Extinguish_Light():
	return render_template("extinguish-light.html")

@app.route("/hefting-shadow")
def Hefting_Shadow():
	return render_template("hefting-shadow.html")

@app.route("/sculpt-shadows")
def Sculpt_Shadows():
	return render_template("sculpt-shadows.html")

@app.route("/shadow-blending")
def Shadow_Blending():
	return render_template("shadow-blending.html")

@app.route("/fortuitous-shift")
def Fortuitous_Shift():
	return render_template("fortuitous-shift.html")

@app.route("/life-leap")
def Life_Leap():
	return render_template("life-leap.html")

@app.route("/basic-innate-spell")
def Basic_Innate_Spell():
	return render_template("basic-innate-spell.html")

@app.route("/energized-font")
def Energized_Font():
	return render_template("energized-font.html")

@app.route("/innate-cantrip")
def Innate_Cantrip():
	return render_template("innate-cantrip.html")

@app.route("/fey-touched")
def Fey_Touched():
	return render_template("fey-touched.html")

@app.route("/life-giving-magic")
def Life_Giving_Magic():
	return render_template("life-giving-magic.html")

@app.route("/expert-innate-spell")
def Expert_Innate_Spell():
	return render_template("expert-innate-spell.html")

@app.route("/otherworldly-acumen")
def Otherworldly_Acumen():
	return render_template("otherworldly-acumen.html")

@app.route("/charred-remains")
def Charred_Remains():
	return render_template("charred-remains.html")

@app.route("/steam-spell")
def Steam_Spell():
	return render_template("steam-spell.html")

@app.route("/twist-healing")
def Twist_Healing():
	return render_template("twist-healing.html")

@app.route("/echoes-in-stone")
def Echoes_in_Stone():
	return render_template("echoes-in-stone.html")

@app.route("/treacherous-earth")
def Treacherous_Earth():
	return render_template("treacherous-earth.html")

@app.route("/long-lived")
def Long_Lived():
	return render_template("long-lived.html")

@app.route("/hybrid-form")
def Hybrid_Form():
	return render_template("hybrid-form.html")

@app.route("/myriad-forms")
def Myriad_Forms():
	return render_template("myriad-forms.html")

@app.route("/quick-shape")
def Quick_Shape():
	return render_template("quick-shape.html")

@app.route("/ankle-bite")
def Ankle_Bite():
	return render_template("ankle-bite.html")

@app.route("/fang-sharpener")
def Fang_Sharpener():
	return render_template("fang-sharpener.html")

@app.route("/bloodletting-fangs")
def Bloodletting_Fangs():
	return render_template("bloodletting-fangs.html")

@app.route("/envenom-fangs")
def Envenom_Fangs():
	return render_template("envenom-fangs.html")

@app.route("/gnaw")
def Gnaw():
	return render_template("gnaw.html")

@app.route("/hungry")
def Hungry():
	return render_template("hungry.html")

@app.route("/sawtooth")
def Sawtooth():
	return render_template("sawtooth.html")

@app.route("/sharp-fangs")
def Sharp_Fangs():
	return render_template("sharp-fangs.html")

@app.route("/swinging-bite")
def Swinging_Bite():
	return render_template("swinging-bite.html")

@app.route("/taste-blood")
def Taste_Blood():
	return render_template("taste-blood.html")

@app.route("/cheek-pouches")
def Cheek_Pouches():
	return render_template("cheek-pouches.html")

@app.route("/big-mouth")
def Big_Mouth():
	return render_template("big-mouth.html")

@app.route("/quick-stow")
def Quick_Stow():
	return render_template("quick-stow.html")

@app.route("/daywalker")
def Daywalker():
	return render_template("daywalker.html")

@app.route("/defy-death")
def Defy_Death():
	return render_template("defy-death.html")

@app.route("/focused-cat-nap")
def Focused_Cat_Nap():
	return render_template("focused-cat-nap.html")

@app.route("/healers-halo")
def Healers_Halo():
	return render_template("healers-halo.html")

@app.route("/ten-lives")
def Ten_Lives():
	return render_template("ten-lives.html")

@app.route("/springing-leaper")
def Springing_Leaper():
	return render_template("springing-leaper.html")

@app.route("/fleet-footed")
def Fleet_Footed():
	return render_template("fleet-footed.html")

@app.route("/lotus-style")
def Lotus_Style():
	return render_template("lotus-style.html")

@app.route("/warren-digger")
def Warren_Digger():
	return render_template("warren-digger.html")

@app.route("/bioluminescent")
def Bioluminescent():
	return render_template("bioluminescent.html")

@app.route("/keen-eyes")
def Keen_Eyes():
	return render_template("keen-eyes.html")

@app.route("/cindersoul")
def Cindersoul():
	return render_template("cindersoul.html")

@app.route("/cleansing-blood")
def Cleansing_Blood():
	return render_template("cleansing-blood.html")

@app.route("/duskwalker")
def Duskwalker():
	return render_template("duskwalker.html")

@app.route("/emberkin")
def Emberkin():
	return render_template("emberkin.html")

@app.route("/graveborn")
def Graveborn():
	return render_template("graveborn.html")

@app.route("/inoculating-blood")
def Inoculating_Blood():
	return render_template("inoculating-blood.html")

@app.route("/intercorporate")
def Intercorporate():
	return render_template("intercorporate.html")

@app.route("/necromantic-physiology")
def Necromantic_Physiology():
	return render_template("necromantic-physiology.html")

@app.route("/powerful-guts")
def Powerful_Guts():
	return render_template("powerful-guts.html")

@app.route("/resist-sleep")
def Resist_Sleep():
	return render_template("resist-sleep.html")

@app.route("/rooted")
def Rooted():
	return render_template("rooted.html")

@app.route("/scar-thick-skin")
def Scar_Thick_Skin():
	return render_template("scar-thick-skin.html")

@app.route("/steady-guts")
def Steady_Guts():
	return render_template("steady-guts.html")

@app.route("/steelskin")
def Steelskin():
	return render_template("steelskin.html")

@app.route("/stormtossed")
def Stormtossed():
	return render_template("stormtossed.html")

@app.route("/unfettered")
def Unfettered():
	return render_template("unfettered.html")

@app.route("/vigorous-health")
def Vigorous_Health():
	return render_template("vigorous-health.html")

@app.route("/vivacious")
def Vivacious():
	return render_template("vivacious.html")

@app.route("/well-groomed")
def Well_Groomed():
	return render_template("well-groomed.html")

@app.route("/wind-tempered")
def Wind_Tempered():
	return render_template("wind-tempered.html")

@app.route("/seedpod")
def Seedpod():
	return render_template("seedpod.html")

@app.route("/thorned-seedpod")
def Thorned_Seedpod():
	return render_template("thorned-seedpod.html")

@app.route("/hear-the-heartbeat")
def Hear_the_Heartbeat():
	return render_template("hear-the-heartbeat.html")

@app.route("/lifesense")
def Lifesense():
	return render_template("lifesense.html")

@app.route("/low-light-vision")
def Low_Light_Vision():
	return render_template("low-light-vision.html")

@app.route("/plague-sense")
def Plague_Sense():
	return render_template("plague-sense.html")

@app.route("/tactile-oceaner")
def Tactile_Oceaner():
	return render_template("tactile-oceaner.html")

@app.route("/uncanny-awareness")
def Uncanny_Awareness():
	return render_template("uncanny-awareness.html")

@app.route("/step-lively")
def Step_Lively():
	return render_template("step-lively.html")

@app.route("/shinstabber")
def Shinstabber():
	return render_template("shinstabber.html")

@app.route("/toppling-dance")
def Toppling_Dance():
	return render_template("toppling-dance.html")

@app.route("/tough-tumbler")
def Tough_Tumbler():
	return render_template("tough-tumbler.html")

@app.route("/mist-child")
def Mist_Child():
	return render_template("mist-child.html")

@app.route("/veil-skin")
def Veil_Skin():
	return render_template("veil-skin.html")

@app.route("/spines")
def Spines():
	return render_template("spines.html")

@app.route("/toxic-spines")
def Toxic_Spines():
	return render_template("toxic-spines.html")

@app.route("/spore-cloud")
def Spore_Cloud():
	return render_template("spore-cloud.html")

@app.route("/eerie-compression")
def Eerie_Compression():
	return render_template("eerie-compression.html")

@app.route("/flexible")
def Flexible():
	return render_template("flexible.html")

@app.route("/lightless-litheness")
def Lightless_Litheness():
	return render_template("lightless-litheness.html")

@app.route("/smushy")
def Smushy():
	return render_template("smushy.html")

@app.route("/drowning-and-suffocation")
def Drowning_and_Suffocation():
	return render_template("drowning-and-suffocation.html")

@app.route("/internal-respirator")
def Internal_Respirator():
	return render_template("internal-respirator.html")

@app.route("/irongut")
def Irongut():
	return render_template("irongut.html")

@app.route("/starvation-and-thirst")
def Starvation_and_Thirst():
	return render_template("starvation-and-thirst.html")

@app.route("/parthenogenic")
def Parthenogenic():
	return render_template("parthenogenic.html")

@app.route("/root-feeder")
def Root_Feeder():
	return render_template("root-feeder.html")

@app.route("/dust-soul")
def Dust_Soul():
	return render_template("dust-soul.html")

@app.route("/long-marcher")
def Long_Marcher():
	return render_template("long-marcher.html")

@app.route("/tongue-disarm")
def Tongue_Disarm():
	return render_template("tongue-disarm.html")

@app.route("/control-fall")
def Control_Fall():
	return render_template("control-fall.html")

@app.route("/true-breakfall")
def True_Breakfall():
	return render_template("true-breakfall.html")

@app.route("/dangle")
def Dangle():
	return render_template("dangle.html")

@app.route("/hard-appendage")
def Hard_Appendage():
	return render_template("hard-appendage.html")

@app.route("/larcenous-appendage")
def Larcenous_Appendage():
	return render_template("larcenous-appendage.html")

@app.route("/shed-appendage")
def Shed_Appendage():
	return render_template("shed-appendage.html")

@app.route("/mischievous-appendage")
def Mischievous_Appendage():
	return render_template("mischievous-appendage.html")

@app.route("/soaring-flight")
def Soaring_Flight():
	return render_template("soaring-flight.html")

@app.route("/limited-flight")
def Limited_Flight():
	return render_template("limited-flight.html")

@app.route("/glide")
def Glide():
	return render_template("glide.html")

@app.route("/wing-cloak")
def Wing_Cloak():
	return render_template("wing-cloak.html")

@app.route("/aquatic-combat")
def Aquatic_Combat():
	return render_template("aquatic-combat.html")

@app.route("/aquatic-camouflage")
def Aquatic_Camouflage():
	return render_template("aquatic-camouflage.html")

@app.route("/deep-diver")
def Deep_Diver():
	return render_template("deep-diver.html")

@app.route("/perfect-dive")
def Perfect_Dive():
	return render_template("perfect-dive.html")

@app.route("/perfect-lungs")
def Perfect_Lungs():
	return render_template("perfect-lungs.html")

@app.route("/water-diver")
def Water_Diver():
	return render_template("water-diver.html")

@app.route("/water-piercer")
def Water_Piercer():
	return render_template("water-piercer.html")

@app.route("/brine-born")
def Brine_born():
	return render_template("brine-born.html")

@app.route("/venomous")
def Venomous():
	return render_template("venomous.html")

@app.route("/fae-killer")
def Fae_Killer():
	return render_template("fae-killer.html")

@app.route("/lycanthrope-killer")
def Lycanthrope_Killer():
	return render_template("lycanthrope-killer.html")

@app.route("/spiteful-rake")
def Spiteful_Rake():
	return render_template("spiteful-rake.html")

@app.route("/natural-climbing")
def Natural_Climbing():
	return render_template("natural-climbing.html")

@app.route("/alter-resistance")
def Alter_Resistance():
	return render_template("alter-resistance.html")

@app.route("/freeze-it")
def Freeze_It():
	return render_template("freeze-it.html")

@app.route("/slip-the-grasp")
def Slip_the_Grasp():
	return render_template("slip-the-grasp.html")

@app.route("/sickening-counter")
def Sickening_Counter():
	return render_template("sickening-counter.html")

@app.route("/quadro")
def Quadro():
	return render_template("quadro.html")

@app.route("/preemptive-configuration")
def Preemptive_Configuration():
	return render_template("preemptive-configuration.html")

@app.route("/roll-with-it")
def Roll_With_It():
	return render_template("roll-with-it.html")

@app.route("/chameleon")
def Chameleon():
	return render_template("chameleon.html")

@app.route("/ferocious-beasts")
def Ferocious_Beasts():
	return render_template("ferocious-beasts.html")

@app.route("/natural-climber")
def Natural_Climber():
	return render_template("natural-climber.html")

@app.route("/allys-shelter")
def Allys_Shelter():
	return render_template("allys-shelter.html")

@app.route("/cooperative-nature")
def Cooperative_Nature():
	return render_template("cooperative-nature.html")

@app.route("/cooperative-soul")
def Cooperative_Soul():
	return render_template("cooperative-soul.html")

@app.route("/group-aid")
def Group_Aid():
	return render_template("group-aid.html")

@app.route("/ghost-strike")
def Ghost_Strike():
	return render_template("ghost-strike.html")

@app.route("/extreme-shared-luck")
def Extreme_Shared_Luck():
	return render_template("extreme-shared-luck.html")

@app.route("/light-adjustment")
def Light_Adjustment():
	return render_template("light-adjustment.html")

@app.route("/heartened-vivacity")
def Heartened_Vivacity():
	return render_template("heartened-vivacity.html")

@app.route("/hard-to-fool")
def Hard_to_Fool():
	return render_template("hard-to-fool.html")

@app.route("/finest-trick")
def Finest_Trick():
	return render_template("finest-trick.html")

@app.route("/distracting-shadows")
def Distracting_Shadows():
	return render_template("distracting-shadows.html")

@app.route("/appendage-spin")
def Appendage_Spin():
	return render_template("appendage-spin.html")

@app.route("/steady-balance")
def Steady_Balance():
	return render_template("steady-balance.html")

@app.route("/nimble-crawl")
def Nimble_Crawl():
	return render_template("nimble-crawl.html")

@app.route("/masterful-crawl")
def Masterful_Crawl():
	return render_template("masterful-crawl.html")

@app.route("/contortionist")
def Contortionist():
	return render_template("contortionist.html")

@app.route("/cat-fall")
def Cat_Fall():
	return render_template("cat-fall.html")

@app.route("/masterful-cat-fall")
def Masterful_Cat_Fall():
	return render_template("masterful-cat-fall.html")

@app.route("/legendary-catfall")
def Legendary_Catfall():
	return render_template("legendary-catfall.html")

@app.route("/aerobatic-mastery")
def Aerobatic_Mastery():
	return render_template("aerobatic-mastery.html")

@app.route("/acrobatic-performer")
def Acrobatic_Performer():
	return render_template("acrobatic-performer.html")

@app.route("/prone-fighter")
def Prone_Fighter():
	return render_template("prone-fighter.html")

@app.route("/quick-squeeze")
def Quick_Squeeze():
	return render_template("quick-squeeze.html")

@app.route("/legendary-squeeze")
def Legendary_Squeeze():
	return render_template("legendary-squeeze.html")

@app.route("/kip-up")
def Kip_Up():
	return render_template("kip-up.html")

@app.route("/shake-it-up")
def Shake_it_Up():
	return render_template("shake-it-up.html")

@app.route("/acrobat-dedication")
def Acrobat_Dedication():
	return render_template("acrobat-dedication.html")

@app.route("/tumble-behind")
def Tumble_Behind():
	return render_template("tumble-behind.html")

@app.route("/travel-domain-travelers-transit")
def Travel_Domain__Travelers_Transit():
	return render_template("travel-domain-travelers-transit.html")

@app.route("/impressive-landing")
def Impressive_Landing():
	return render_template("impressive-landing.html")

@app.route("/graceful-landing")
def Graceful_Landing():
	return render_template("graceful-landing.html")

@app.route("/water-step")
def Water_Step():
	return render_template("water-step.html")

@app.route("/cloud-walk")
def Cloud_Walk():
	return render_template("cloud-walk.html")

@app.route("/implausible-infiltration")
def Implausible_Infiltration():
	return render_template("implausible-infiltration.html")

@app.route("/travel-domain-agile-feet")
def Travel_Domain__Agile_Feet():
	return render_template("travel-domain-agile-feet.html")

@app.route("/freedom-domain-unimpeded-stride")
def Freedom_Domain__Unimpeded_Stride():
	return render_template("freedom-domain-unimpeded-stride.html")

@app.route("/freedom-domain-word-of-freedom")
def Freedom_Domain__Word_of_Freedom():
	return render_template("freedom-domain-word-of-freedom.html")

@app.route("/dodging-roll")
def Dodging_Roll():
	return render_template("dodging-roll.html")

@app.route("/tumbling-strike")
def Tumbling_Strike():
	return render_template("tumbling-strike.html")

@app.route("/acrobatic-dodge")
def Acrobatic_Dodge():
	return render_template("acrobatic-dodge.html")

@app.route("/defensive-roll")
def Defensive_Roll():
	return render_template("defensive-roll.html")

@app.route("/graceful-leaper")
def Graceful_Leaper():
	return render_template("graceful-leaper.html")

@app.route("/dancing-leaf")
def Dancing_Leaf():
	return render_template("dancing-leaf.html")

@app.route("/additive")
def Additive():
	return render_template("additive.html")

@app.route("/exploitive-bomb")
def Exploitive_Bomb():
	return render_template("exploitive-bomb.html")

@app.route("/astonishing-explosive")
def Astonishing_Explosive():
	return render_template("astonishing-explosive.html")

@app.route("/perpetual-bomber")
def Perpetual_Bomber():
	return render_template("perpetual-bomber.html")

@app.route("/splash")
def Splash():
	return render_template("splash.html")

@app.route("/demolition-charge")
def Demolition_Charge():
	return render_template("demolition-charge.html")

@app.route("/greater-bomb-discovery")
def Greater_Bomb_Discovery():
	return render_template("greater-bomb-discovery.html")

@app.route("/bomb-making-prodigy")
def Bomb_Making_Prodigy():
	return render_template("bomb-making-prodigy.html")

@app.route("/directional-bomb")
def Directional_Bomb():
	return render_template("directional-bomb.html")

@app.route("/mega-bomb")
def Mega_Bomb():
	return render_template("mega-bomb.html")

@app.route("/perfect-debilitation")
def Perfect_Debilitation():
	return render_template("perfect-debilitation.html")

@app.route("/quick-bomber")
def Quick_Bomber():
	return render_template("quick-bomber.html")

@app.route("/smoke-bomb")
def Smoke_Bomb():
	return render_template("smoke-bomb.html")

@app.route("/sticky-bomb")
def Sticky_Bomb():
	return render_template("sticky-bomb.html")

@app.route("/true-debilitating-bomb")
def True_Debilitating_Bomb():
	return render_template("true-debilitating-bomb.html")

@app.route("/greater-debilitating-bomb")
def Greater_Debilitating_Bomb():
	return render_template("greater-debilitating-bomb.html")

@app.route("/uncanny-bombs")
def Uncanny_Bombs():
	return render_template("uncanny-bombs.html")

@app.route("/golem-grafter")
def Golem_Grafter():
	return render_template("golem-grafter.html")

@app.route("/accursed-fist")
def Accursed_Fist():
	return render_template("accursed-fist.html")

@app.route("/iron-lung")
def Iron_Lung():
	return render_template("iron-lung.html")

@app.route("/legs-of-stone")
def Legs_of_Stone():
	return render_template("legs-of-stone.html")

@app.route("/quicken-heartbeat")
def Quicken_Heartbeat():
	return render_template("quicken-heartbeat.html")

@app.route("/healing-bomb")
def Healing_Bomb():
	return render_template("healing-bomb.html")

@app.route("/greater-merciful-elixir")
def Greater_Merciful_Elixir():
	return render_template("greater-merciful-elixir.html")

@app.route("/surgical-prodigy")
def Surgical_Prodigy():
	return render_template("surgical-prodigy.html")

@app.route("/supreme-surgical-prodigy")
def Supreme_Surgical_Prodigy():
	return render_template("supreme-surgical-prodigy.html")

@app.route("/alchemical-alacrity")
def Alchemical_Alacrity():
	return render_template("alchemical-alacrity.html")

@app.route("/efficient-alchemy")
def Efficient_Alchemy():
	return render_template("efficient-alchemy.html")

@app.route("/enduring-alchemy")
def Enduring_Alchemy():
	return render_template("enduring-alchemy.html")

@app.route("/unstable-concoction")
def Unstable_Concoction():
	return render_template("unstable-concoction.html")

@app.route("/feral-mutagen")
def Feral_Mutagen():
	return render_template("feral-mutagen.html")

@app.route("/mutagen-prodigy")
def Mutagen_Prodigy():
	return render_template("mutagen-prodigy.html")

@app.route("/perpetual-mutagenist")
def Perpetual_Mutagenist():
	return render_template("perpetual-mutagenist.html")

@app.route("/shaped-contaminant")
def Shaped_Contaminant():
	return render_template("shaped-contaminant.html")

@app.route("/improved-poison-weapon")
def Improved_Poison_Weapon():
	return render_template("improved-poison-weapon.html")

@app.route("/deadly-weapon-poison")
def Deadly_Weapon_Poison():
	return render_template("deadly-weapon-poison.html")

@app.route("/poison-coat")
def Poison_Coat():
	return render_template("poison-coat.html")

@app.route("/poisoners-twist")
def Poisoners_Twist():
	return render_template("poisoners-twist.html")

@app.route("/perpetual-toxicologist")
def Perpetual_Toxicologist():
	return render_template("perpetual-toxicologist.html")

@app.route("/toxicology-prodigy")
def Toxicology_Prodigy():
	return render_template("toxicology-prodigy.html")

@app.route("/toxicological-discovery")
def Toxicological_Discovery():
	return render_template("toxicological-discovery.html")

@app.route("/eternal-elixir")
def Eternal_Elixir():
	return render_template("eternal-elixir.html")

@app.route("/crystal-keeper")
def Crystal_Keeper():
	return render_template("crystal-keeper.html")

@app.route("/strange-script")
def Strange_Script():
	return render_template("strange-script.html")

@app.route("/unravel-mysteries")
def Unravel_Mysteries():
	return render_template("unravel-mysteries.html")

@app.route("/assured-identification")
def Assured_Identification():
	return render_template("assured-identification.html")

@app.route("/quick-identify")
def Quick_Identify():
	return render_template("quick-identify.html")

@app.route("/recognize-spell")
def Recognize_Spell():
	return render_template("recognize-spell.html")

@app.route("/quick-recognition")
def Quick_Recognition():
	return render_template("quick-recognition.html")

@app.route("/spellmaster")
def Spellmaster():
	return render_template("spellmaster.html")

@app.route("/loaner-spell")
def Loaner_Spell():
	return render_template("loaner-spell.html")

@app.route("/timeless-body")
def Timeless_Body():
	return render_template("timeless-body.html")

@app.route("/bardic-lore")
def Bardic_Lore():
	return render_template("bardic-lore.html")

@app.route("/assured-knowledge")
def Assured_Knowledge():
	return render_template("assured-knowledge.html")

@app.route("/automatic-knowledge")
def Automatic_Knowledge():
	return render_template("automatic-knowledge.html")

@app.route("/bestiary-scholar")
def Bestiary_Scholar():
	return render_template("bestiary-scholar.html")

@app.route("/combat-assessment")
def Combat_Assessment():
	return render_template("combat-assessment.html")

@app.route("/diverse-recognition")
def Diverse_Recognition():
	return render_template("diverse-recognition.html")

@app.route("/dubious-knowledge")
def Dubious_Knowledge():
	return render_template("dubious-knowledge.html")

@app.route("/enigmas-knowledge")
def Enigmas_Knowledge():
	return render_template("enigmas-knowledge.html")

@app.route("/innate-magic-intuition")
def Innate_Magic_Intuition():
	return render_template("innate-magic-intuition.html")

@app.route("/masterful-obfuscation")
def Masterful_Obfuscation():
	return render_template("masterful-obfuscation.html")

@app.route("/knowledge-domain-scholarly-recollection")
def Knowledge_Domain__Scholarly_Recollection():
	return render_template("knowledge-domain-scholarly-recollection.html")

@app.route("/knowledge-domain-know-the-enemy")
def Knowledge_Domain__Know_the_Enemy():
	return render_template("knowledge-domain-know-the-enemy.html")

@app.route("/mastermind")
def Mastermind():
	return render_template("mastermind.html")

@app.route("/clever-gambit")
def Clever_Gambit():
	return render_template("clever-gambit.html")

@app.route("/reason-rapidly")
def Reason_Rapidly():
	return render_template("reason-rapidly.html")

@app.route("/recognize-threat")
def Recognize_Threat():
	return render_template("recognize-threat.html")

@app.route("/recollect-studies")
def Recollect_Studies():
	return render_template("recollect-studies.html")

@app.route("/remember-your-training")
def Remember_your_Training():
	return render_template("remember-your-training.html")

@app.route("/storytelling")
def Storytelling():
	return render_template("storytelling.html")

@app.route("/storytelling-recollection")
def Storytelling_Recollection():
	return render_template("storytelling-recollection.html")

@app.route("/storytelling-lessons")
def Storytelling_Lessons():
	return render_template("storytelling-lessons.html")

@app.route("/thorough-reports")
def Thorough_Reports():
	return render_template("thorough-reports.html")

@app.route("/discerning-strike")
def Discerning_Strike():
	return render_template("discerning-strike.html")

@app.route("/thorough-research")
def Thorough_Research():
	return render_template("thorough-research.html")

@app.route("/just-the-facts")
def Just_the_Facts():
	return render_template("just-the-facts.html")

@app.route("/know-what-you-know")
def Know_What_You_Know():
	return render_template("know-what-you-know.html")

@app.route("/cheat-death")
def Cheat_Death():
	return render_template("cheat-death.html")

@app.route("/spellmasters-resilience")
def Spellmasters_Resilience():
	return render_template("spellmasters-resilience.html")

@app.route("/spellmasters-tenacity")
def Spellmasters_Tenacity():
	return render_template("spellmasters-tenacity.html")

@app.route("/trick-magic-item")
def Trick_Magic_Item():
	return render_template("trick-magic-item.html")

@app.route("/scroll-trickster")
def Scroll_Trickster():
	return render_template("scroll-trickster.html")

@app.route("/foolproof-instructions")
def Foolproof_Instructions():
	return render_template("foolproof-instructions.html")

@app.route("/scroll-cache")
def Scroll_Cache():
	return render_template("scroll-cache.html")

@app.route("/skim-scroll")
def Skim_Scroll():
	return render_template("skim-scroll.html")

@app.route("/hunters-luck")
def Hunters_Luck():
	return render_template("hunters-luck.html")

@app.route("/draconic-bloodline-dragon-claws")
def Draconic_Bloodline__Dragon_Claws():
	return render_template("draconic-bloodline-dragon-claws.html")

@app.route("/draconic-bloodline-dragon-breath")
def Draconic_Bloodline__Dragon_Breath():
	return render_template("draconic-bloodline-dragon-breath.html")

@app.route("/draconic-bloodline-dragon-wings")
def Draconic_Bloodline__Dragon_Wings():
	return render_template("draconic-bloodline-dragon-wings.html")

@app.route("/fey-bloodline-genies-veil")
def Fey_Bloodline__Genies_Veil():
	return render_template("fey-bloodline-genies-veil.html")

@app.route("/fey-bloodline-hearts-desire")
def Fey_Bloodline__Hearts_Desire():
	return render_template("fey-bloodline-hearts-desire.html")

@app.route("/fey-bloodline-wish-twisted-form")
def Fey_Bloodline__Wish_Twisted_Form():
	return render_template("fey-bloodline-wish-twisted-form.html")

@app.route("/imperial-bloodline-extend-spell")
def Imperial_Bloodline__Extend_Spell():
	return render_template("imperial-bloodline-extend-spell.html")

@app.route("/imperial-bloodline-arcane-countermeasures")
def Imperial_Bloodline__Arcane_Countermeasures():
	return render_template("imperial-bloodline-arcane-countermeasures.html")

@app.route("/imperial-bloodline-ancestral-memories")
def Imperial_Bloodline__Ancestral_Memories():
	return render_template("imperial-bloodline-ancestral-memories.html")

@app.route("/change-domain-adapt-self")
def Change_Domain__Adapt_Self():
	return render_template("change-domain-adapt-self.html")

@app.route("/change-domain-adaptive-ablation")
def Change_Domain__Adaptive_Ablation():
	return render_template("change-domain-adaptive-ablation.html")

@app.route("/glyph-domain-ghostly-transcription")
def Glyph_Domain__Ghostly_Transcription():
	return render_template("glyph-domain-ghostly-transcription.html")

@app.route("/glyph-domain-redact")
def Glyph_Domain__Redact():
	return render_template("glyph-domain-redact.html")

@app.route("/magic-domain-magics-vessel")
def Magic_Domain__Magics_Vessel():
	return render_template("magic-domain-magics-vessel.html")

@app.route("/time-domain-delay-consequence")
def Time_Domain__Delay_Consequence():
	return render_template("time-domain-delay-consequence.html")

@app.route("/time-domain-stasis")
def Time_Domain__Stasis():
	return render_template("time-domain-stasis.html")

@app.route("/wyrmkin-domain-draconic-barrage")
def Wyrmkin_Domain__Draconic_Barrage():
	return render_template("wyrmkin-domain-draconic-barrage.html")

@app.route("/wyrmkin-domain-roar-of-the-wyrm")
def Wyrmkin_Domain__Roar_of_the_Wyrm():
	return render_template("wyrmkin-domain-roar-of-the-wyrm.html")

@app.route("/dragon-disciple")
def Dragon_Disciple():
	return render_template("dragon-disciple.html")

@app.route("/claws-of-the-dragon")
def Claws_of_the_Dragon():
	return render_template("claws-of-the-dragon.html")

@app.route("/draconic-scent")
def Draconic_Scent():
	return render_template("draconic-scent.html")

@app.route("/scales-of-the-dragon")
def Scales_of_the_Dragon():
	return render_template("scales-of-the-dragon.html")

@app.route("/crystal-keeper-focus")
def Crystal_Keeper_Focus():
	return render_template("crystal-keeper-focus.html")

@app.route("/glyph-expert")
def Glyph_Expert():
	return render_template("glyph-expert.html")

@app.route("/unified-theory")
def Unified_Theory():
	return render_template("unified-theory.html")

@app.route("/spellmasters-ward")
def Spellmasters_Ward():
	return render_template("spellmasters-ward.html")

@app.route("/augment-summoning")
def Augment_Summoning():
	return render_template("augment-summoning.html")

@app.route("/call-of-the-grave")
def Call_of_the_Grave():
	return render_template("call-of-the-grave.html")

@app.route("/charming-words")
def Charming_Words():
	return render_template("charming-words.html")

@app.route("/dimensional-steps")
def Dimensional_Steps():
	return render_template("dimensional-steps.html")

@app.route("/diviners-sight")
def Diviners_Sight():
	return render_template("diviners-sight.html")

@app.route("/dread-aura")
def Dread_Aura():
	return render_template("dread-aura.html")

@app.route("/protective-ward")
def Protective_Ward():
	return render_template("protective-ward.html")

@app.route("/energy-absorption")
def Energy_Absorption():
	return render_template("energy-absorption.html")

@app.route("/hand-of-the-apprentice")
def Hand_of_the_Apprentice():
	return render_template("hand-of-the-apprentice.html")

@app.route("/warped-terrain")
def Warped_Terrain():
	return render_template("warped-terrain.html")

@app.route("/physical-boost")
def Physical_Boost():
	return render_template("physical-boost.html")

@app.route("/shifting-form")
def Shifting_Form():
	return render_template("shifting-form.html")

@app.route("/universal-versatility")
def Universal_Versatility():
	return render_template("universal-versatility.html")

@app.route("/vigilant-eye")
def Vigilant_Eye():
	return render_template("vigilant-eye.html")

@app.route("/magic-sense")
def Magic_Sense():
	return render_template("magic-sense.html")

@app.route("/combat-climber")
def Combat_Climber():
	return render_template("combat-climber.html")

@app.route("/impossible-climber")
def Impossible_Climber():
	return render_template("impossible-climber.html")

@app.route("/follow-the-expert")
def Follow_the_Expert():
	return render_template("follow-the-expert.html")

@app.route("/lead-climber")
def Lead_Climber():
	return render_template("lead-climber.html")

@app.route("/quick-climber")
def Quick_Climber():
	return render_template("quick-climber.html")

@app.route("/rapid-mantel")
def Rapid_Mantel():
	return render_template("rapid-mantel.html")

@app.route("/wall-jump")
def Wall_Jump():
	return render_template("wall-jump.html")

@app.route("/titan-wrestler")
def Titan_Wrestler():
	return render_template("titan-wrestler.html")

@app.route("/might-domain-enduring-might")
def Might_Domain__Enduring_Might():
	return render_template("might-domain-enduring-might.html")

@app.route("/might-domain-athletic-rush")
def Might_Domain__Athletic_Rush():
	return render_template("might-domain-athletic-rush.html")

@app.route("/cloud-jump")
def Cloud_Jump():
	return render_template("cloud-jump.html")

@app.route("/powerful-leap")
def Powerful_Leap():
	return render_template("powerful-leap.html")

@app.route("/quick-jump")
def Quick_Jump():
	return render_template("quick-jump.html")

@app.route("/forced-entry")
def Forced_Entry():
	return render_template("forced-entry.html")

@app.route("/adrenaline-rush")
def Adrenaline_Rush():
	return render_template("adrenaline-rush.html")

@app.route("/bashing-charge")
def Bashing_Charge():
	return render_template("bashing-charge.html")

@app.route("/hefty-hauler")
def Hefty_Hauler():
	return render_template("hefty-hauler.html")

@app.route("/incredible-movement")
def Incredible_Movement():
	return render_template("incredible-movement.html")

@app.route("/water-sprint")
def Water_Sprint():
	return render_template("water-sprint.html")

@app.route("/wall-run")
def Wall_Run():
	return render_template("wall-run.html")

@app.route("/breath-control")
def Breath_Control():
	return render_template("breath-control.html")

@app.route("/impossible-swimmer")
def Impossible_Swimmer():
	return render_template("impossible-swimmer.html")

@app.route("/quick-swim")
def Quick_Swim():
	return render_template("quick-swim.html")

@app.route("/underwater-marauder")
def Underwater_Marauder():
	return render_template("underwater-marauder.html")

@app.route("/pick-up-the-pace")
def Pick_Up_the_Pace():
	return render_template("pick-up-the-pace.html")

@app.route("/caravan-leader")
def Caravan_Leader():
	return render_template("caravan-leader.html")

@app.route("/friendly-toss")
def Friendly_Toss():
	return render_template("friendly-toss.html")

@app.route("/sticky-poison")
def Sticky_Poison():
	return render_template("sticky-poison.html")

@app.route("/alchemical-crafter-efficiency")
def Alchemical_Crafter_Efficiency():
	return render_template("alchemical-crafter-efficiency.html")

@app.route("/tweak-appearances")
def Tweak_Appearances():
	return render_template("tweak-appearances.html")

@app.route("/bless-tonic")
def Bless_Tonic():
	return render_template("bless-tonic.html")

@app.route("/bless-toxin")
def Bless_Toxin():
	return render_template("bless-toxin.html")

@app.route("/rapid-affixture")
def Rapid_Affixture():
	return render_template("rapid-affixture.html")

@app.route("/seasoned")
def Seasoned():
	return render_template("seasoned.html")

@app.route("/specialty-crafting")
def Specialty_Crafting():
	return render_template("specialty-crafting.html")

@app.route("/impeccable-crafting")
def Impeccable_Crafting():
	return render_template("impeccable-crafting.html")

@app.route("/creation-domain-artistic-flourish")
def Creation_Domain__Artistic_Flourish():
	return render_template("creation-domain-artistic-flourish.html")

@app.route("/creation-domain-splash-of-art")
def Creation_Domain__Splash_of_Art():
	return render_template("creation-domain-splash-of-art.html")

@app.route("/indulgence-domain-overstuff")
def Indulgence_Domain__Overstuff():
	return render_template("indulgence-domain-overstuff.html")

@app.route("/indulgence-domain-take-its-course")
def Indulgence_Domain__Take_Its_Course():
	return render_template("indulgence-domain-take-its-course.html")

@app.route("/reverse-engineering")
def Reverse_Engineering():
	return render_template("reverse-engineering.html")

@app.route("/alchemical-savant")
def Alchemical_Savant():
	return render_template("alchemical-savant.html")

@app.route("/stone-blood")
def Stone_Blood():
	return render_template("stone-blood.html")

@app.route("/fortified-flesh")
def Fortified_Flesh():
	return render_template("fortified-flesh.html")

@app.route("/improvised-crafting")
def Improvised_Crafting():
	return render_template("improvised-crafting.html")

@app.route("/shoddy")
def Shoddy():
	return render_template("shoddy.html")

@app.route("/quick-repair")
def Quick_Repair():
	return render_template("quick-repair.html")

@app.route("/craft-facsimile")
def Craft_Facsimile():
	return render_template("craft-facsimile.html")

@app.route("/scrounger")
def Scrounger():
	return render_template("scrounger.html")

@app.route("/high-quality-scrounging")
def High_Quality_Scrounging():
	return render_template("high-quality-scrounging.html")

@app.route("/signifier-mask")
def Signifier_Mask():
	return render_template("signifier-mask.html")

@app.route("/masked-casting")
def Masked_Casting():
	return render_template("masked-casting.html")

@app.route("/signifiers-sight")
def Signifiers_Sight():
	return render_template("signifiers-sight.html")

@app.route("/expert-disassembler")
def Expert_Disassembler():
	return render_template("expert-disassembler.html")

@app.route("/giant-snare")
def Giant_Snare():
	return render_template("giant-snare.html")

@app.route("/quick-snares")
def Quick_Snares():
	return render_template("quick-snares.html")

@app.route("/lightning-snares")
def Lightning_Snares():
	return render_template("lightning-snares.html")

@app.route("/remote-trigger")
def Remote_Trigger():
	return render_template("remote-trigger.html")

@app.route("/snare-hopping")
def Snare_Hopping():
	return render_template("snare-hopping.html")

@app.route("/surprise-snare")
def Surprise_Snare():
	return render_template("surprise-snare.html")

@app.route("/ubiquitous-snares")
def Ubiquitous_Snares():
	return render_template("ubiquitous-snares.html")

@app.route("/impossible-snares")
def Impossible_Snares():
	return render_template("impossible-snares.html")

@app.route("/improvised-repair")
def Improvised_Repair():
	return render_template("improvised-repair.html")

@app.route("/bargain-hunter")
def Bargain_Hunter():
	return render_template("bargain-hunter.html")

@app.route("/dandy")
def Dandy():
	return render_template("dandy.html")

@app.route("/hobnobber")
def Hobnobber():
	return render_template("hobnobber.html")

@app.route("/entourage")
def Entourage():
	return render_template("entourage.html")

@app.route("/mesmerizing-gaze")
def Mesmerizing_Gaze():
	return render_template("mesmerizing-gaze.html")

@app.route("/command-attention")
def Command_Attention():
	return render_template("command-attention.html")

@app.route("/vigilante")
def Vigilante():
	return render_template("vigilante.html")

@app.route("/lion-blade-spy")
def Lion_Blade_Spy():
	return render_template("lion-blade-spy.html")

@app.route("/subjective-truth")
def Subjective_Truth():
	return render_template("subjective-truth.html")

@app.route("/sow-rumor")
def Sow_Rumor():
	return render_template("sow-rumor.html")

@app.route("/quick-disguise")
def Quick_Disguise():
	return render_template("quick-disguise.html")

@app.route("/discreet-inquiry")
def Discreet_Inquiry():
	return render_template("discreet-inquiry.html")

@app.route("/hidden-magic")
def Hidden_Magic():
	return render_template("hidden-magic.html")

@app.route("/confabulator")
def Confabulator():
	return render_template("confabulator.html")

@app.route("/slippery-secrets")
def Slippery_Secrets():
	return render_template("slippery-secrets.html")

@app.route("/fabricated-connections")
def Fabricated_Connections():
	return render_template("fabricated-connections.html")

@app.route("/charlatan")
def Charlatan():
	return render_template("charlatan.html")

@app.route("/quick-change")
def Quick_Change():
	return render_template("quick-change.html")

@app.route("/convincing-illusion")
def Convincing_Illusion():
	return render_template("convincing-illusion.html")

@app.route("/flicker")
def Flicker():
	return render_template("flicker.html")

@app.route("/lengthy-diversion")
def Lengthy_Diversion():
	return render_template("lengthy-diversion.html")

@app.route("/trickery-domain-sudden-shift")
def Trickery_Domain__Sudden_Shift():
	return render_template("trickery-domain-sudden-shift.html")

@app.route("/reactive-distraction")
def Reactive_Distraction():
	return render_template("reactive-distraction.html")

@app.route("/reveal-machinations")
def Reveal_Machinations():
	return render_template("reveal-machinations.html")

@app.route("/lie-to-me")
def Lie_to_Me():
	return render_template("lie-to-me.html")

@app.route("/distracting-flattery")
def Distracting_Flattery():
	return render_template("distracting-flattery.html")

@app.route("/backup-disguise")
def Backup_Disguise():
	return render_template("backup-disguise.html")

@app.route("/charming-liar")
def Charming_Liar():
	return render_template("charming-liar.html")

@app.route("/analyze-idiolect")
def Analyze_Idiolect():
	return render_template("analyze-idiolect.html")

@app.route("/spys-countermeasures")
def Spys_Countermeasures():
	return render_template("spys-countermeasures.html")

@app.route("/blank-slate")
def Blank_Slate():
	return render_template("blank-slate.html")

@app.route("/many-guises")
def Many_Guises():
	return render_template("many-guises.html")

@app.route("/double-speak")
def Double_Speak():
	return render_template("double-speak.html")

@app.route("/trickery-domain-tricksters-twin")
def Trickery_Domain__Tricksters_Twin():
	return render_template("trickery-domain-tricksters-twin.html")

@app.route("/bravos-determination")
def Bravos_Determination():
	return render_template("bravos-determination.html")

@app.route("/secret-speech")
def Secret_Speech():
	return render_template("secret-speech.html")

@app.route("/family-domain-soothing-words")
def Family_Domain__Soothing_Words():
	return render_template("family-domain-soothing-words.html")

@app.route("/family-domain-unity")
def Family_Domain__Unity():
	return render_template("family-domain-unity.html")

@app.route("/passion-domain-captivating-adoration")
def Passion_Domain__Captivating_Adoration():
	return render_template("passion-domain-captivating-adoration.html")

@app.route("/passion-domain-charming-touch")
def Passion_Domain__Charming_Touch():
	return render_template("passion-domain-charming-touch.html")

@app.route("/bon-mot")
def Bon_Mot():
	return render_template("bon-mot.html")

@app.route("/evangelize")
def Evangelize():
	return render_template("evangelize.html")

@app.route("/pointed-question")
def Pointed_Question():
	return render_template("pointed-question.html")

@app.route("/glad-hand")
def Glad_Hand():
	return render_template("glad-hand.html")

@app.route("/group-impression")
def Group_Impression():
	return render_template("group-impression.html")

@app.route("/legendary-negotiation")
def Legendary_Negotiation():
	return render_template("legendary-negotiation.html")

@app.route("/shameless-request")
def Shameless_Request():
	return render_template("shameless-request.html")

@app.route("/tense-negotiator")
def Tense_Negotiator():
	return render_template("tense-negotiator.html")

@app.route("/all-in-my-head")
def All_In_My_Head():
	return render_template("all-in-my-head.html")

@app.route("/no-cause-for-alarm")
def No_Cause_For_Alarm():
	return render_template("no-cause-for-alarm.html")

@app.route("/one-for-all")
def One_For_All():
	return render_template("one-for-all.html")

@app.route("/ringmasters-introduction")
def Ringmasters_Introduction():
	return render_template("ringmasters-introduction.html")

@app.route("/diplomacy-feats")
def Diplomacy_Feats():
	return render_template("diplomacy-feats.html")

@app.route("/diehard")
def Diehard():
	return render_template("diehard.html")

@app.route("/necromantic-resistance")
def Necromantic_Resistance():
	return render_template("necromantic-resistance.html")

@app.route("/necromantic-resilience")
def Necromantic_Resilience():
	return render_template("necromantic-resilience.html")

@app.route("/toughness")
def Toughness():
	return render_template("toughness.html")

@app.route("/acquired-tolerance")
def Acquired_Tolerance():
	return render_template("acquired-tolerance.html")

@app.route("/divine-health")
def Divine_Health():
	return render_template("divine-health.html")

@app.route("/inner-strength")
def Inner_Strength():
	return render_template("inner-strength.html")

@app.route("/resist-poison")
def Resist_Poison():
	return render_template("resist-poison.html")

@app.route("/swift-river")
def Swift_River():
	return render_template("swift-river.html")

@app.route("/ardent-nature")
def Ardent_Nature():
	return render_template("ardent-nature.html")

@app.route("/aura-of-courage")
def Aura_of_Courage():
	return render_template("aura-of-courage.html")

@app.route("/bravery")
def Bravery():
	return render_template("bravery.html")

@app.route("/cognitive-loophole")
def Cognitive_Loophole():
	return render_template("cognitive-loophole.html")

@app.route("/conceited-mindset")
def Conceited_Mindset():
	return render_template("conceited-mindset.html")

@app.route("/determination")
def Determination():
	return render_template("determination.html")

@app.route("/enlightened-presence")
def Enlightened_Presence():
	return render_template("enlightened-presence.html")

@app.route("/pure-clarity")
def Pure_Clarity():
	return render_template("pure-clarity.html")

@app.route("/projected-clarity")
def Projected_Clarity():
	return render_template("projected-clarity.html")

@app.route("/resounding-bravery")
def Resounding_Bravery():
	return render_template("resounding-bravery.html")

@app.route("/shake-it-off")
def Shake_It_Off():
	return render_template("shake-it-off.html")

@app.route("/unshakeable-idealism")
def Unshakeable_Idealism():
	return render_template("unshakeable-idealism.html")

@app.route("/ward-mind")
def Ward_Mind():
	return render_template("ward-mind.html")

@app.route("/immutable-body")
def Immutable_Body():
	return render_template("immutable-body.html")

@app.route("/group-coercion")
def Group_Coercion():
	return render_template("group-coercion.html")

@app.route("/lasting-coercion")
def Lasting_Coercion():
	return render_template("lasting-coercion.html")

@app.route("/quick-coercion")
def Quick_Coercion():
	return render_template("quick-coercion.html")

@app.route("/antagonize")
def Antagonize():
	return render_template("antagonize.html")

@app.route("/deimatic-display")
def Deimatic_Display():
	return render_template("deimatic-display.html")

@app.route("/intimidating-glare")
def Intimidating_Glare():
	return render_template("intimidating-glare.html")

@app.route("/scare-to-death")
def Scare_to_Death():
	return render_template("scare-to-death.html")

@app.route("/terrified-retreat")
def Terrified_Retreat():
	return render_template("terrified-retreat.html")

@app.route("/terrifying-howl")
def Terrifying_Howl():
	return render_template("terrifying-howl.html")

@app.route("/terrifying-resistance")
def Terrifying_Resistance():
	return render_template("terrifying-resistance.html")

@app.route("/youre-next")
def Youre_Next():
	return render_template("youre-next.html")

@app.route("/nightmares-domain-shared-nightmare")
def Nightmares_Domain__Shared_Nightmare():
	return render_template("nightmares-domain-shared-nightmare.html")

@app.route("/nightmares-domain-waking-nightmare")
def Nightmares_Domain__Waking_Nightmare():
	return render_template("nightmares-domain-waking-nightmare.html")

@app.route("/tyranny-domain-touch-of-obedience")
def Tyranny_Domain__Touch_of_Obedience():
	return render_template("tyranny-domain-touch-of-obedience.html")

@app.route("/aura-of-despair")
def Aura_of_Despair():
	return render_template("aura-of-despair.html")

@app.route("/decry-thief")
def Decry_Thief():
	return render_template("decry-thief.html")

@app.route("/walk-the-plank")
def Walk_the_Plank():
	return render_template("walk-the-plank.html")

@app.route("/watch-your-back")
def Watch_Your_Back():
	return render_template("watch-your-back.html")

@app.route("/battle-cry")
def Battle_Cry():
	return render_template("battle-cry.html")

@app.route("/medical-researcher")
def Medical_Researcher():
	return render_template("medical-researcher.html")

@app.route("/forensic-acumen")
def Forensic_Acumen():
	return render_template("forensic-acumen.html")

@app.route("/ward-medic")
def Ward_Medic():
	return render_template("ward-medic.html")

@app.route("/rapid-response")
def Rapid_Response():
	return render_template("rapid-response.html")

@app.route("/advanced-medicine")
def Advanced_Medicine():
	return render_template("advanced-medicine.html")

@app.route("/legendary-medic")
def Legendary_Medic():
	return render_template("legendary-medic.html")

@app.route("/treat-condition")
def Treat_Condition():
	return render_template("treat-condition.html")

@app.route("/doctors-visitation")
def Doctors_Visitation():
	return render_template("doctors-visitation.html")

@app.route("/mortal-healing")
def Mortal_Healing():
	return render_template("mortal-healing.html")

@app.route("/paragon-battle-medicine")
def Paragon_Battle_Medicine():
	return render_template("paragon-battle-medicine.html")

@app.route("/resuscitate")
def Resuscitate():
	return render_template("resuscitate.html")

@app.route("/innoculation")
def Innoculation():
	return render_template("innoculation.html")

@app.route("/robust-recovery")
def Robust_Recovery():
	return render_template("robust-recovery.html")

@app.route("/doctors-visitation-9859353")
def Doctors_Visitation():
	return render_template("doctors-visitation-9859353.html")

@app.route("/holistic-care")
def Holistic_Care():
	return render_template("holistic-care.html")

@app.route("/emergency-medical-assistance")
def Emergency_Medical_Assistance():
	return render_template("emergency-medical-assistance.html")

@app.route("/keep-it-together")
def Keep_It_Together():
	return render_template("keep-it-together.html")

@app.route("/feather-step")
def Feather_Step():
	return render_template("feather-step.html")

@app.route("/consult-the-spirits")
def Consult_the_Spirits():
	return render_template("consult-the-spirits.html")

@app.route("/animal-trainer")
def Animal_Trainer():
	return render_template("animal-trainer.html")

@app.route("/companions-cry")
def Companions_Cry():
	return render_template("companions-cry.html")

@app.route("/enlarge-companion")
def Enlarge_Companion():
	return render_template("enlarge-companion.html")

@app.route("/magic-hide")
def Magic_Hide():
	return render_template("magic-hide.html")

@app.route("/mesmerizing-performance")
def Mesmerizing_Performance():
	return render_template("mesmerizing-performance.html")

@app.route("/pale-horse")
def Pale_Horse():
	return render_template("pale-horse.html")

@app.route("/side-by-side")
def Side_By_Side():
	return render_template("side-by-side.html")

@app.route("/insistent-commands")
def Insistent_Commands():
	return render_template("insistent-commands.html")

@app.route("/train-animal")
def Train_Animal():
	return render_template("train-animal.html")

@app.route("/wild-empathy")
def Wild_Empathy():
	return render_template("wild-empathy.html")

@app.route("/air-domain-disperse-into-air")
def Air_Domain__Disperse_Into_Air():
	return render_template("air-domain-disperse-into-air.html")

@app.route("/air-domain-pushing-gust")
def Air_Domain__Pushing_Gust():
	return render_template("air-domain-pushing-gust.html")

@app.route("/aspect-of-the-beast")
def Aspect_of_the_Beast():
	return render_template("aspect-of-the-beast.html")

@app.route("/cold-domain-diamond-dust")
def Cold_Domain__Diamond_Dust():
	return render_template("cold-domain-diamond-dust.html")

@app.route("/cold-domain-winter-bolt")
def Cold_Domain__Winter_Bolt():
	return render_template("cold-domain-winter-bolt.html")

@app.route("/dust-domain-dust-storm")
def Dust_Domain__Dust_Storm():
	return render_template("dust-domain-dust-storm.html")

@app.route("/dust-domain-parch")
def Dust_Domain__Parch():
	return render_template("dust-domain-parch.html")

@app.route("/elemental-bloodline-focus-elemental-toss")
def Elemental_Bloodline_Focus__Elemental_Toss():
	return render_template("elemental-bloodline-focus-elemental-toss.html")

@app.route("/elemental-bloodline-focus-elemental-motion")
def Elemental_Bloodline_Focus__Elemental_Motion():
	return render_template("elemental-bloodline-focus-elemental-motion.html")

@app.route("/elemental-bloodline-focus-elemental-blast")
def Elemental_Bloodline_Focus__Elemental_Blast():
	return render_template("elemental-bloodline-focus-elemental-blast.html")

@app.route("/fey-bloodline-focus-faerie-dust")
def Fey_Bloodline_Focus__Faerie_Dust():
	return render_template("fey-bloodline-focus-faerie-dust.html")

@app.route("/fey-bloodline-focus-fey-disappearance")
def Fey_Bloodline_Focus__Fey_Disappearance():
	return render_template("fey-bloodline-focus-fey-disappearance.html")

@app.route("/fire-domain-fire-ray")
def Fire_Domain__Fire_Ray():
	return render_template("fire-domain-fire-ray.html")

@app.route("/fire-domain-flame-barrier")
def Fire_Domain__Flame_Barrier():
	return render_template("fire-domain-flame-barrier.html")

@app.route("/storm-order")
def Storm_Order():
	return render_template("storm-order.html")

@app.route("/lightning-domain-bottle-the-lightning")
def Lightning_Domain__Bottle_the_Lightning():
	return render_template("lightning-domain-bottle-the-lightning.html")

@app.route("/lightning-domain-charged-javelin")
def Lightning_Domain__Charged_Javelin():
	return render_template("lightning-domain-charged-javelin.html")

@app.route("/nature-domain-vibrant-thorns")
def Nature_Domain__Vibrant_Thorns():
	return render_template("nature-domain-vibrant-thorns.html")

@app.route("/nymph-bloodline-focus-nymphs-token")
def Nymph_Bloodline_focus__Nymphs_Token():
	return render_template("nymph-bloodline-focus-nymphs-token.html")

@app.route("/nymph-bloodline-focus-blinding-beauty")
def Nymph_Bloodline_Focus__Blinding_Beauty():
	return render_template("nymph-bloodline-focus-blinding-beauty.html")

@app.route("/nymph-bloodline-focus-establishing-ward")
def Nymph_Bloodline_Focus__Establishing_Ward():
	return render_template("nymph-bloodline-focus-establishing-ward.html")

@app.route("/virulent")
def Virulent():
	return render_template("virulent.html")

@app.route("/plague-domain-divine-plagues")
def Plague_Domain__Divine_Plagues():
	return render_template("plague-domain-divine-plagues.html")

@app.route("/plague-domain-foul-miasma")
def Plague_Domain__Foul_Miasma():
	return render_template("plague-domain-foul-miasma.html")

@app.route("/tempest-surge")
def Tempest_Surge():
	return render_template("tempest-surge.html")

@app.route("/storm-retribution")
def Storm_Retribution():
	return render_template("storm-retribution.html")

@app.route("/swarm")
def Swarm():
	return render_template("swarm.html")

@app.route("/swarm-domain-swarm-form")
def Swarm_Domain__Swarm_Form():
	return render_template("swarm-domain-swarm-form.html")

@app.route("/water-domain-downpour")
def Water_Domain__Downpour():
	return render_template("water-domain-downpour.html")

@app.route("/water-domain-tidal-surge")
def Water_Domain__Tidal_Surge():
	return render_template("water-domain-tidal-surge.html")

@app.route("/cavalier-banner")
def Cavalier_Banner():
	return render_template("cavalier-banner.html")

@app.route("/cavaliers-charge")
def Cavaliers_Charge():
	return render_template("cavaliers-charge.html")

@app.route("/defend-mount")
def Defend_Mount():
	return render_template("defend-mount.html")

@app.route("/express-rider")
def Express_Rider():
	return render_template("express-rider.html")

@app.route("/quick-mount")
def Quick_Mount():
	return render_template("quick-mount.html")

@app.route("/ride")
def Ride():
	return render_template("ride.html")

@app.route("/trampling-charge")
def Trampling_Charge():
	return render_template("trampling-charge.html")

@app.route("/unseat")
def Unseat():
	return render_template("unseat.html")

@app.route("/green-empathy")
def Green_Empathy():
	return render_template("green-empathy.html")

@app.route("/magical-mobility")
def Magical_Mobility():
	return render_template("magical-mobility.html")

@app.route("/primal-aegis")
def Primal_Aegis():
	return render_template("primal-aegis.html")

@app.route("/influence-nature")
def Influence_Nature():
	return render_template("influence-nature.html")

@app.route("/natural-medicine")
def Natural_Medicine():
	return render_template("natural-medicine.html")

@app.route("/fresh-ingredients")
def Fresh_Ingredients():
	return render_template("fresh-ingredients.html")

@app.route("/form-control")
def Form_Control():
	return render_template("form-control.html")

@app.route("/reactive-transformation")
def Reactive_Transformation():
	return render_template("reactive-transformation.html")

@app.route("/heal-companion")
def Heal_Companion():
	return render_template("heal-companion.html")

@app.route("/auspicious-mount")
def Auspicious_Mount():
	return render_template("auspicious-mount.html")

@app.route("/earth-domain-localized-quake")
def Earth_Domain__Localized_Quake():
	return render_template("earth-domain-localized-quake.html")

@app.route("/earth-domain-hurtling-stone")
def Earth_Domain__Hurtling_Stone():
	return render_template("earth-domain-hurtling-stone.html")

@app.route("/bizarre-magic")
def Bizarre_Magic():
	return render_template("bizarre-magic.html")

@app.route("/deceptive-worship")
def Deceptive_Worship():
	return render_template("deceptive-worship.html")

@app.route("/living-hair")
def Living_Hair():
	return render_template("living-hair.html")

@app.route("/aberrant-bloodline-focus-tentacular-limbs")
def Aberrant_Bloodline_Focus__Tentacular_Limbs():
	return render_template("aberrant-bloodline-focus-tentacular-limbs.html")

@app.route("/aberrant-bloodline-focus-unusual-anatomy")
def Aberrant_Bloodline_Focus__Unusual_Anatomy():
	return render_template("aberrant-bloodline-focus-unusual-anatomy.html")

@app.route("/abomination-domain-fearful-feast")
def Abomination_Domain__Fearful_Feast():
	return render_template("abomination-domain-fearful-feast.html")

@app.route("/abomination-domain-lift-natures-caul")
def Abomination_Domain__Lift_Natures_Caul():
	return render_template("abomination-domain-lift-natures-caul.html")

@app.route("/cackle")
def Cackle():
	return render_template("cackle.html")

@app.route("/decay-domain-fallow-field")
def Decay_Domain__Fallow_Field():
	return render_template("decay-domain-fallow-field.html")

@app.route("/decay-domain-withering-grasp")
def Decay_Domain__Withering_Grasp():
	return render_template("decay-domain-withering-grasp.html")

@app.route("/delirium-domain-ephemeral-hazards")
def Delirium_Domain__Ephemeral_Hazards():
	return render_template("delirium-domain-ephemeral-hazards.html")

@app.route("/delirium-domain-hyperfocus")
def Delirium_Domain__Hyperfocus():
	return render_template("delirium-domain-hyperfocus.html")

@app.route("/discern-secrets")
def Discern_Secrets():
	return render_template("discern-secrets.html")

@app.route("/disturbing-knowledge")
def Disturbing_Knowledge():
	return render_template("disturbing-knowledge.html")

@app.route("/dreams-domain-dreamers-call")
def Dreams_Domain__Dreamers_Call():
	return render_template("dreams-domain-dreamers-call.html")

@app.route("/dreams-domain-sweet-dream")
def Dreams_Domain__Sweet_Dream():
	return render_template("dreams-domain-sweet-dream.html")

@app.route("/eldritch-nails")
def Eldritch_Nails():
	return render_template("eldritch-nails.html")

@app.route("/fate-domain-read-domain")
def Fate_Domain__Read_Domain():
	return render_template("fate-domain-read-domain.html")

@app.route("/fate-domain-tempt-fate")
def Fate_Domain__Tempt_Fate():
	return render_template("fate-domain-tempt-fate.html")

@app.route("/hag-bloodline-focus-jealous-hex")
def Hag_Bloodline_Focus__Jealous_Hex():
	return render_template("hag-bloodline-focus-jealous-hex.html")

@app.route("/hag-bloodline-focus-youre-mine")
def Hag_Bloodline_Focus__Youre_Mine():
	return render_template("hag-bloodline-focus-youre-mine.html")

@app.route("/hag-bloodline-focus-horrific-visage")
def Hag_Bloodline_Focus__Horrific_Visage():
	return render_template("hag-bloodline-focus-horrific-visage.html")

@app.route("/lesson-of-protection")
def Lesson_of_Protection():
	return render_template("lesson-of-protection.html")

@app.route("/lesson-of-shadow")
def Lesson_of_Shadow():
	return render_template("lesson-of-shadow.html")

@app.route("/lesson-of-the-elements")
def Lesson_of_the_Elements():
	return render_template("lesson-of-the-elements.html")

@app.route("/lesson-of-the-frozen-queen")
def Lesson_of_the_Frozen_Queen():
	return render_template("lesson-of-the-frozen-queen.html")

@app.route("/lesson-of-vengeance")
def Lesson_of_Vengeance():
	return render_template("lesson-of-vengeance.html")

@app.route("/moon-domain-moon-beam")
def Moon_Domain__Moon_Beam():
	return render_template("moon-domain-moon-beam.html")

@app.route("/moon-domain-touch-of-the-moon")
def Moon_Domain__Touch_of_the_Moon():
	return render_template("moon-domain-touch-of-the-moon.html")

@app.route("/split-the-tongue")
def Split_the_Tongue():
	return render_template("split-the-tongue.html")

@app.route("/nudge-fate")
def Nudge_Fate():
	return render_template("nudge-fate.html")

@app.route("/phase-familiar")
def Phase_Familiar():
	return render_template("phase-familiar.html")

@app.route("/shadow-bloodline-focus-dim-the-light")
def Shadow_Bloodline_Focus__Dim_the_Light():
	return render_template("shadow-bloodline-focus-dim-the-light.html")

@app.route("/shadow-bloodline-focus-steal-shadow")
def Shadow_Bloodline_Focus__Steal_Shadow():
	return render_template("shadow-bloodline-focus-steal-shadow.html")

@app.route("/shadow-bloodline-focus-consuming-darkness")
def Shadow_Bloodline_Focus__Consuming_Darkness():
	return render_template("shadow-bloodline-focus-consuming-darkness.html")

@app.route("/shroud-of-night")
def Shroud_of_Night():
	return render_template("shroud-of-night.html")

@app.route("/sorrow-domain-lament")
def Sorrow_Domain__Lament():
	return render_template("sorrow-domain-lament.html")

@app.route("/soul-domain-ectoplasmic-interstice")
def Soul_Domain__Ectoplasmic_Interstice():
	return render_template("soul-domain-ectoplasmic-interstice.html")

@app.route("/spirit-object")
def Spirit_Object():
	return render_template("spirit-object.html")

@app.route("/star-domain-asterism")
def Star_Domain__Asterism():
	return render_template("star-domain-asterism.html")

@app.route("/star-domain-zenith-star")
def Star_Domain__Zenith_Star():
	return render_template("star-domain-zenith-star.html")

@app.route("/stoke-the-heart")
def Stoke_the_Heart():
	return render_template("stoke-the-heart.html")

@app.route("/void-domain-door-to-the-beyond")
def Void_Domain__Door_to_the_Beyond():
	return render_template("void-domain-door-to-the-beyond.html")

@app.route("/void-domain-empty-inside")
def Void_Domain__Empty_Inside():
	return render_template("void-domain-empty-inside.html")

@app.route("/wilding-word")
def Wilding_Word():
	return render_template("wilding-word.html")

@app.route("/schooled-in-secrets")
def Schooled_in_Secrets():
	return render_template("schooled-in-secrets.html")

@app.route("/combat-reading")
def Combat_Reading():
	return render_template("combat-reading.html")

@app.route("/eclectic-skill")
def Eclectic_Skill():
	return render_template("eclectic-skill.html")

@app.route("/oddity-identification")
def Oddity_Identification():
	return render_template("oddity-identification.html")

@app.route("/scholarly-defense")
def Scholarly_Defense():
	return render_template("scholarly-defense.html")

@app.route("/root-magic")
def Root_Magic():
	return render_template("root-magic.html")

@app.route("/peer-beyond")
def Peer_Beyond():
	return render_template("peer-beyond.html")

@app.route("/naga-domain-ordained-purpose")
def Naga_Domain__Ordained_Purpose():
	return render_template("naga-domain-ordained-purpose.html")

@app.route("/spirit-hunter")
def Spirit_Hunter():
	return render_template("spirit-hunter.html")

@app.route("/spectral-strike")
def Spectral_Strike():
	return render_template("spectral-strike.html")

@app.route("/graves-voice")
def Graves_Voice():
	return render_template("graves-voice.html")

@app.route("/investigate-haunting")
def Investigate_Haunting():
	return render_template("investigate-haunting.html")

@app.route("/clinging-ice")
def Clinging_Ice():
	return render_template("clinging-ice.html")

@app.route("/evil-eye")
def Evil_Eye():
	return render_template("evil-eye.html")

@app.route("/witchs-bottle")
def Witchs_Bottle():
	return render_template("witchs-bottle.html")

@app.route("/hazard-finder")
def Hazard_Finder():
	return render_template("hazard-finder.html")

@app.route("/battlefield-surveyor")
def Battlefield_Surveyor():
	return render_template("battlefield-surveyor.html")

@app.route("/plot-the-future")
def Plot_the_Future():
	return render_template("plot-the-future.html")

@app.route("/reconstruct-the-scene")
def Reconstruct_the_Scene():
	return render_template("reconstruct-the-scene.html")

@app.route("/sense-alignment")
def Sense_Alignment():
	return render_template("sense-alignment.html")

@app.route("/boleras-interrogation")
def Boleras_Interrogation():
	return render_template("boleras-interrogation.html")

@app.route("/lie-detector")
def Lie_Detector():
	return render_template("lie-detector.html")

@app.route("/investigate")
def Investigate():
	return render_template("investigate.html")

@app.route("/ongoing-investigation")
def Ongoing_Investigation():
	return render_template("ongoing-investigation.html")

@app.route("/thats-odd")
def Thats_Odd():
	return render_template("thats-odd.html")

@app.route("/pursue-a-lead")
def Pursue_a_Lead():
	return render_template("pursue-a-lead.html")

@app.route("/clue-in")
def Clue_In():
	return render_template("clue-in.html")

@app.route("/clue-them-all-in")
def Clue_Them_All_In():
	return render_template("clue-them-all-in.html")

@app.route("/connect-the-dots")
def Connect_the_Dots():
	return render_template("connect-the-dots.html")

@app.route("/detectives-readiness")
def Detectives_Readiness():
	return render_template("detectives-readiness.html")

@app.route("/interrogation")
def Interrogation():
	return render_template("interrogation.html")

@app.route("/just-one-more-thing")
def Just_One_More_Thing():
	return render_template("just-one-more-thing.html")

@app.route("/lead-investigator")
def Lead_Investigator():
	return render_template("lead-investigator.html")

@app.route("/red-herring")
def Red_Herring():
	return render_template("red-herring.html")

@app.route("/solid-lead")
def Solid_Lead():
	return render_template("solid-lead.html")

@app.route("/subject-of-opportunity")
def Subject_of_Opportunity():
	return render_template("subject-of-opportunity.html")

@app.route("/underworld-investigator")
def Underworld_Investigator():
	return render_template("underworld-investigator.html")

@app.route("/whodunnit")
def Whodunnit():
	return render_template("whodunnit.html")

@app.route("/battle-assessment")
def Battle_Assessment():
	return render_template("battle-assessment.html")

@app.route("/incredible-scout")
def Incredible_Scout():
	return render_template("incredible-scout.html")

@app.route("/expeditious-search")
def Expeditious_Search():
	return render_template("expeditious-search.html")

@app.route("/observant-explorer")
def Observant_Explorer():
	return render_template("observant-explorer.html")

@app.route("/thorough-search")
def Thorough_Search():
	return render_template("thorough-search.html")

@app.route("/grave-sense")
def Grave_Sense():
	return render_template("grave-sense.html")

@app.route("/sense-chaos")
def Sense_Chaos():
	return render_template("sense-chaos.html")

@app.route("/spiritual-sense")
def Spiritual_Sense():
	return render_template("spiritual-sense.html")

@app.route("/supertaster")
def Supertaster():
	return render_template("supertaster.html")

@app.route("/instinctive-strike")
def Instinctive_Strike():
	return render_template("instinctive-strike.html")

@app.route("/sense-evil")
def Sense_Evil():
	return render_template("sense-evil.html")

@app.route("/sense-good")
def Sense_Good():
	return render_template("sense-good.html")

@app.route("/sense-the-unseen")
def Sense_the_Unseen():
	return render_template("sense-the-unseen.html")

@app.route("/soulsight")
def Soulsight():
	return render_template("soulsight.html")

@app.route("/foresee-danger")
def Foresee_Danger():
	return render_template("foresee-danger.html")

@app.route("/predictable")
def Predictable():
	return render_template("predictable.html")

@app.route("/edgewatch-detective")
def Edgewatch_Detective():
	return render_template("edgewatch-detective.html")

@app.route("/anticipate-ambush")
def Anticipate_Ambush():
	return render_template("anticipate-ambush.html")

@app.route("/allegro")
def Allegro():
	return render_template("allegro.html")

@app.route("/inspire-courage")
def Inspire_Courage():
	return render_template("inspire-courage.html")

@app.route("/inspire-defense")
def Inspire_Defense():
	return render_template("inspire-defense.html")

@app.route("/inspire-heroics")
def Inspire_Heroics():
	return render_template("inspire-heroics.html")

@app.route("/lingering-composition")
def Lingering_Composition():
	return render_template("lingering-composition.html")

@app.route("/annotate-composition")
def Annotate_Composition():
	return render_template("annotate-composition.html")

@app.route("/call-and-response")
def Call_and_Response():
	return render_template("call-and-response.html")

@app.route("/courageous-onslaught")
def Courageous_Onslaught():
	return render_template("courageous-onslaught.html")

@app.route("/disrupting-actions")
def Disrupting_Actions():
	return render_template("disrupting-actions.html")

@app.route("/courageous-opportunity")
def Courageous_Opportunity():
	return render_template("courageous-opportunity.html")

@app.route("/sorrow-domain-overflowing-sorrow")
def Sorrow_Domain__Overflowing_Sorrow():
	return render_template("sorrow-domain-overflowing-sorrow.html")

@app.route("/lesson-of-dreams")
def Lesson_of_Dreams():
	return render_template("lesson-of-dreams.html")

@app.route("/defensive-coordination")
def Defensive_Coordination():
	return render_template("defensive-coordination.html")

@app.route("/directed-audience")
def Directed_Audience():
	return render_template("directed-audience.html")

@app.route("/dirge-of-doom")
def Dirge_of_Doom():
	return render_template("dirge-of-doom.html")

@app.route("/discordant-voice")
def Discordant_Voice():
	return render_template("discordant-voice.html")

@app.route("/earworm")
def Earworm():
	return render_template("earworm.html")

@app.route("/well-versed")
def Well_Versed():
	return render_template("well-versed.html")

@app.route("/educate-allies")
def Educate_Allies():
	return render_template("educate-allies.html")

@app.route("/fatal-aria")
def Fatal_Aria():
	return render_template("fatal-aria.html")

@app.route("/harmonize")
def Harmonize():
	return render_template("harmonize.html")

@app.route("/inspire-competence")
def Inspire_Competence():
	return render_template("inspire-competence.html")

@app.route("/loremasters-etude")
def Loremasters_Etude():
	return render_template("loremasters-etude.html")

@app.route("/ode-to-ouroboros")
def Ode_to_Ouroboros():
	return render_template("ode-to-ouroboros.html")

@app.route("/pied-piping")
def Pied_Piping():
	return render_template("pied-piping.html")

@app.route("/resounding-finale")
def Resounding_Finale():
	return render_template("resounding-finale.html")

@app.route("/shared-assault")
def Shared_Assault():
	return render_template("shared-assault.html")

@app.route("/silvers-refrain")
def Silvers_Refrain():
	return render_template("silvers-refrain.html")

@app.route("/song-of-the-fallen")
def Song_of_the_Fallen():
	return render_template("song-of-the-fallen.html")

@app.route("/songs-of-strength")
def Songs_of_Strength():
	return render_template("songs-of-strength.html")

@app.route("/symphony-of-the-unfettered-heart")
def Symphony_of_the_Unfettered_Heart():
	return render_template("symphony-of-the-unfettered-heart.html")

@app.route("/triple-time")
def Triple_Time():
	return render_template("triple-time.html")

@app.route("/triumphant-inspiration")
def Triumphant_Inspiration():
	return render_template("triumphant-inspiration.html")

@app.route("/unusual-composition")
def Unusual_Composition():
	return render_template("unusual-composition.html")

@app.route("/vigorous-inspiration")
def Vigorous_Inspiration():
	return render_template("vigorous-inspiration.html")

@app.route("/courageous-advance")
def Courageous_Advance():
	return render_template("courageous-advance.html")

@app.route("/courageous-assault")
def Courageous_Assault():
	return render_template("courageous-assault.html")

@app.route("/distracting-performance")
def Distracting_Performance():
	return render_template("distracting-performance.html")

@app.route("/gladiator")
def Gladiator():
	return render_template("gladiator.html")

@app.route("/play-to-the-crowd")
def Play_To_The_Crowd():
	return render_template("play-to-the-crowd.html")

@app.route("/call-your-shot")
def Call_Your_Shot():
	return render_template("call-your-shot.html")

@app.route("/fascinating-performance")
def Fascinating_Performance():
	return render_template("fascinating-performance.html")

@app.route("/flourishing-finish")
def Flourishing_Finish():
	return render_template("flourishing-finish.html")

@app.route("/focused-fascination")
def Focused_Fascination():
	return render_template("focused-fascination.html")

@app.route("/juggle")
def Juggle():
	return render_template("juggle.html")

@app.route("/focused-juggler")
def Focused_Juggler():
	return render_template("focused-juggler.html")

@app.route("/quick-juggle")
def Quick_Juggle():
	return render_template("quick-juggle.html")

@app.route("/reflexive-catch")
def Reflexive_Catch():
	return render_template("reflexive-catch.html")

@app.route("/virtuosic-performance")
def Virtuosic_Performance():
	return render_template("virtuosic-performance.html")

@app.route("/acting")
def Acting():
	return render_template("acting.html")

@app.route("/fancy-moves")
def Fancy_Moves():
	return render_template("fancy-moves.html")

@app.route("/impressive-performance")
def Impressive_Performance():
	return render_template("impressive-performance.html")

@app.route("/versatile-performance")
def Versatile_Performance():
	return render_template("versatile-performance.html")

@app.route("/quick-juggler")
def Quick_Juggler():
	return render_template("quick-juggler.html")

@app.route("/never-tire")
def Never_Tire():
	return render_template("never-tire.html")

@app.route("/reverberate")
def Reverberate():
	return render_template("reverberate.html")

@app.route("/orthographic-mastery")
def Orthographic_Mastery():
	return render_template("orthographic-mastery.html")

@app.route("/all-knowledge-skills")
def All_Knowledge_Skills():
	return render_template("all-knowledge-skills.html")

@app.route("/devoted-focus")
def Devoted_Focus():
	return render_template("devoted-focus.html")

@app.route("/moment-of-clarity")
def Moment_of_Clarity():
	return render_template("moment-of-clarity.html")

@app.route("/surging-focus")
def Surging_Focus():
	return render_template("surging-focus.html")

@app.route("/transcribe-moment")
def Transcribe_Moment():
	return render_template("transcribe-moment.html")

@app.route("/great-boaster")
def Great_Boaster():
	return render_template("great-boaster.html")

@app.route("/spot-translate")
def Spot_Translate():
	return render_template("spot-translate.html")

@app.route("/tongue-of-the-sun-and-moon")
def Tongue_of_the_Sun_and_Moon():
	return render_template("tongue-of-the-sun-and-moon.html")

@app.route("/liberators-drive")
def Liberators_Drive():
	return render_template("liberators-drive.html")

@app.route("/practiced-guidance")
def Practiced_Guidance():
	return render_template("practiced-guidance.html")

@app.route("/scarecrow")
def Scarecrow():
	return render_template("scarecrow.html")

@app.route("/seasoned-pro")
def Seasoned_Pro():
	return render_template("seasoned-pro.html")

@app.route("/gossip-lore")
def Gossip_Lore():
	return render_template("gossip-lore.html")

@app.route("/legendary-professional")
def Legendary_Professional():
	return render_template("legendary-professional.html")

@app.route("/unmistakable-lore")
def Unmistakable_Lore():
	return render_template("unmistakable-lore.html")

@app.route("/inspiring-marshal-stance")
def Inspiring_Marshal_Stance():
	return render_template("inspiring-marshal-stance.html")

@app.route("/snap-out-of-it")
def Snap_Out_of_It():
	return render_template("snap-out-of-it.html")

@app.route("/tactical-cadence")
def Tactical_Cadence():
	return render_template("tactical-cadence.html")

@app.route("/to-battle")
def To_Battle():
	return render_template("to-battle.html")

@app.route("/dread-marshal-stance")
def Dread_Marshal_Stance():
	return render_template("dread-marshal-stance.html")

@app.route("/scrollmaster")
def Scrollmaster():
	return render_template("scrollmaster.html")

@app.route("/oozemorph")
def Oozemorph():
	return render_template("oozemorph.html")

@app.route("/hideous-ululation")
def Hideous_Ululation():
	return render_template("hideous-ululation.html")

@app.route("/ooze-empathy")
def Ooze_Empathy():
	return render_template("ooze-empathy.html")

@app.route("/rubbery-skin")
def Rubbery_Skin():
	return render_template("rubbery-skin.html")

@app.route("/vacate-vision")
def Vacate_Vision():
	return render_template("vacate-vision.html")

@app.route("/able-ritualist")
def Able_Ritualist():
	return render_template("able-ritualist.html")

@app.route("/assured-ritualist")
def Assured_Ritualist():
	return render_template("assured-ritualist.html")

@app.route("/flexible-ritualist")
def Flexible_Ritualist():
	return render_template("flexible-ritualist.html")

@app.route("/resourceful-ritualist")
def Resourceful_Ritualist():
	return render_template("resourceful-ritualist.html")

@app.route("/speedy-rituals")
def Speedy_Rituals():
	return render_template("speedy-rituals.html")

@app.route("/cognitive-crossover")
def Cognitive_Crossover():
	return render_template("cognitive-crossover.html")

@app.route("/deductive-improvisation")
def Deductive_Improvisation():
	return render_template("deductive-improvisation.html")

@app.route("/expeditious-inspection")
def Expeditious_Inspection():
	return render_template("expeditious-inspection.html")

@app.route("/flexible-studies")
def Flexible_Studies():
	return render_template("flexible-studies.html")

@app.route("/untrained-improvisation")
def Untrained_Improvisation():
	return render_template("untrained-improvisation.html")

@app.route("/tricksters-ace")
def Tricksters_Ace():
	return render_template("tricksters-ace.html")

@app.route("/incredible-luck")
def Incredible_Luck():
	return render_template("incredible-luck.html")

@app.route("/diamond-soul")
def Diamond_Soul():
	return render_template("diamond-soul.html")

@app.route("/impossible-technique")
def Impossible_Technique():
	return render_template("impossible-technique.html")

@app.route("/keen-follower")
def Keen_Follower():
	return render_template("keen-follower.html")

@app.route("/swordmasters-assist")
def Swordmasters_Assist():
	return render_template("swordmasters-assist.html")

@app.route("/divine-guidance")
def Divine_Guidance():
	return render_template("divine-guidance.html")

@app.route("/angelic-bloodline-focus-angelic-halo")
def Angelic_Bloodline_Focus__Angelic_Halo():
	return render_template("angelic-bloodline-focus-angelic-halo.html")

@app.route("/angelic-bloodline-focus-celestial-brand")
def Angelic_Bloodline_Focus__Celestial_Brand():
	return render_template("angelic-bloodline-focus-celestial-brand.html")

@app.route("/demonic-bloodline-focus-gluttons-jaw")
def Demonic_Bloodline_Focus__Gluttons_Jaw():
	return render_template("demonic-bloodline-focus-gluttons-jaw.html")

@app.route("/diabolic-bloodline-focus-diabolic-edict")
def Diabolic_Bloodline_Focus__Diabolic_Edict():
	return render_template("diabolic-bloodline-focus-diabolic-edict.html")

@app.route("/diabolic-bloodline-focus-embrace-the-pit")
def Diabolic_Bloodline_Focus__Embrace_the_Pit():
	return render_template("diabolic-bloodline-focus-embrace-the-pit.html")

@app.route("/psychopomp-bloodline-focus-sepulchral-mask")
def Psychopomp_Bloodline_Focus__Sepulchral_Mask():
	return render_template("psychopomp-bloodline-focus-sepulchral-mask.html")

@app.route("/psychopomp-bloodline-focus-spirit-veil")
def Psychopomp_Bloodline_Focus__Spirit_Veil():
	return render_template("psychopomp-bloodline-focus-spirit-veil.html")

@app.route("/diabolic-bloodline-focus-hellfire-plume")
def Diabolic_Bloodline_Focus__Hellfire_Plume():
	return render_template("diabolic-bloodline-focus-hellfire-plume.html")

@app.route("/demonic-bloodline-focus-swamp-of-sloth")
def Demonic_Bloodline_Focus__Swamp_of_Sloth():
	return render_template("demonic-bloodline-focus-swamp-of-sloth.html")

@app.route("/demonic-bloodline-focus-abyssal-wrath")
def Demonic_Bloodline_Focus__Abyssal_Wrath():
	return render_template("demonic-bloodline-focus-abyssal-wrath.html")

@app.route("/psychopomp-bloodline-focus-shepard-of-souls")
def Psychopomp_Bloodline_Focus__Shepard_of_Souls():
	return render_template("psychopomp-bloodline-focus-shepard-of-souls.html")

@app.route("/undead-bloodline-focus-drain-life")
def Undead_Bloodline_Focus__Drain_Life():
	return render_template("undead-bloodline-focus-drain-life.html")

@app.route("/undead-bloodline-focus-grasping-grave")
def Undead_Bloodline_Focus__Grasping_Grave():
	return render_template("undead-bloodline-focus-grasping-grave.html")

@app.route("/light-of-revelation")
def Light_of_Revelation():
	return render_template("light-of-revelation.html")

@app.route("/ambition-domain-blind-ambition")
def Ambition_Domain__Blind_Ambition():
	return render_template("ambition-domain-blind-ambition.html")

@app.route("/ambition-domain-competitive-edge")
def Ambition_Domain__Competitive_Edge():
	return render_template("ambition-domain-competitive-edge.html")

@app.route("/confidence-domain-delusional-pride")
def Confidence_Domain__Delusional_Pride():
	return render_template("confidence-domain-delusional-pride.html")

@app.route("/confidence-domain-veil-of-confidence")
def Confidence_Domain__Veil_of_Confidence():
	return render_template("confidence-domain-veil-of-confidence.html")

@app.route("/death-domain-deaths-call")
def Death_Domain__Deaths_Call():
	return render_template("death-domain-deaths-call.html")

@app.route("/death-domain-eradicate-undeath")
def Death_Domain__Eradicate_Undeath():
	return render_template("death-domain-eradicate-undeath.html")

@app.route("/destruction-domain-cry-of-destruction")
def Destruction_Domain__Cry_of_Destruction():
	return render_template("destruction-domain-cry-of-destruction.html")

@app.route("/destruction-domain-destructive-aura")
def Destruction_Domain__Destructive_Aura():
	return render_template("destruction-domain-destructive-aura.html")

@app.route("/deitys-protection")
def Deitys_Protection():
	return render_template("deitys-protection.html")

@app.route("/duty-domain-dutiful-challenge")
def Duty_Domain__Dutiful_Challenge():
	return render_template("duty-domain-dutiful-challenge.html")

@app.route("/duty-domain-oathkeepers-insignia")
def Duty_Domain__Oathkeepers_Insignia():
	return render_template("duty-domain-oathkeepers-insignia.html")

@app.route("/healing-domain-healers-blessing")
def Healing_Domain_Healers_Blessing():
	return render_template("healing-domain-healers-blessing.html")

@app.route("/luck-domain-bit-of-luck")
def Luck_Domain_Bit_of_Luck():
	return render_template("luck-domain-bit-of-luck.html")

@app.route("/luck-domain-lucky-break")
def Luck_Domain__Lucky_Break():
	return render_template("luck-domain-lucky-break.html")

@app.route("/pain-domain-savor-the-sting-8156902")
def Pain_Domain__Savor_the_Sting():
	return render_template("pain-domain-savor-the-sting-8156902.html")

@app.route("/pain-domain-retributive-pain")
def Pain_Domain__Retributive_Pain():
	return render_template("pain-domain-retributive-pain.html")

@app.route("/perfection-domain-perfected-form")
def Perfection_Domain__Perfected_Form():
	return render_template("perfection-domain-perfected-form.html")

@app.route("/perfection-domain-perfected-mind")
def Perfection_Domain__Perfected_Mind():
	return render_template("perfection-domain-perfected-mind.html")

@app.route("/protection-domain-protectors-sacrifice")
def Protection_Domain__Protectors_Sacrifice():
	return render_template("protection-domain-protectors-sacrifice.html")

@app.route("/protection-domain-protectors-sphere")
def Protection_Domain__Protectors_Sphere():
	return render_template("protection-domain-protectors-sphere.html")

@app.route("/repose-domain-font-of-serenity")
def Repose_Domain__Font_of_Serenity():
	return render_template("repose-domain-font-of-serenity.html")

@app.route("/repose-domain-share-burden")
def Repose_Domain__Share_Burden():
	return render_template("repose-domain-share-burden.html")

@app.route("/shield-of-faith")
def Shield_of_Faith():
	return render_template("shield-of-faith.html")

@app.route("/sun-domain-dazzling-flash")
def Sun_Domain__Dazzling_Flash():
	return render_template("sun-domain-dazzling-flash.html")

@app.route("/sun-domain-positive-luminance")
def Sun_Domain__Positive_Luminance():
	return render_template("sun-domain-positive-luminance.html")

@app.route("/toll-domain-practice-makes-perfect")
def Toll_Domain__Practice_Makes_Perfect():
	return render_template("toll-domain-practice-makes-perfect.html")

@app.route("/toll-domain-tireless-worker")
def Toll_Domain__Tireless_Worker():
	return render_template("toll-domain-tireless-worker.html")

@app.route("/truth-domain-word-of-truth")
def Truth_Domain__Word_of_Truth():
	return render_template("truth-domain-word-of-truth.html")

@app.route("/truth-domain-glimpse-of-truth")
def Truth_Domain__Glimpse_of_Truth():
	return render_template("truth-domain-glimpse-of-truth.html")

@app.route("/undeath-domain-spell-malignant")
def Undeath_Domain__Spell_Malignant():
	return render_template("undeath-domain-spell-malignant.html")

@app.route("/undeath-domain-touch-of-undeath")
def Undeath_Domain__Touch_of_Undeath():
	return render_template("undeath-domain-touch-of-undeath.html")

@app.route("/vigil-domain-object-memory")
def Vigil_Domain__Object_Memory():
	return render_template("vigil-domain-object-memory.html")

@app.route("/vigil-domain-remember-the-lost")
def Vigil_Domain__Remember_the_Lost():
	return render_template("vigil-domain-remember-the-lost.html")

@app.route("/shield-block")
def Shield_Block():
	return render_template("shield-block.html")

@app.route("/emblazon-antimagic")
def Emblazon_Antimagic():
	return render_template("emblazon-antimagic.html")

@app.route("/emblazon-armament")
def Emblazon_Armament():
	return render_template("emblazon-armament.html")

@app.route("/emblazon-energy")
def Emblazon_Energy():
	return render_template("emblazon-energy.html")

@app.route("/emblazon-divinity")
def Emblazon_Divinity():
	return render_template("emblazon-divinity.html")

@app.route("/premonition-of-avoidance")
def Premonition_of_Avoidance():
	return render_template("premonition-of-avoidance.html")

@app.route("/shared-avoidance")
def Shared_Avoidance():
	return render_template("shared-avoidance.html")

@app.route("/spiritual-explorer")
def Spiritual_Explorer():
	return render_template("spiritual-explorer.html")

@app.route("/aura-of-faith")
def Aura_of_Faith():
	return render_template("aura-of-faith.html")

@app.route("/aura-of-righteousness")
def Aura_of_Righteousness():
	return render_template("aura-of-righteousness.html")

@app.route("/divine-grace")
def Divine_Grace():
	return render_template("divine-grace.html")

@app.route("/hellknight-armiger")
def Hellknight_Armiger():
	return render_template("hellknight-armiger.html")

@app.route("/false-faith")
def False_Faith():
	return render_template("false-faith.html")

@app.route("/oracular-warning")
def Oracular_Warning():
	return render_template("oracular-warning.html")

@app.route("/pilgrims-token")
def Pilgrims_Token():
	return render_template("pilgrims-token.html")

@app.route("/diabolic-certitude")
def Diabolic_Certitude():
	return render_template("diabolic-certitude.html")

@app.route("/student-of-the-canon")
def Student_of_the_Canon():
	return render_template("student-of-the-canon.html")

@app.route("/glean-lore")
def Glean_Lore():
	return render_template("glean-lore.html")

@app.route("/accelerating-touch")
def Accelerating_Touch():
	return render_template("accelerating-touch.html")

@app.route("/amplifying-touch")
def Amplifying_Touch():
	return render_template("amplifying-touch.html")

@app.route("/heal-mount")
def Heal_Mount():
	return render_template("heal-mount.html")

@app.route("/mercy")
def Mercy():
	return render_template("mercy.html")

@app.route("/affliction-mercy")
def Affliction_Mercy():
	return render_template("affliction-mercy.html")

@app.route("/elucidating-mercy")
def Elucidating_Mercy():
	return render_template("elucidating-mercy.html")

@app.route("/greater-mercy")
def Greater_Mercy():
	return render_template("greater-mercy.html")

@app.route("/invigorating-mercy")
def Invigorating_Mercy():
	return render_template("invigorating-mercy.html")

@app.route("/rejuvenating-touch")
def Rejuvenating_Touch():
	return render_template("rejuvenating-touch.html")

@app.route("/resilient-touch")
def Resilient_Touch():
	return render_template("resilient-touch.html")

@app.route("/ultimate-mercy")
def Ultimate_Mercy():
	return render_template("ultimate-mercy.html")

@app.route("/vengeful-oath")
def Vengeful_Oath():
	return render_template("vengeful-oath.html")

@app.route("/litany-against-sloth")
def Litany_Against_Sloth():
	return render_template("litany-against-sloth.html")

@app.route("/litany-against-wrath")
def Litany_Against_Wrath():
	return render_template("litany-against-wrath.html")

@app.route("/litany-of-depravity")
def Litany_of_Depravity():
	return render_template("litany-of-depravity.html")

@app.route("/litany-of-righteousness")
def Litany_of_Righteousness():
	return render_template("litany-of-righteousness.html")

@app.route("/litany-of-self-interest")
def Litany_of_Self_Interest():
	return render_template("litany-of-self-interest.html")

@app.route("/exhort-the-faithful")
def Exhort_the_Faithful():
	return render_template("exhort-the-faithful.html")

@app.route("/battle-prayer")
def Battle_Prayer():
	return render_template("battle-prayer.html")

@app.route("/eternal-bane")
def Eternal_Bane():
	return render_template("eternal-bane.html")

@app.route("/touch-of-corruption")
def Touch_of_Corruption():
	return render_template("touch-of-corruption.html")

@app.route("/cruelty")
def Cruelty():
	return render_template("cruelty.html")

@app.route("/greater-cruelty")
def Greater_Cruelty():
	return render_template("greater-cruelty.html")

@app.route("/knight-reclaimant")
def Knight_Reclaimant():
	return render_template("knight-reclaimant.html")

@app.route("/lastwall-warden")
def Lastwall_Warden():
	return render_template("lastwall-warden.html")

@app.route("/suns-fury")
def Suns_Fury():
	return render_template("suns-fury.html")

@app.route("/smite-evil")
def Smite_Evil():
	return render_template("smite-evil.html")

@app.route("/smite-good")
def Smite_Good():
	return render_template("smite-good.html")

@app.route("/champions-sacrifice")
def Champions_Sacrifice():
	return render_template("champions-sacrifice.html")

@app.route("/invoke-the-crimson-oath")
def Invoke_the_Crimson_Oath():
	return render_template("invoke-the-crimson-oath.html")

@app.route("/stance")
def Stance():
	return render_template("stance.html")

@app.route("/anchoring-aura")
def Anchoring_Aura():
	return render_template("anchoring-aura.html")

@app.route("/aura-of-life")
def Aura_of_Life():
	return render_template("aura-of-life.html")

@app.route("/aura-of-preservation")
def Aura_of_Preservation():
	return render_template("aura-of-preservation.html")

@app.route("/enforce-oath")
def Enforce_Oath():
	return render_template("enforce-oath.html")

@app.route("/wyrmbane-aura")
def Wyrmbane_Aura():
	return render_template("wyrmbane-aura.html")

@app.route("/banishing-blow")
def Banishing_Blow():
	return render_template("banishing-blow.html")

@app.route("/destructive-vengeance")
def Destructive_Vengeance():
	return render_template("destructive-vengeance.html")

@app.route("/antipaladins-divine-smite")
def Antipaladins_Divine_Smite():
	return render_template("antipaladins-divine-smite.html")

@app.route("/divine-reflexes")
def Divine_Reflexes():
	return render_template("divine-reflexes.html")

@app.route("/gruesome-strike")
def Gruesome_Strike():
	return render_template("gruesome-strike.html")

@app.route("/iron-command")
def Iron_Command():
	return render_template("iron-command.html")

@app.route("/iron-repercussions")
def Iron_Repercussions():
	return render_template("iron-repercussions.html")

@app.route("/weight-of-guilt")
def Weight_of_Guilt():
	return render_template("weight-of-guilt.html")

@app.route("/lasting-doubt")
def Lasting_Doubt():
	return render_template("lasting-doubt.html")

@app.route("/liberating-step")
def Liberating_Step():
	return render_template("liberating-step.html")

@app.route("/liberating-oath")
def Liberating_Oath():
	return render_template("liberating-oath.html")

@app.route("/liberating-stride")
def Liberating_Stride():
	return render_template("liberating-stride.html")

@app.route("/liberating-divine-smite")
def Liberating_Divine_Smite():
	return render_template("liberating-divine-smite.html")

@app.route("/liberators-exalt")
def Liberators_Exalt():
	return render_template("liberators-exalt.html")

@app.route("/lightslayer-oath")
def Lightslayer_Oath():
	return render_template("lightslayer-oath.html")

@app.route("/selfish-shield")
def Selfish_Shield():
	return render_template("selfish-shield.html")

@app.route("/ongoing-selfishness")
def Ongoing_Selfishness():
	return render_template("ongoing-selfishness.html")

@app.route("/retributive-strike")
def Retributive_Strike():
	return render_template("retributive-strike.html")

@app.route("/paladins-divine-smite")
def Paladins_Divine_Smite():
	return render_template("paladins-divine-smite.html")

@app.route("/paladins-exalt")
def Paladins_Exalt():
	return render_template("paladins-exalt.html")

@app.route("/ranged-reprisal")
def Ranged_Reprisal():
	return render_template("ranged-reprisal.html")

@app.route("/redeemers-divine-smite")
def Redeemers_Divine_Smite():
	return render_template("redeemers-divine-smite.html")

@app.route("/redeemers-exalt")
def Redeemers_Exalt():
	return render_template("redeemers-exalt.html")

@app.route("/redemptive-oath")
def Redemptive_Oath():
	return render_template("redemptive-oath.html")

@app.route("/retributive-oath")
def Retributive_Oath():
	return render_template("retributive-oath.html")

@app.route("/tyrants-divine-smite")
def Tyrants_Divine_Smite():
	return render_template("tyrants-divine-smite.html")

@app.route("/tyrants-exalt")
def Tyrants_Exalt():
	return render_template("tyrants-exalt.html")

@app.route("/unimpeded-step")
def Unimpeded_Step():
	return render_template("unimpeded-step.html")

@app.route("/vicious-vengeance")
def Vicious_Vengeance():
	return render_template("vicious-vengeance.html")

@app.route("/instrument-of-slaughter")
def Instrument_of_Slaughter():
	return render_template("instrument-of-slaughter.html")

@app.route("/blade-of-justice")
def Blade_of_Justice():
	return render_template("blade-of-justice.html")

@app.route("/instrument-of-zeal")
def Instrument_of_Zeal():
	return render_template("instrument-of-zeal.html")

@app.route("/align-armament")
def Align_Armament():
	return render_template("align-armament.html")

@app.route("/blade-of-law")
def Blade_of_Law():
	return render_template("blade-of-law.html")

@app.route("/extend-align-armament")
def Extend_Align_Armament():
	return render_template("extend-align-armament.html")

@app.route("/aegis-of-arnisant")
def Aegis_of_Arnisant():
	return render_template("aegis-of-arnisant.html")

@app.route("/shield-ally")
def Shield_Ally():
	return render_template("shield-ally.html")

@app.route("/shield-paragon")
def Shield_Paragon():
	return render_template("shield-paragon.html")

@app.route("/corrupted-shield")
def Corrupted_Shield():
	return render_template("corrupted-shield.html")

@app.route("/blade-of-crimson-oath")
def Blade_of_Crimson_Oath():
	return render_template("blade-of-crimson-oath.html")

@app.route("/endure-deaths-touch")
def Endure_Deaths_Touch():
	return render_template("endure-deaths-touch.html")

@app.route("/lastwall-warden-2790495")
def Lastwall_Warden():
	return render_template("lastwall-warden-2790495.html")

@app.route("/reaper-of-repose")
def Reaper_of_Repose():
	return render_template("reaper-of-repose.html")

@app.route("/sunblade")
def Sunblade():
	return render_template("sunblade.html")

@app.route("/aura-of-vengeance")
def Aura_of_Vengeance():
	return render_template("aura-of-vengeance.html")

@app.route("/antipaladins-exalt")
def Antipaladins_Exalt():
	return render_template("antipaladins-exalt.html")

@app.route("/desecrators-divine-smite")
def Desecrators_Divine_Smite():
	return render_template("desecrators-divine-smite.html")

@app.route("/desecrators-exalt")
def Desecrators_Exalt():
	return render_template("desecrators-exalt.html")

@app.route("/aura-of-unbreakable-virtue")
def Aura_of_Unbreakable_Virtue():
	return render_template("aura-of-unbreakable-virtue.html")

@app.route("/a-home-in-every-port")
def A_Home_in_Every_Port():
	return render_template("a-home-in-every-port.html")

@app.route("/courtly-graces")
def Courtly_Graces():
	return render_template("courtly-graces.html")

@app.route("/connections")
def Connections():
	return render_template("connections.html")

@app.route("/streetwise")
def Streetwise():
	return render_template("streetwise.html")

@app.route("/criminal-connections")
def Criminal_Connections():
	return render_template("criminal-connections.html")

@app.route("/quick-contacts")
def Quick_Contacts():
	return render_template("quick-contacts.html")

@app.route("/settlement-scholastics")
def Settlement_Scholastics():
	return render_template("settlement-scholastics.html")

@app.route("/underground-network")
def Underground_Network():
	return render_template("underground-network.html")

@app.route("/glean-contents")
def Glean_Contents():
	return render_template("glean-contents.html")

@app.route("/legendary-codebreaker")
def Legendary_Codebreaker():
	return render_template("legendary-codebreaker.html")

@app.route("/multilingual-cypher")
def Multilingual_Cypher():
	return render_template("multilingual-cypher.html")

@app.route("/scholastic-contextualization")
def Scholastic_Contextualization():
	return render_template("scholastic-contextualization.html")

@app.route("/prescient-consumable")
def Prescient_Consumable():
	return render_template("prescient-consumable.html")

@app.route("/predictive-purchaser")
def Predictive_Purchaser():
	return render_template("predictive-purchaser.html")

@app.route("/prescient-planner")
def Prescient_Planner():
	return render_template("prescient-planner.html")

@app.route("/wealth-domain-precious-metals")
def Wealth_Domain__Precious_Metals():
	return render_template("wealth-domain-precious-metals.html")

@app.route("/wealth-domain-appearance-of-wealth-6497474")
def Wealth_Domain__Appearance_of_Wealth():
	return render_template("wealth-domain-appearance-of-wealth-6497474.html")

@app.route("/cities-domain-face-in-the-crowd")
def Cities_Domain__Face_in_the_Crowd():
	return render_template("cities-domain-face-in-the-crowd.html")

@app.route("/cities-of-domain-pulse-of-the-city")
def Cities_of_Domain__Pulse_of_the_City():
	return render_template("cities-of-domain-pulse-of-the-city.html")

@app.route("/hireling-manager")
def Hireling_Manager():
	return render_template("hireling-manager.html")

@app.route("/archeologist")
def Archeologist():
	return render_template("archeologist.html")

@app.route("/scholastic-identification")
def Scholastic_Identification():
	return render_template("scholastic-identification.html")

@app.route("/biographical-eye")
def Biographical_Eye():
	return render_template("biographical-eye.html")

@app.route("/crude-communication")
def Crude_Communication():
	return render_template("crude-communication.html")

@app.route("/multilingual")
def Multilingual():
	return render_template("multilingual.html")

@app.route("/legendary-linguist")
def Legendary_Linguist():
	return render_template("legendary-linguist.html")

@app.route("/phonetic-training")
def Phonetic_Training():
	return render_template("phonetic-training.html")

@app.route("/read-lips")
def Read_Lips():
	return render_template("read-lips.html")

@app.route("/sign-language")
def Sign_Language():
	return render_template("sign-language.html")

@app.route("/city-guard")
def City_Guard():
	return render_template("city-guard.html")

@app.route("/know-the-beat")
def Know_the_Beat():
	return render_template("know-the-beat.html")

@app.route("/eye-for-numbers")
def Eye_for_Numbers():
	return render_template("eye-for-numbers.html")

@app.route("/accustomization")
def Accustomization():
	return render_template("accustomization.html")

@app.route("/party-crasher")
def Party_Crasher():
	return render_template("party-crasher.html")

@app.route("/read-shibboleths")
def Read_Shibboleths():
	return render_template("read-shibboleths.html")

@app.route("/implausible-purchase")
def Implausible_Purchase():
	return render_template("implausible-purchase.html")

@app.route("/society-feats")
def Society_Feats():
	return render_template("society-feats.html")

@app.route("/retain-absorbed-spell")
def Retain_Absorbed_Spell():
	return render_template("retain-absorbed-spell.html")

@app.route("/bond-conservation")
def Bond_Conservation():
	return render_template("bond-conservation.html")

@app.route("/call-bonded-item")
def Call_Bonded_Item():
	return render_template("call-bonded-item.html")

@app.route("/superior-bond")
def Superior_Bond():
	return render_template("superior-bond.html")

@app.route("/familiars-language")
def Familiars_Language():
	return render_template("familiars-language.html")

@app.route("/improved-familiar-attunement")
def Improved_Familiar_Attunement():
	return render_template("improved-familiar-attunement.html")

@app.route("/charged-creation")
def Charged_Creation():
	return render_template("charged-creation.html")

@app.route("/familiar-conduit")
def Familiar_Conduit():
	return render_template("familiar-conduit.html")

@app.route("/improved-familiar")
def Improved_Familiar():
	return render_template("improved-familiar.html")

@app.route("/incredible-familiar")
def Incredible_Familiar():
	return render_template("incredible-familiar.html")

@app.route("/baba-yagas-patronage")
def Baba_Yagas_Patronage():
	return render_template("baba-yagas-patronage.html")

@app.route("/familiar-mascot")
def Familiar_Mascot():
	return render_template("familiar-mascot.html")

@app.route("/leshy-familiar-secrets")
def Leshy_Familiar_Secrets():
	return render_template("leshy-familiar-secrets.html")

@app.route("/mask-familiar")
def Mask_Familiar():
	return render_template("mask-familiar.html")

@app.route("/mutable-familiar")
def Mutable_Familiar():
	return render_template("mutable-familiar.html")

@app.route("/halcyon-speaker")
def Halcyon_Speaker():
	return render_template("halcyon-speaker.html")

@app.route("/cascade-bearers-spellcasting")
def Cascade_Bearers_Spellcasting():
	return render_template("cascade-bearers-spellcasting.html")

@app.route("/dualistic-synergy")
def Dualistic_Synergy():
	return render_template("dualistic-synergy.html")

@app.route("/fulminating-synergy")
def Fulminating_Synergy():
	return render_template("fulminating-synergy.html")

@app.route("/shared-synergy")
def Shared_Synergy():
	return render_template("shared-synergy.html")

@app.route("/synergistic-spell")
def Synergistic_Spell():
	return render_template("synergistic-spell.html")

@app.route("/harming-hands")
def Harming_Hands():
	return render_template("harming-hands.html")

@app.route("/improved-command-undead")
def Improved_Command_Undead():
	return render_template("improved-command-undead.html")

@app.route("/necrotic-infusion")
def Necrotic_Infusion():
	return render_template("necrotic-infusion.html")

@app.route("/sap-life")
def Sap_Life():
	return render_template("sap-life.html")

@app.route("/vile-desecration")
def Vile_Desecration():
	return render_template("vile-desecration.html")

@app.route("/healing-hands")
def Healing_Hands():
	return render_template("healing-hands.html")

@app.route("/turn-undead")
def Turn_Undead():
	return render_template("turn-undead.html")

@app.route("/cremate-undead")
def Cremate_Undead():
	return render_template("cremate-undead.html")

@app.route("/denier-of-destruction")
def Denier_of_Destruction():
	return render_template("denier-of-destruction.html")

@app.route("/heroic-recovery")
def Heroic_Recovery():
	return render_template("heroic-recovery.html")

@app.route("/holy-castigation")
def Holy_Castigation():
	return render_template("holy-castigation.html")

@app.route("/castigating-weapon")
def Castigating_Weapon():
	return render_template("castigating-weapon.html")

@app.route("/improved-communal-healing")
def Improved_Communal_Healing():
	return render_template("improved-communal-healing.html")

@app.route("/radiant-infusion")
def Radiant_Infusion():
	return render_template("radiant-infusion.html")

@app.route("/cast-down")
def Cast_Down():
	return render_template("cast-down.html")

@app.route("/channel-smite")
def Channel_Smite():
	return render_template("channel-smite.html")

@app.route("/defensive-recovery")
def Defensive_Recovery():
	return render_template("defensive-recovery.html")

@app.route("/directed-channel")
def Directed_Channel():
	return render_template("directed-channel.html")

@app.route("/echoing-channel")
def Echoing_Channel():
	return render_template("echoing-channel.html")

@app.route("/fast-channel")
def Fast_Channel():
	return render_template("fast-channel.html")

@app.route("/metamagic-channel")
def Metamagic_Channel():
	return render_template("metamagic-channel.html")

@app.route("/blood-component")
def Blood_Component():
	return render_template("blood-component.html")

@app.route("/effortless-concentration")
def Effortless_Concentration():
	return render_template("effortless-concentration.html")

@app.route("/eschew-materials")
def Eschew_Materials():
	return render_template("eschew-materials.html")

@app.route("/spell-penetration")
def Spell_Penetration():
	return render_template("spell-penetration.html")

@app.route("/steady-spellcasting")
def Steady_Spellcasting():
	return render_template("steady-spellcasting.html")

@app.route("/ward-casting")
def Ward_Casting():
	return render_template("ward-casting.html")

@app.route("/aberrant-bloodline-focus-aberrant-whispers")
def Aberrant_Bloodline_Focus__Aberrant_Whispers():
	return render_template("aberrant-bloodline-focus-aberrant-whispers.html")

@app.route("/ancestral-blood-magic")
def Ancestral_Blood_Magic():
	return render_template("ancestral-blood-magic.html")

@app.route("/anoint-ally")
def Anoint_Ally():
	return render_template("anoint-ally.html")

@app.route("/bloodline-metamorphasis")
def Bloodline_Metamorphasis():
	return render_template("bloodline-metamorphasis.html")

@app.route("/bloodline-mutation")
def Bloodline_Mutation():
	return render_template("bloodline-mutation.html")

@app.route("/demonic-bloodline")
def Demonic_Bloodline():
	return render_template("demonic-bloodline.html")

@app.route("/angelic-bloodline")
def Angelic_Bloodline():
	return render_template("angelic-bloodline.html")

@app.route("/diabolic-bloodline")
def Diabolic_Bloodline():
	return render_template("diabolic-bloodline.html")

@app.route("/draconic-bloodline")
def Draconic_Bloodline():
	return render_template("draconic-bloodline.html")

@app.route("/elemental-bloodline")
def Elemental_Bloodline():
	return render_template("elemental-bloodline.html")

@app.route("/entreat-the-forbearers")
def Entreat_the_Forbearers():
	return render_template("entreat-the-forbearers.html")

@app.route("/fey-bloodline")
def Fey_Bloodline():
	return render_template("fey-bloodline.html")

@app.route("/genie-bloodline")
def Genie_Bloodline():
	return render_template("genie-bloodline.html")

@app.route("/hag-bloodline")
def Hag_Bloodline():
	return render_template("hag-bloodline.html")

@app.route("/imperial-bloodline")
def Imperial_Bloodline():
	return render_template("imperial-bloodline.html")

@app.route("/nymph-bloodline")
def Nymph_Bloodline():
	return render_template("nymph-bloodline.html")

@app.route("/occult-evolution")
def Occult_Evolution():
	return render_template("occult-evolution.html")

@app.route("/pscyhopomp-bloodline")
def Pscyhopomp_Bloodline():
	return render_template("pscyhopomp-bloodline.html")

@app.route("/shadow-bloodline")
def Shadow_Bloodline():
	return render_template("shadow-bloodline.html")

@app.route("/tenacious-blood-magic")
def Tenacious_Blood_Magic():
	return render_template("tenacious-blood-magic.html")

@app.route("/undead-bloodline")
def Undead_Bloodline():
	return render_template("undead-bloodline.html")

@app.route("/bespell-weapon")
def Bespell_Weapon():
	return render_template("bespell-weapon.html")

@app.route("/diverting-vortex")
def Diverting_Vortex():
	return render_template("diverting-vortex.html")

@app.route("/divine-weapon")
def Divine_Weapon():
	return render_template("divine-weapon.html")

@app.route("/verdant-weapon")
def Verdant_Weapon():
	return render_template("verdant-weapon.html")

@app.route("/pristine-weapon")
def Pristine_Weapon():
	return render_template("pristine-weapon.html")

@app.route("/replenishment-of-war")
def Replenishment_of_War():
	return render_template("replenishment-of-war.html")

@app.route("/shared-replenishment")
def Shared_Replenishment():
	return render_template("shared-replenishment.html")

@app.route("/conceal-spell")
def Conceal_Spell():
	return render_template("conceal-spell.html")

@app.route("/current-spell")
def Current_Spell():
	return render_template("current-spell.html")

@app.route("/forcible-energy")
def Forcible_Energy():
	return render_template("forcible-energy.html")

@app.route("/melodious-spell")
def Melodious_Spell():
	return render_template("melodious-spell.html")

@app.route("/metamagical-experimentation")
def Metamagical_Experimentation():
	return render_template("metamagical-experimentation.html")

@app.route("/overwhelming-energy")
def Overwhelming_Energy():
	return render_template("overwhelming-energy.html")

@app.route("/primal-summons")
def Primal_Summons():
	return render_template("primal-summons.html")

@app.route("/quickened-casting")
def Quickened_Casting():
	return render_template("quickened-casting.html")

@app.route("/reach-spell")
def Reach_Spell():
	return render_template("reach-spell.html")

@app.route("/redirection")
def Redirection():
	return render_template("redirection.html")

@app.route("/spiritual-infusion")
def Spiritual_Infusion():
	return render_template("spiritual-infusion.html")

@app.route("/split-shot")
def Split_Shot():
	return render_template("split-shot.html")

@app.route("/surreptitious-spellcasting")
def Surreptitious_Spellcasting():
	return render_template("surreptitious-spellcasting.html")

@app.route("/through-spell")
def Through_Spell():
	return render_template("through-spell.html")

@app.route("/widen-spell")
def Widen_Spell():
	return render_template("widen-spell.html")

@app.route("/echoing-spell")
def Echoing_Spell():
	return render_template("echoing-spell.html")

@app.route("/energy-ablation")
def Energy_Ablation():
	return render_template("energy-ablation.html")

@app.route("/energy-fusion")
def Energy_Fusion():
	return render_template("energy-fusion.html")

@app.route("/portentous-spell")
def Portentous_Spell():
	return render_template("portentous-spell.html")

@app.route("/recover-spell")
def Recover_Spell():
	return render_template("recover-spell.html")

@app.route("/safeguard-spell")
def Safeguard_Spell():
	return render_template("safeguard-spell.html")

@app.route("/scintillating-spell")
def Scintillating_Spell():
	return render_template("scintillating-spell.html")

@app.route("/silent-spell")
def Silent_Spell():
	return render_template("silent-spell.html")

@app.route("/sow-spell")
def Sow_Spell():
	return render_template("sow-spell.html")

@app.route("/spell-relay")
def Spell_Relay():
	return render_template("spell-relay.html")

@app.route("/spell-shroud")
def Spell_Shroud():
	return render_template("spell-shroud.html")

@app.route("/terraforming-spell")
def Terraforming_Spell():
	return render_template("terraforming-spell.html")

@app.route("/pesh-skin")
def Pesh_Skin():
	return render_template("pesh-skin.html")

@app.route("/divine-aegis")
def Divine_Aegis():
	return render_template("divine-aegis.html")

@app.route("/energy-ward")
def Energy_Ward():
	return render_template("energy-ward.html")

@app.route("/energetic-resonance")
def Energetic_Resonance():
	return render_template("energetic-resonance.html")

@app.route("/diviner-sense")
def Diviner_Sense():
	return render_template("diviner-sense.html")

@app.route("/cantrip-expansion")
def Cantrip_Expansion():
	return render_template("cantrip-expansion.html")

@app.route("/ancestral-mage")
def Ancestral_Mage():
	return render_template("ancestral-mage.html")

@app.route("/crossblood-evolution")
def Crossblood_Evolution():
	return render_template("crossblood-evolution.html")

@app.route("/mysterious-repertoire")
def Mysterious_Repertoire():
	return render_template("mysterious-repertoire.html")

@app.route("/greater-crossblood-evolution")
def Greater_Crossblood_Evolution():
	return render_template("greater-crossblood-evolution.html")

@app.route("/communal-sustain")
def Communal_Sustain():
	return render_template("communal-sustain.html")

@app.route("/witchs-charge")
def Witchs_Charge():
	return render_template("witchs-charge.html")

@app.route("/witchs-communion")
def Witchs_Communion():
	return render_template("witchs-communion.html")

@app.route("/linked-focus")
def Linked_Focus():
	return render_template("linked-focus.html")

@app.route("/universalist")
def Universalist():
	return render_template("universalist.html")

@app.route("/familiars-eyes")
def Familiars_Eyes():
	return render_template("familiars-eyes.html")

@app.route("/ebb-and-flow")
def Ebb_and_Flow():
	return render_template("ebb-and-flow.html")

@app.route("/martyr")
def Martyr():
	return render_template("martyr.html")

@app.route("/remediate")
def Remediate():
	return render_template("remediate.html")

@app.route("/psychopomp-bloodline")
def Psychopomp_Bloodline():
	return render_template("psychopomp-bloodline.html")

@app.route("/dangerous-sorcery")
def Dangerous_Sorcery():
	return render_template("dangerous-sorcery.html")

@app.route("/surging-might")
def Surging_Might():
	return render_template("surging-might.html")

@app.route("/nonlethal-spell")
def Nonlethal_Spell():
	return render_template("nonlethal-spell.html")

@app.route("/verdant-presence")
def Verdant_Presence():
	return render_template("verdant-presence.html")

@app.route("/pinpoint-poisoner")
def Pinpoint_Poisoner():
	return render_template("pinpoint-poisoner.html")

@app.route("/noisy")
def Noisy():
	return render_template("noisy.html")

@app.route("/armored-stealth")
def Armored_Stealth():
	return render_template("armored-stealth.html")

@app.route("/lost-in-the-crowd")
def Lost_in_the_Crowd():
	return render_template("lost-in-the-crowd.html")

@app.route("/crowd-mastery")
def Crowd_Mastery():
	return render_template("crowd-mastery.html")

@app.route("/light")
def Light():
	return render_template("light.html")

@app.route("/darkness-domain-cloak-of-shadow")
def Darkness_Domain__Cloak_of_Shadow():
	return render_template("darkness-domain-cloak-of-shadow.html")

@app.route("/darkness-domain-darkened-eyes")
def Darkness_Domain__Darkened_Eyes():
	return render_template("darkness-domain-darkened-eyes.html")

@app.route("/secrecy-domain-forced-quiet")
def Secrecy_Domain__Forced_Quiet():
	return render_template("secrecy-domain-forced-quiet.html")

@app.route("/secrecy-domain-safeguard-secret")
def Secrecy_Domain__Safeguard_Secret():
	return render_template("secrecy-domain-safeguard-secret.html")

@app.route("/shadow-magic-shadow-jump")
def Shadow_Magic__Shadow_Jump():
	return render_template("shadow-magic-shadow-jump.html")

@app.route("/fanes-escape")
def Fanes_Escape():
	return render_template("fanes-escape.html")

@app.route("/senses")
def Senses():
	return render_template("senses.html")

@app.route("/foil-senses")
def Foil_Senses():
	return render_template("foil-senses.html")

@app.route("/sneak-savant")
def Sneak_Savant():
	return render_template("sneak-savant.html")

@app.route("/fleeting-shadow")
def Fleeting_Shadow():
	return render_template("fleeting-shadow.html")

@app.route("/swift-sneak")
def Swift_Sneak():
	return render_template("swift-sneak.html")

@app.route("/tactical-entry")
def Tactical_Entry():
	return render_template("tactical-entry.html")

@app.route("/shadowdancer")
def Shadowdancer():
	return render_template("shadowdancer.html")

@app.route("/experienced-smuggler")
def Experienced_Smuggler():
	return render_template("experienced-smuggler.html")

@app.route("/shadow-mark")
def Shadow_Mark():
	return render_template("shadow-mark.html")

@app.route("/ambushing-knockdown")
def Ambushing_Knockdown():
	return render_template("ambushing-knockdown.html")

@app.route("/scouts-pounce")
def Scouts_Pounce():
	return render_template("scouts-pounce.html")

@app.route("/startling-appearance")
def Startling_Appearance():
	return render_template("startling-appearance.html")

@app.route("/stunning-appearance")
def Stunning_Appearance():
	return render_template("stunning-appearance.html")

@app.route("/frightening-appearance")
def Frightening_Appearance():
	return render_template("frightening-appearance.html")

@app.route("/subtle-shank")
def Subtle_Shank():
	return render_template("subtle-shank.html")

@app.route("/quiet-allies")
def Quiet_Allies():
	return render_template("quiet-allies.html")

@app.route("/underhanded-assault")
def Underhanded_Assault():
	return render_template("underhanded-assault.html")

@app.route("/shadow-hunter")
def Shadow_Hunter():
	return render_template("shadow-hunter.html")

@app.route("/terrain-stalker-2875549")
def Terrain_Stalker():
	return render_template("terrain-stalker-2875549.html")

@app.route("/terrain-scout")
def Terrain_Scout():
	return render_template("terrain-scout.html")

@app.route("/wardens-step")
def Wardens_Step():
	return render_template("wardens-step.html")

@app.route("/legendary-sneak")
def Legendary_Sneak():
	return render_template("legendary-sneak.html")

@app.route("/spring-from-the-shadows")
def Spring_From_the_Shadows():
	return render_template("spring-from-the-shadows.html")

@app.route("/camouflage")
def Camouflage():
	return render_template("camouflage.html")

@app.route("/stealth-feats")
def Stealth_Feats():
	return render_template("stealth-feats.html")

@app.route("/lesson-of-snow")
def Lesson_of_Snow():
	return render_template("lesson-of-snow.html")

@app.route("/afflictions")
def Afflictions():
	return render_template("afflictions.html")

@app.route("/lesson-of-death")
def Lesson_of_Death():
	return render_template("lesson-of-death.html")

@app.route("/lesson-of-renewal")
def Lesson_of_Renewal():
	return render_template("lesson-of-renewal.html")

@app.route("/lumberjack")
def Lumberjack():
	return render_template("lumberjack.html")

@app.route("/natures-edge")
def Natures_Edge():
	return render_template("natures-edge.html")

@app.route("/survey-wildlife")
def Survey_Wildlife():
	return render_template("survey-wildlife.html")

@app.route("/wild-stride")
def Wild_Stride():
	return render_template("wild-stride.html")

@app.route("/favored-terrain")
def Favored_Terrain():
	return render_template("favored-terrain.html")

@app.route("/acclimatization")
def Acclimatization():
	return render_template("acclimatization.html")

@app.route("/horizon-walker")
def Horizon_Walker():
	return render_template("horizon-walker.html")

@app.route("/perpetual-scout")
def Perpetual_Scout():
	return render_template("perpetual-scout.html")

@app.route("/sure-foot")
def Sure_Foot():
	return render_template("sure-foot.html")

@app.route("/terrain-expertise")
def Terrain_Expertise():
	return render_template("terrain-expertise.html")

@app.route("/terrain-mastery")
def Terrain_Mastery():
	return render_template("terrain-mastery.html")

@app.route("/ephemeral-tracking")
def Ephemeral_Tracking():
	return render_template("ephemeral-tracking.html")

@app.route("/environmental-grace")
def Environmental_Grace():
	return render_template("environmental-grace.html")

@app.route("/planar-survival")
def Planar_Survival():
	return render_template("planar-survival.html")

@app.route("/survival-of-desolation")
def Survival_of_Desolation():
	return render_template("survival-of-desolation.html")

@app.route("/wandering-oasis")
def Wandering_Oasis():
	return render_template("wandering-oasis.html")

@app.route("/axe-climber")
def Axe_Climber():
	return render_template("axe-climber.html")

@app.route("/legendary-guide")
def Legendary_Guide():
	return render_template("legendary-guide.html")

@app.route("/pirate")
def Pirate():
	return render_template("pirate.html")

@app.route("/rope-runner")
def Rope_Runner():
	return render_template("rope-runner.html")

@app.route("/wild-stride-3036686")
def Wild_Stride():
	return render_template("wild-stride-3036686.html")

@app.route("/ultimate-skirmisher")
def Ultimate_Skirmisher():
	return render_template("ultimate-skirmisher.html")

@app.route("/woodland-stride")
def Woodland_Stride():
	return render_template("woodland-stride.html")

@app.route("/storm-born")
def Storm_Born():
	return render_template("storm-born.html")

@app.route("/wilderness-spotter")
def Wilderness_Spotter():
	return render_template("wilderness-spotter.html")

@app.route("/wortwitch")
def Wortwitch():
	return render_template("wortwitch.html")

@app.route("/forager")
def Forager():
	return render_template("forager.html")

@app.route("/rain-scribe-sustenance")
def Rain_Scribe_Sustenance():
	return render_template("rain-scribe-sustenance.html")

@app.route("/rugged-survivalist")
def Rugged_Survivalist():
	return render_template("rugged-survivalist.html")

@app.route("/experienced-tracker")
def Experienced_Tracker():
	return render_template("experienced-tracker.html")

@app.route("/swift-tracker")
def Swift_Tracker():
	return render_template("swift-tracker.html")

@app.route("/trackless-step")
def Trackless_Step():
	return render_template("trackless-step.html")

@app.route("/dead-reckoning")
def Dead_Reckoning():
	return render_template("dead-reckoning.html")

@app.route("/terrain-transposition")
def Terrain_Transposition():
	return render_template("terrain-transposition.html")

@app.route("/environmental-explorer")
def Environmental_Explorer():
	return render_template("environmental-explorer.html")

@app.route("/survival-feats")
def Survival_Feats():
	return render_template("survival-feats.html")

@app.route("/slice-and-swipe")
def Slice_and_Swipe():
	return render_template("slice-and-swipe.html")

@app.route("/stab-and-snag")
def Stab_and_Snag():
	return render_template("stab-and-snag.html")

@app.route("/quick-unlock")
def Quick_Unlock():
	return render_template("quick-unlock.html")

@app.route("/concealed-legerdemain")
def Concealed_Legerdemain():
	return render_template("concealed-legerdemain.html")

@app.route("/pickpocket")
def Pickpocket():
	return render_template("pickpocket.html")

@app.route("/plant-evidence")
def Plant_Evidence():
	return render_template("plant-evidence.html")

@app.route("/legendary-thief")
def Legendary_Thief():
	return render_template("legendary-thief.html")

@app.route("/steal-spell")
def Steal_Spell():
	return render_template("steal-spell.html")

@app.route("/steal-essence")
def Steal_Essence():
	return render_template("steal-essence.html")

@app.route("/subtle-theft")
def Subtle_Theft():
	return render_template("subtle-theft.html")

@app.route("/sabotage")
def Sabotage():
	return render_template("sabotage.html")

@app.route("/careful-explorer")
def Careful_Explorer():
	return render_template("careful-explorer.html")

@app.route("/delay-trap")
def Delay_Trap():
	return render_template("delay-trap.html")

@app.route("/everyone-duck")
def Everyone_Duck():
	return render_template("everyone-duck.html")

@app.route("/gifted-disarmer")
def Gifted_Disarmer():
	return render_template("gifted-disarmer.html")

@app.route("/trapbreakers-luck")
def Trapbreakers_Luck():
	return render_template("trapbreakers-luck.html")

@app.route("/wary-disarmament")
def Wary_Disarmament():
	return render_template("wary-disarmament.html")

@app.route("/cartwheel-dodge")
def Cartwheel_Dodge():
	return render_template("cartwheel-dodge.html")

@app.route("/daring-act")
def Daring_Act():
	return render_template("daring-act.html")

@app.route("/daredevils-gambit")
def Daredevils_Gambit():
	return render_template("daredevils-gambit.html")

@app.route("/daring-flourish")
def Daring_Flourish():
	return render_template("daring-flourish.html")

@app.route("/furious-sprint")
def Furious_Sprint():
	return render_template("furious-sprint.html")

@app.route("/light-step-1100854")
def Light_Step():
	return render_template("light-step-1100854.html")

@app.route("/swift-elusion")
def Swift_Elusion():
	return render_template("swift-elusion.html")

@app.route("/acrobatics-class-feats")
def Acrobatics_Class_Feats():
	return render_template("acrobatics-class-feats.html")

@app.route("/armigers-mobility")
def Armigers_Mobility():
	return render_template("armigers-mobility.html")

@app.route("/armor-assist")
def Armor_Assist():
	return render_template("armor-assist.html")

@app.route("/armor-specialist")
def Armor_Specialist():
	return render_template("armor-specialist.html")

@app.route("/armored-rebuff")
def Armored_Rebuff():
	return render_template("armored-rebuff.html")

@app.route("/bulwark")
def Bulwark():
	return render_template("bulwark.html")

@app.route("/mighty-bulwark")
def Mighty_Bulwark():
	return render_template("mighty-bulwark.html")

@app.route("/greater-interpose")
def Greater_Interpose():
	return render_template("greater-interpose.html")

@app.route("/overpowering-charge")
def Overpowering_Charge():
	return render_template("overpowering-charge.html")

@app.route("/mobility")
def Mobility():
	return render_template("mobility.html")

@app.route("/guarded-movement")
def Guarded_Movement():
	return render_template("guarded-movement.html")

@app.route("/brutal-bully")
def Brutal_Bully():
	return render_template("brutal-bully.html")

@app.route("/sudden-charge")
def Sudden_Charge():
	return render_template("sudden-charge.html")

@app.route("/no-escape")
def No_Escape():
	return render_template("no-escape.html")

@app.route("/ship-to-ship")
def Ship_to_Ship():
	return render_template("ship-to-ship.html")

@app.route("/sudden-leap")
def Sudden_Leap():
	return render_template("sudden-leap.html")

@app.route("/winding-flow")
def Winding_Flow():
	return render_template("winding-flow.html")

@app.route("/determined-dash")
def Determined_Dash():
	return render_template("determined-dash.html")

@app.route("/farabellas-flip")
def Farabellas_Flip():
	return render_template("farabellas-flip.html")

@app.route("/brutal-critical")
def Brutal_Critical():
	return render_template("brutal-critical.html")

@app.route("/savage-critical")
def Savage_Critical():
	return render_template("savage-critical.html")

@app.route("/unbalancing-blow")
def Unbalancing_Blow():
	return render_template("unbalancing-blow.html")

@app.route("/sidestep")
def Sidestep():
	return render_template("sidestep.html")

@app.route("/spring-attack")
def Spring_Attack():
	return render_template("spring-attack.html")

@app.route("/great-cleave")
def Great_Cleave():
	return render_template("great-cleave.html")

@app.route("/quick-reversal")
def Quick_Reversal():
	return render_template("quick-reversal.html")

@app.route("/swipe")
def Swipe():
	return render_template("swipe.html")

@app.route("/whirlwind-strike")
def Whirlwind_Strike():
	return render_template("whirlwind-strike.html")

@app.route("/disarming-assault")
def Disarming_Assault():
	return render_template("disarming-assault.html")

@app.route("/disarming-flair")
def Disarming_Flair():
	return render_template("disarming-flair.html")

@app.route("/relentless-disarm")
def Relentless_Disarm():
	return render_template("relentless-disarm.html")

@app.route("/quick-draw")
def Quick_Draw():
	return render_template("quick-draw.html")

@app.route("/ultimate-flexibility")
def Ultimate_Flexibility():
	return render_template("ultimate-flexibility.html")

@app.route("/deny-support")
def Deny_Support():
	return render_template("deny-support.html")

@app.route("/overextending-feint")
def Overextending_Feint():
	return render_template("overextending-feint.html")

@app.route("/scoundrel")
def Scoundrel():
	return render_template("scoundrel.html")

@app.route("/scouts-charge")
def Scouts_Charge():
	return render_template("scouts-charge.html")

@app.route("/gravity-weapon")
def Gravity_Weapon():
	return render_template("gravity-weapon.html")

@app.route("/zeal-domain-weapon-surge")
def Zeal_Domain__Weapon_Surge():
	return render_template("zeal-domain-weapon-surge.html")

@app.route("/felling-strike")
def Felling_Strike():
	return render_template("felling-strike.html")

@app.route("/mobile-magical-combat")
def Mobile_Magical_Combat():
	return render_template("mobile-magical-combat.html")

@app.route("/combat-grab")
def Combat_Grab():
	return render_template("combat-grab.html")

@app.route("/crushing-grab")
def Crushing_Grab():
	return render_template("crushing-grab.html")

@app.route("/dazing-blow")
def Dazing_Blow():
	return render_template("dazing-blow.html")

@app.route("/embrace-the-pain")
def Embrace_the_Pain():
	return render_template("embrace-the-pain.html")

@app.route("/furious-grab")
def Furious_Grab():
	return render_template("furious-grab.html")

@app.route("/impaling-thrust")
def Impaling_Thrust():
	return render_template("impaling-thrust.html")

@app.route("/collateral-dash")
def Collateral_Dash():
	return render_template("collateral-dash.html")

@app.route("/whirling-throw")
def Whirling_Throw():
	return render_template("whirling-throw.html")

@app.route("/battle-planner")
def Battle_Planner():
	return render_template("battle-planner.html")

@app.route("/zeal-domain-zeal-for-battle")
def Zeal_Domain__Zeal_for_Battle():
	return render_template("zeal-domain-zeal-for-battle.html")

@app.route("/surprise-attack")
def Surprise_Attack():
	return render_template("surprise-attack.html")

@app.route("/swaggering-initiative")
def Swaggering_Initiative():
	return render_template("swaggering-initiative.html")

@app.route("/dread-striker")
def Dread_Striker():
	return render_template("dread-striker.html")

@app.route("/fearsome-brute")
def Fearsome_Brute():
	return render_template("fearsome-brute.html")

@app.route("/intimidating-strike")
def Intimidating_Strike():
	return render_template("intimidating-strike.html")

@app.route("/deadly-grace")
def Deadly_Grace():
	return render_template("deadly-grace.html")

@app.route("/devastator")
def Devastator():
	return render_template("devastator.html")

@app.route("/furious-focus")
def Furious_Focus():
	return render_template("furious-focus.html")

@app.route("/certain-strike")
def Certain_Strike():
	return render_template("certain-strike.html")

@app.route("/exacting-strike")
def Exacting_Strike():
	return render_template("exacting-strike.html")

@app.route("/follow-up-assault")
def Follow_Up_Assault():
	return render_template("follow-up-assault.html")

@app.route("/perfected-form")
def Perfected_Form():
	return render_template("perfected-form.html")

@app.route("/overwhelming-blow")
def Overwhelming_Blow():
	return render_template("overwhelming-blow.html")

@app.route("/death")
def Death():
	return render_template("death.html")

@app.route("/angel-of-death")
def Angel_of_Death():
	return render_template("angel-of-death.html")

@app.route("/assassinate")
def Assassinate():
	return render_template("assassinate.html")

@app.route("/expert-backstabber")
def Expert_Backstabber():
	return render_template("expert-backstabber.html")

@app.route("/lunging-stance")
def Lunging_Stance():
	return render_template("lunging-stance.html")

@app.route("/combat-reflexes")
def Combat_Reflexes():
	return render_template("combat-reflexes.html")

@app.route("/desperate-finisher")
def Desperate_Finisher():
	return render_template("desperate-finisher.html")

@app.route("/disorienting-opening")
def Disorienting_Opening():
	return render_template("disorienting-opening.html")

@app.route("/disruptive-stance")
def Disruptive_Stance():
	return render_template("disruptive-stance.html")

@app.route("/felicitous-riposte")
def Felicitous_Riposte():
	return render_template("felicitous-riposte.html")

@app.route("/impassible-wall-stance")
def Impassible_Wall_Stance():
	return render_template("impassible-wall-stance.html")

@app.route("/impossible-riposte")
def Impossible_Riposte():
	return render_template("impossible-riposte.html")

@app.route("/opportune-backstab")
def Opportune_Backstab():
	return render_template("opportune-backstab.html")

@app.route("/reactive-interference")
def Reactive_Interference():
	return render_template("reactive-interference.html")

@app.route("/reflexive-riposte")
def Reflexive_Riposte():
	return render_template("reflexive-riposte.html")

@app.route("/stand-still")
def Stand_Still():
	return render_template("stand-still.html")

@app.route("/stay-down")
def Stay_Down():
	return render_template("stay-down.html")

@app.route("/achaekeks-grip")
def Achaekeks_Grip():
	return render_template("achaekeks-grip.html")

@app.route("/achaekeks-sense")
def Achaekeks_sense():
	return render_template("achaekeks-sense.html")

@app.route("/fading")
def Fading():
	return render_template("fading.html")

@app.route("/vernai-training")
def Vernai_Training():
	return render_template("vernai-training.html")

@app.route("/blind-fight")
def Blind_Fight():
	return render_template("blind-fight.html")

@app.route("/revealing-stab")
def Revealing_Stab():
	return render_template("revealing-stab.html")

@app.route("/awesome-blow")
def Awesome_Blow():
	return render_template("awesome-blow.html")

@app.route("/shove-down")
def Shove_Down():
	return render_template("shove-down.html")

@app.route("/annihilating-swing")
def Annihilating_Swing():
	return render_template("annihilating-swing.html")

@app.route("/brutal-beating")
def Brutal_Beating():
	return render_template("brutal-beating.html")

@app.route("/demanding-challenge")
def Demanding_Challenge():
	return render_template("demanding-challenge.html")

@app.route("/harrying-strike")
def Harrying_Strike():
	return render_template("harrying-strike.html")

@app.route("/head-stomp")
def Head_Stomp():
	return render_template("head-stomp.html")

@app.route("/instant-opening")
def Instant_Opening():
	return render_template("instant-opening.html")

@app.route("/master-strike")
def Master_Strike():
	return render_template("master-strike.html")

@app.route("/resounding-blow")
def Resounding_Blow():
	return render_template("resounding-blow.html")

@app.route("/snagging-strike")
def Snagging_Strike():
	return render_template("snagging-strike.html")

@app.route("/murderers-circle")
def Murderers_Circle():
	return render_template("murderers-circle.html")

@app.route("/vivacious-evisceration")
def Vivacious_Evisceration():
	return render_template("vivacious-evisceration.html")

@app.route("/advantageous-assault")
def Advantageous_Assault():
	return render_template("advantageous-assault.html")

@app.route("/snatch-arrow")
def Snatch_Arrow():
	return render_template("snatch-arrow.html")

@app.route("/deaths-door")
def Deaths_Door():
	return render_template("deaths-door.html")

@app.route("/deny-advantage")
def Deny_Advantage():
	return render_template("deny-advantage.html")

@app.route("/nimble-roll")
def Nimble_Roll():
	return render_template("nimble-roll.html")

@app.route("/reflexive-grip")
def Reflexive_Grip():
	return render_template("reflexive-grip.html")

@app.route("/smash-from-the-air")
def Smash_From_the_Air():
	return render_template("smash-from-the-air.html")

@app.route("/master-of-many-styles")
def Master_of_Many_Styles():
	return render_template("master-of-many-styles.html")

@app.route("/prevailing-position")
def Prevailing_Position():
	return render_template("prevailing-position.html")

@app.route("/back-to-back")
def Back_to_Back():
	return render_template("back-to-back.html")

@app.route("/coordinated-charge")
def Coordinated_Charge():
	return render_template("coordinated-charge.html")

@app.route("/coordinated-distraction")
def Coordinated_Distraction():
	return render_template("coordinated-distraction.html")

@app.route("/deft-combat-cooperation")
def Deft_Combat_Cooperation():
	return render_template("deft-combat-cooperation.html")

@app.route("/gang-up")
def Gang_Up():
	return render_template("gang-up.html")

@app.route("/knight-vigilant")
def Knight_Vigilant():
	return render_template("knight-vigilant.html")

@app.route("/leave-an-opening")
def Leave_an_Opening():
	return render_template("leave-an-opening.html")

@app.route("/scouts-warning")
def Scouts_Warning():
	return render_template("scouts-warning.html")

@app.route("/target-of-opportunity")
def Target_of_Opportunity():
	return render_template("target-of-opportunity.html")

@app.route("/topple-foe")
def Topple_Foe():
	return render_template("topple-foe.html")

@app.route("/vigils-walls-rise-anew")
def Vigils_Walls_Rise_Anew():
	return render_template("vigils-walls-rise-anew.html")

@app.route("/protect-ally")
def Protect_Ally():
	return render_template("protect-ally.html")

@app.route("/rallying-charge")
def Rallying_Charge():
	return render_template("rallying-charge.html")

@app.route("/stave-off-catastrophe")
def Stave_off_Catastrophe():
	return render_template("stave-off-catastrophe.html")

@app.route("/leading-dance")
def Leading_Dance():
	return render_template("leading-dance.html")

@app.route("/sleeper-hold")
def Sleeper_Hold():
	return render_template("sleeper-hold.html")

@app.route("/tangle-of-battle")
def Tangle_of_Battle():
	return render_template("tangle-of-battle.html")

@app.route("/lunge")
def Lunge():
	return render_template("lunge.html")

@app.route("/blood-debilitations")
def Blood_Debilitations():
	return render_template("blood-debilitations.html")

@app.route("/critical-debilitations")
def Critical_Debilitations():
	return render_template("critical-debilitations.html")

@app.route("/double-debilitation")
def Double_Debilitation():
	return render_template("double-debilitation.html")

@app.route("/eldritch-debilitation")
def Eldritch_Debilitation():
	return render_template("eldritch-debilitation.html")

@app.route("/methodical-debilitation")
def Methodical_Debilitation():
	return render_template("methodical-debilitation.html")

@app.route("/precise-debilitation")
def Precise_Debilitation():
	return render_template("precise-debilitation.html")

@app.route("/tactical-debilitation")
def Tactical_Debilitation():
	return render_template("tactical-debilitation.html")

@app.route("/vicious-debilitation")
def Vicious_Debilitation():
	return render_template("vicious-debilitation.html")

@app.route("/tactic")
def Tactic():
	return render_template("tactic.html")

@app.route("/hunt-prey")
def Hunt_Prey():
	return render_template("hunt-prey.html")

@app.route("/outwit")
def Outwit():
	return render_template("outwit.html")

@app.route("/posse")
def Posse():
	return render_template("posse.html")

@app.route("/double-prey")
def Double_Prey():
	return render_template("double-prey.html")

@app.route("/wardens-boon")
def Wardens_Boon():
	return render_template("wardens-boon.html")

@app.route("/shared-prey")
def Shared_Prey():
	return render_template("shared-prey.html")

@app.route("/swift-track-prey")
def Swift_Track_Prey():
	return render_template("swift-track-prey.html")

@app.route("/to-the-ends-of-the-earth")
def To_the_Ends_of_the_Earth():
	return render_template("to-the-ends-of-the-earth.html")

@app.route("/triple-threat")
def Triple_Threat():
	return render_template("triple-threat.html")

@app.route("/greater-outwit")
def Greater_Outwit():
	return render_template("greater-outwit.html")

@app.route("/wardens-guidance")
def Wardens_Guidance():
	return render_template("wardens-guidance.html")

@app.route("/rangers-companion")
def Rangers_Companion():
	return render_template("rangers-companion.html")

@app.route("/rangers-masterful-companion")
def Rangers_Masterful_Companion():
	return render_template("rangers-masterful-companion.html")

@app.route("/hunters-vision")
def Hunters_Vision():
	return render_template("hunters-vision.html")

@app.route("/flurry")
def Flurry():
	return render_template("flurry.html")

@app.route("/precision")
def Precision():
	return render_template("precision.html")

@app.route("/greater-precision")
def Greater_Precision():
	return render_template("greater-precision.html")

@app.route("/additional-recollection")
def Additional_Recollection():
	return render_template("additional-recollection.html")

@app.route("/monster-warden")
def Monster_Warden():
	return render_template("monster-warden.html")

@app.route("/master-monster-hunter")
def Master_Monster_Hunter():
	return render_template("master-monster-hunter.html")

@app.route("/disrupt-prey")
def Disrupt_Prey():
	return render_template("disrupt-prey.html")

@app.route("/rangers-snap-grapple")
def Rangers_Snap_Grapple():
	return render_template("rangers-snap-grapple.html")

@app.route("/second-sting")
def Second_Sting():
	return render_template("second-sting.html")

@app.route("/twin-takedown")
def Twin_Takedown():
	return render_template("twin-takedown.html")

@app.route("/deadly-aim")
def Deadly_Aim():
	return render_template("deadly-aim.html")

@app.route("/distracting-shot")
def Distracting_Shot():
	return render_template("distracting-shot.html")

@app.route("/greater-distracting-shot")
def Greater_Distracting_Shot():
	return render_template("greater-distracting-shot.html")

@app.route("/hunted-shot")
def Hunted_Shot():
	return render_template("hunted-shot.html")

@app.route("/hunters-aim")
def Hunters_Aim():
	return render_template("hunters-aim.html")

@app.route("/penetrating-shot")
def Penetrating_Shot():
	return render_template("penetrating-shot.html")

@app.route("/targeting-shot")
def Targeting_Shot():
	return render_template("targeting-shot.html")

@app.route("/favored-enemy")
def Favored_Enemy():
	return render_template("favored-enemy.html")

@app.route("/after-you")
def After_You():
	return render_template("after-you.html")

@app.route("/combination-finisher")
def Combination_Finisher():
	return render_template("combination-finisher.html")

@app.route("/continuous-flair")
def Continuous_Flair():
	return render_template("continuous-flair.html")

@app.route("/derring-do")
def Derring_Do():
	return render_template("derring-do.html")

@app.route("/disarming-panache")
def Disarming_Panache():
	return render_template("disarming-panache.html")

@app.route("/impaling-finisher")
def Impaling_Finisher():
	return render_template("impaling-finisher.html")

@app.route("/dual-finisher")
def Dual_Finisher():
	return render_template("dual-finisher.html")

@app.route("/precise-finisher")
def Precise_Finisher():
	return render_template("precise-finisher.html")

@app.route("/stunning-finisher")
def Stunning_Finisher():
	return render_template("stunning-finisher.html")

@app.route("/targeting-finisher")
def Targeting_Finisher():
	return render_template("targeting-finisher.html")

@app.route("/unbalancing-finisher")
def Unbalancing_Finisher():
	return render_template("unbalancing-finisher.html")

@app.route("/vivacious-speed")
def Vivacious_Speed():
	return render_template("vivacious-speed.html")

@app.route("/finishing-follow")
def Finishing_Follow():
	return render_template("finishing-follow.html")

@app.route("/flamboyant-athlete")
def Flamboyant_Athlete():
	return render_template("flamboyant-athlete.html")

@app.route("/flamboyant-cruelty")
def Flamboyant_Cruelty():
	return render_template("flamboyant-cruelty.html")

@app.route("/mobile-finisher")
def Mobile_Finisher():
	return render_template("mobile-finisher.html")

@app.route("/flamboyant-leap")
def Flamboyant_Leap():
	return render_template("flamboyant-leap.html")

@app.route("/perfect-finisher")
def Perfect_Finisher():
	return render_template("perfect-finisher.html")

@app.route("/rage")
def Rage():
	return render_template("rage.html")

@app.route("/animal-skin")
def Animal_Skin():
	return render_template("animal-skin.html")

@app.route("/furious-bully")
def Furious_Bully():
	return render_template("furious-bully.html")

@app.route("/come-and-get-me")
def Come_and_Get_Me():
	return render_template("come-and-get-me.html")

@app.route("/share-rage")
def Share_Rage():
	return render_template("share-rage.html")

@app.route("/contagious-rage")
def Contagious_Rage():
	return render_template("contagious-rage.html")

@app.route("/draconic-arrogance")
def Draconic_Arrogance():
	return render_template("draconic-arrogance.html")

@app.route("/dragons-rage-wings")
def Dragons_Rage_Wings():
	return render_template("dragons-rage-wings.html")

@app.route("/dragons-rage-breath")
def Dragons_Rage_Breath():
	return render_template("dragons-rage-breath.html")

@app.route("/furious-finish")
def Furious_Finish():
	return render_template("furious-finish.html")

@app.route("/furious-vengeance")
def Furious_Vengeance():
	return render_template("furious-vengeance.html")

@app.route("/giants-stature")
def Giants_Stature():
	return render_template("giants-stature.html")

@app.route("/giants-lunge")
def Giants_Lunge():
	return render_template("giants-lunge.html")

@app.route("/mage-hunter")
def Mage_Hunter():
	return render_template("mage-hunter.html")

@app.route("/mighty-rage")
def Mighty_Rage():
	return render_template("mighty-rage.html")

@app.route("/moment-of-clarity-4338219")
def Moment_of_Clarity():
	return render_template("moment-of-clarity-4338219.html")

@app.route("/nocturnal-sense")
def Nocturnal_Sense():
	return render_template("nocturnal-sense.html")

@app.route("/predators-pounce")
def Predators_Pounce():
	return render_template("predators-pounce.html")

@app.route("/quick-rage")
def Quick_Rage():
	return render_template("quick-rage.html")

@app.route("/raging-thrower")
def Raging_Thrower():
	return render_template("raging-thrower.html")

@app.route("/reckless-abandon-131641")
def Reckless_Abandon():
	return render_template("reckless-abandon-131641.html")

@app.route("/renewed-vigor")
def Renewed_Vigor():
	return render_template("renewed-vigor.html")

@app.route("/scouring-rage")
def Scouring_Rage():
	return render_template("scouring-rage.html")

@app.route("/second-wind")
def Second_Wind():
	return render_template("second-wind.html")

@app.route("/shattering-blows")
def Shattering_Blows():
	return render_template("shattering-blows.html")

@app.route("/spirits-interference")
def Spirits_Interference():
	return render_template("spirits-interference.html")

@app.route("/spirits-wrath")
def Spirits_Wrath():
	return render_template("spirits-wrath.html")

@app.route("/spiritual-guides")
def Spiritual_Guides():
	return render_template("spiritual-guides.html")

@app.route("/sunder-spell")
def Sunder_Spell():
	return render_template("sunder-spell.html")

@app.route("/sunder-enchantment")
def Sunder_Enchantment():
	return render_template("sunder-enchantment.html")

@app.route("/titans-structure")
def Titans_Structure():
	return render_template("titans-structure.html")

@app.route("/unstoppable-juggernaut")
def Unstoppable_Juggernaut():
	return render_template("unstoppable-juggernaut.html")

@app.route("/vengeful-strike")
def Vengeful_Strike():
	return render_template("vengeful-strike.html")

@app.route("/wounded-rage")
def Wounded_Rage():
	return render_template("wounded-rage.html")

@app.route("/supernatural-senses")
def Supernatural_Senses():
	return render_template("supernatural-senses.html")

@app.route("/athletic-strategem")
def Athletic_Strategem():
	return render_template("athletic-strategem.html")

@app.route("/shared-strategem")
def Shared_Strategem():
	return render_template("shared-strategem.html")

@app.route("/didactic-strike")
def Didactic_Strike():
	return render_template("didactic-strike.html")

@app.route("/known-weakness")
def Known_Weakness():
	return render_template("known-weakness.html")

@app.route("/ongoing-strategy")
def Ongoing_Strategy():
	return render_template("ongoing-strategy.html")

@app.route("/scalpels-point")
def Scalpels_Point():
	return render_template("scalpels-point.html")

@app.route("/strategic-assessment")
def Strategic_Assessment():
	return render_template("strategic-assessment.html")

@app.route("/strategic-bypass")
def Strategic_Bypass():
	return render_template("strategic-bypass.html")

@app.route("/takedown-expert")
def Takedown_Expert():
	return render_template("takedown-expert.html")

@app.route("/analyze-weakness")
def Analyze_Weakness():
	return render_template("analyze-weakness.html")

@app.route("/magical-trickster")
def Magical_Trickster():
	return render_template("magical-trickster.html")

@app.route("/mug")
def Mug():
	return render_template("mug.html")

@app.route("/ruffian")
def Ruffian():
	return render_template("ruffian.html")

@app.route("/dispelling-slice")
def Dispelling_Slice():
	return render_template("dispelling-slice.html")

@app.route("/powerful-sneak")
def Powerful_Sneak():
	return render_template("powerful-sneak.html")

@app.route("/the-harder-they-fall")
def The_Harder_They_Fall():
	return render_template("the-harder-they-fall.html")

@app.route("/enduring-debilitation")
def Enduring_Debilitation():
	return render_template("enduring-debilitation.html")

@app.route("/mimic-protections")
def Mimic_Protections():
	return render_template("mimic-protections.html")

@app.route("/swift-prey")
def Swift_Prey():
	return render_template("swift-prey.html")

@app.route("/monster-hunter")
def Monster_Hunter():
	return render_template("monster-hunter.html")

@app.route("/legendary-monster-hunter")
def Legendary_Monster_Hunter():
	return render_template("legendary-monster-hunter.html")

@app.route("/panache")
def Panache():
	return render_template("panache.html")

@app.route("/confident-finisher")
def Confident_Finisher():
	return render_template("confident-finisher.html")

@app.route("/battledancer")
def Battledancer():
	return render_template("battledancer.html")

@app.route("/braggart")
def Braggart():
	return render_template("braggart.html")

@app.route("/fencer")
def Fencer():
	return render_template("fencer.html")

@app.route("/gymnast")
def Gymnast():
	return render_template("gymnast.html")

@app.route("/wit")
def Wit():
	return render_template("wit.html")

@app.route("/bleeding-finisher")
def Bleeding_Finisher():
	return render_template("bleeding-finisher.html")

@app.route("/eternal-confidence")
def Eternal_Confidence():
	return render_template("eternal-confidence.html")

@app.route("/flying-blade")
def Flying_Blade():
	return render_template("flying-blade.html")

@app.route("/lethal-finisher")
def Lethal_Finisher():
	return render_template("lethal-finisher.html")

@app.route("/perfect-clarity")
def Perfect_Clarity():
	return render_template("perfect-clarity.html")

@app.route("/vivacious-bravado")
def Vivacious_Bravado():
	return render_template("vivacious-bravado.html")

@app.route("/mystic-strikes")
def Mystic_Strikes():
	return render_template("mystic-strikes.html")

@app.route("/adamantine-strikes")
def Adamantine_Strikes():
	return render_template("adamantine-strikes.html")

@app.route("/monastic-weaponry")
def Monastic_Weaponry():
	return render_template("monastic-weaponry.html")

@app.route("/ancestral-weaponry")
def Ancestral_Weaponry():
	return render_template("ancestral-weaponry.html")

@app.route("/ancestral-weapon-familiarity")
def Ancestral_Weapon_Familiarity():
	return render_template("ancestral-weapon-familiarity.html")

@app.route("/blazing-talon-surge")
def Blazing_Talon_Surge():
	return render_template("blazing-talon-surge.html")

@app.route("/brawling-focus")
def Brawling_Focus():
	return render_template("brawling-focus.html")

@app.route("/rain-of-embers-stance")
def Rain_of_Embers_Stance():
	return render_template("rain-of-embers-stance.html")

@app.route("/cobra-envenom")
def Cobra_Envenom():
	return render_template("cobra-envenom.html")

@app.route("/crane-flutter")
def Crane_Flutter():
	return render_template("crane-flutter.html")

@app.route("/cross-the-final-horizon")
def Cross_the_Final_Horizon():
	return render_template("cross-the-final-horizon.html")

@app.route("/stumbling-stance")
def Stumbling_Stance():
	return render_template("stumbling-stance.html")

@app.route("/dragon-stance")
def Dragon_Stance():
	return render_template("dragon-stance.html")

@app.route("/dragon-roar")
def Dragon_Roar():
	return render_template("dragon-roar.html")

@app.route("/explosive-death-drop")
def Explosive_Death_Drop():
	return render_template("explosive-death-drop.html")

@app.route("/flurry-of-blows")
def Flurry_of_Blows():
	return render_template("flurry-of-blows.html")

@app.route("/flurry-of-maneuvers")
def Flurry_of_Maneuvers():
	return render_template("flurry-of-maneuvers.html")

@app.route("/monastic-archer-stance")
def Monastic_Archer_Stance():
	return render_template("monastic-archer-stance.html")

@app.route("/focused-shot")
def Focused_Shot():
	return render_template("focused-shot.html")

@app.route("/gorilla-stance")
def Gorilla_Stance():
	return render_template("gorilla-stance.html")

@app.route("/gorilla-pound")
def Gorilla_Pound():
	return render_template("gorilla-pound.html")

@app.route("/animal-instinct")
def Animal_Instinct():
	return render_template("animal-instinct.html")

@app.route("/dragon-instinct")
def Dragon_Instinct():
	return render_template("dragon-instinct.html")

@app.route("/fury-instinct")
def Fury_Instinct():
	return render_template("fury-instinct.html")

@app.route("/giant-instinct")
def Giant_Instinct():
	return render_template("giant-instinct.html")

@app.route("/spirit-instinct")
def Spirit_Instinct():
	return render_template("spirit-instinct.html")

@app.route("/ironblood-stance")
def Ironblood_Stance():
	return render_template("ironblood-stance.html")

@app.route("/ironblood-surge")
def Ironblood_Surge():
	return render_template("ironblood-surge.html")

@app.route("/metal-strikes")
def Metal_Strikes():
	return render_template("metal-strikes.html")

@app.route("/peafowl-stance")
def Peafowl_Stance():
	return render_template("peafowl-stance.html")

@app.route("/peafowl-strut")
def Peafowl_Strut():
	return render_template("peafowl-strut.html")

@app.route("/pinning-fire")
def Pinning_Fire():
	return render_template("pinning-fire.html")

@app.route("/return-fire")
def Return_Fire():
	return render_template("return-fire.html")

@app.route("/shooting-stars-stance")
def Shooting_Stars_Stance():
	return render_template("shooting-stars-stance.html")

@app.route("/stumbling-feint")
def Stumbling_Feint():
	return render_template("stumbling-feint.html")

@app.route("/stunning-fist")
def Stunning_Fist():
	return render_template("stunning-fist.html")

@app.route("/movement-types")
def Movement_Types():
	return render_template("movement-types.html")

@app.route("/forced-movement")
def Forced_Movement():
	return render_template("forced-movement.html")

@app.route("/tangled-forest-rake")
def Tangled_Forest_Rake():
	return render_template("tangled-forest-rake.html")

@app.route("/tiger-stance")
def Tiger_Stance():
	return render_template("tiger-stance.html")

@app.route("/tiger-slash")
def Tiger_Slash():
	return render_template("tiger-slash.html")

@app.route("/triangle-shot")
def Triangle_Shot():
	return render_template("triangle-shot.html")

@app.route("/whirling-blade-stance")
def Whirling_Blade_Stance():
	return render_template("whirling-blade-stance.html")

@app.route("/wolf-stance")
def Wolf_Stance():
	return render_template("wolf-stance.html")

@app.route("/wolf-drag")
def Wolf_Drag():
	return render_template("wolf-drag.html")

@app.route("/abundant-step")
def Abundant_Step():
	return render_template("abundant-step.html")

@app.route("/ki-strike")
def Ki_Strike():
	return render_template("ki-strike.html")

@app.route("/elemental-fist")
def Elemental_Fist():
	return render_template("elemental-fist.html")

@app.route("/endurance-of-the-rooted-tree")
def Endurance_of_the_Rooted_Tree():
	return render_template("endurance-of-the-rooted-tree.html")

@app.route("/ki-blast")
def Ki_Blast():
	return render_template("ki-blast.html")

@app.route("/ki-center")
def Ki_Center():
	return render_template("ki-center.html")

@app.route("/ki-form")
def Ki_Form():
	return render_template("ki-form.html")

@app.route("/ki-rush")
def Ki_Rush():
	return render_template("ki-rush.html")

@app.route("/medusas-wrath")
def Medusas_Wrath():
	return render_template("medusas-wrath.html")

@app.route("/overwhelming-breath")
def Overwhelming_Breath():
	return render_template("overwhelming-breath.html")

@app.route("/perfect-strike")
def Perfect_Strike():
	return render_template("perfect-strike.html")

@app.route("/quivering-palm")
def Quivering_Palm():
	return render_template("quivering-palm.html")

@app.route("/sacred-ki")
def Sacred_Ki():
	return render_template("sacred-ki.html")

@app.route("/unblinking-flame-revelation")
def Unblinking_Flame_Revelation():
	return render_template("unblinking-flame-revelation.html")

@app.route("/unbreaking-wave-advance")
def Unbreaking_Wave_Advance():
	return render_template("unbreaking-wave-advance.html")

@app.route("/untwisting-iron-buffer")
def Untwisting_Iron_Buffer():
	return render_template("untwisting-iron-buffer.html")

@app.route("/wild-wind-initiate")
def Wild_Wind_Initiate():
	return render_template("wild-wind-initiate.html")

@app.route("/wild-winds-gust")
def Wild_Winds_Gust():
	return render_template("wild-winds-gust.html")

@app.route("/wind-jump")
def Wind_Jump():
	return render_template("wind-jump.html")

@app.route("/fuse-stance")
def Fuse_Stance():
	return render_template("fuse-stance.html")

@app.route("/deadly-strikes")
def Deadly_Strikes():
	return render_template("deadly-strikes.html")

@app.route("/disrupt-ki")
def Disrupt_Ki():
	return render_template("disrupt-ki.html")

@app.route("/flinging-blow")
def Flinging_Blow():
	return render_template("flinging-blow.html")

@app.route("/flying-kick")
def Flying_Kick():
	return render_template("flying-kick.html")

@app.route("/knockback-strike")
def Knockback_Strike():
	return render_template("knockback-strike.html")

@app.route("/one-inch-punch")
def One_Inch_Punch():
	return render_template("one-inch-punch.html")

@app.route("/one-millimeter-punch")
def One_Millimeter_Punch():
	return render_template("one-millimeter-punch.html")

@app.route("/form-lock")
def Form_Lock():
	return render_template("form-lock.html")

@app.route("/speaking-sky")
def Speaking_Sky():
	return render_template("speaking-sky.html")

@app.route("/sky-and-heaven-stance")
def Sky_and_Heaven_Stance():
	return render_template("sky-and-heaven-stance.html")

@app.route("/mountain-stance")
def Mountain_Stance():
	return render_template("mountain-stance.html")

@app.route("/mountain-stronghold")
def Mountain_Stronghold():
	return render_template("mountain-stronghold.html")

@app.route("/mountain-quake")
def Mountain_Quake():
	return render_template("mountain-quake.html")

@app.route("/shadows-web")
def Shadows_Web():
	return render_template("shadows-web.html")

@app.route("/tangled-forest-stance")
def Tangled_Forest_Stance():
	return render_template("tangled-forest-stance.html")

@app.route("/diamond-fists")
def Diamond_Fists():
	return render_template("diamond-fists.html")

@app.route("/improvised-weapon-fighter")
def Improvised_Weapon_Fighter():
	return render_template("improvised-weapon-fighter.html")

@app.route("/splash-7476201")
def Splash():
	return render_template("splash-7476201.html")

@app.route("/weapon-critical-specialization-effects")
def Weapon_Critical_Specialization_Effects():
	return render_template("weapon-critical-specialization-effects.html")

@app.route("/improvised-critical")
def Improvised_Critical():
	return render_template("improvised-critical.html")

@app.route("/improvised-pummel")
def Improvised_Pummel():
	return render_template("improvised-pummel.html")

@app.route("/makeshift-strike")
def Makeshift_Strike():
	return render_template("makeshift-strike.html")

@app.route("/oversized-throw")
def Oversized_Throw():
	return render_template("oversized-throw.html")

@app.route("/shattering-strike-3539424")
def Shattering_Strike():
	return render_template("shattering-strike-3539424.html")

@app.route("/surprise-strike")
def Surprise_Strike():
	return render_template("surprise-strike.html")

@app.route("/fanes-fourberie")
def Fanes_Fourberie():
	return render_template("fanes-fourberie.html")

@app.route("/archers-aim")
def Archers_Aim():
	return render_template("archers-aim.html")

@app.route("/arrow-of-death")
def Arrow_of_Death():
	return render_template("arrow-of-death.html")

@app.route("/press")
def Press():
	return render_template("press.html")

@app.route("/assisting-shot")
def Assisting_Shot():
	return render_template("assisting-shot.html")

@app.route("/bullseye")
def Bullseye():
	return render_template("bullseye.html")

@app.route("/crossbow-terror")
def Crossbow_Terror():
	return render_template("crossbow-terror.html")

@app.route("/debilitating-shot")
def Debilitating_Shot():
	return render_template("debilitating-shot.html")

@app.route("/double-shot")
def Double_Shot():
	return render_template("double-shot.html")

@app.route("/enchanting-arrow")
def Enchanting_Arrow():
	return render_template("enchanting-arrow.html")

@app.route("/far-shot")
def Far_Shot():
	return render_template("far-shot.html")

@app.route("/far-throw")
def Far_Throw():
	return render_template("far-throw.html")

@app.route("/forceful-shot")
def Forceful_Shot():
	return render_template("forceful-shot.html")

@app.route("/impossible-volley")
def Impossible_Volley():
	return render_template("impossible-volley.html")

@app.route("/incredible-ricochet")
def Incredible_Ricochet():
	return render_template("incredible-ricochet.html")

@app.route("/incredible-aim")
def Incredible_Aim():
	return render_template("incredible-aim.html")

@app.route("/lobbed-attack")
def Lobbed_Attack():
	return render_template("lobbed-attack.html")

@app.route("/viper-eldritch-arrow")
def Viper_Eldritch_Arrow():
	return render_template("viper-eldritch-arrow.html")

@app.route("/shining-eldritch-arrow")
def Shining_Eldritch_Arrow():
	return render_template("shining-eldritch-arrow.html")

@app.route("/beacon-shot-eldritch-arrow")
def Beacon_Shot_Eldritch_Arrow():
	return render_template("beacon-shot-eldritch-arrow.html")

@app.route("/antler-eldritch-arrow")
def Antler_Eldritch_Arrow():
	return render_template("antler-eldritch-arrow.html")

@app.route("/vine-eldritch-arrow")
def Vine_Eldritch_Arrow():
	return render_template("vine-eldritch-arrow.html")

@app.route("/climbing-bolt-eldritch-arrow")
def Climbing_Bolt_Eldritch_Arrow():
	return render_template("climbing-bolt-eldritch-arrow.html")

@app.route("/triple-shot")
def Triple_Shot():
	return render_template("triple-shot.html")

@app.route("/multishot-stance")
def Multishot_Stance():
	return render_template("multishot-stance.html")

@app.route("/mobile-shot-stance")
def Mobile_Shot_Stance():
	return render_template("mobile-shot-stance.html")

@app.route("/opportune-throw")
def Opportune_Throw():
	return render_template("opportune-throw.html")

@app.route("/parting-shot")
def Parting_Shot():
	return render_template("parting-shot.html")

@app.route("/penetrating-projectile")
def Penetrating_Projectile():
	return render_template("penetrating-projectile.html")

@app.route("/perfect-shot")
def Perfect_Shot():
	return render_template("perfect-shot.html")

@app.route("/phase-arrow")
def Phase_Arrow():
	return render_template("phase-arrow.html")

@app.route("/point-blank-shot")
def Point_Blank_Shot():
	return render_template("point-blank-shot.html")

@app.route("/precious-arrow")
def Precious_Arrow():
	return render_template("precious-arrow.html")

@app.route("/quick-shot")
def Quick_Shot():
	return render_template("quick-shot.html")

@app.route("/rebounding-toss")
def Rebounding_Toss():
	return render_template("rebounding-toss.html")

@app.route("/shootists-draw")
def Shootists_Draw():
	return render_template("shootists-draw.html")

@app.route("/repeating-hand-crossbow")
def Repeating_Hand_Crossbow():
	return render_template("repeating-hand-crossbow.html")

@app.route("/ricochet-stance")
def Ricochet_Stance():
	return render_template("ricochet-stance.html")

@app.route("/ricochet-feint")
def Ricochet_Feint():
	return render_template("ricochet-feint.html")

@app.route("/running-reload")
def Running_Reload():
	return render_template("running-reload.html")

@app.route("/seeker-arrow")
def Seeker_Arrow():
	return render_template("seeker-arrow.html")

@app.route("/strong-arm")
def Strong_Arm():
	return render_template("strong-arm.html")

@app.route("/aggressive-block")
def Aggressive_Block():
	return render_template("aggressive-block.html")

@app.route("/buckler-expertise")
def Buckler_Expertise():
	return render_template("buckler-expertise.html")

@app.route("/buckler-dance")
def Buckler_Dance():
	return render_template("buckler-dance.html")

@app.route("/destructive-block")
def Destructive_Block():
	return render_template("destructive-block.html")

@app.route("/disarming-block")
def Disarming_Block():
	return render_template("disarming-block.html")

@app.route("/divine-shield-wall")
def Divine_Shield_Wall():
	return render_template("divine-shield-wall.html")

@app.route("/everstand-stance")
def Everstand_Stance():
	return render_template("everstand-stance.html")

@app.route("/everstand-strike")
def Everstand_Strike():
	return render_template("everstand-strike.html")

@app.route("/reflexive-shield")
def Reflexive_Shield():
	return render_template("reflexive-shield.html")

@app.route("/improved-reflexive-shield")
def Improved_Reflexive_Shield():
	return render_template("improved-reflexive-shield.html")

@app.route("/nimble-shield-hand")
def Nimble_Shield_Hand():
	return render_template("nimble-shield-hand.html")

@app.route("/defend")
def Defend():
	return render_template("defend.html")

@app.route("/practiced-defender")
def Practiced_Defender():
	return render_template("practiced-defender.html")

@app.route("/quick-block")
def Quick_Block():
	return render_template("quick-block.html")

@app.route("/reactive-shield")
def Reactive_Shield():
	return render_template("reactive-shield.html")

@app.route("/rescuers-press")
def Rescuers_Press():
	return render_template("rescuers-press.html")

@app.route("/second-shield")
def Second_Shield():
	return render_template("second-shield.html")

@app.route("/shield-of-grace")
def Shield_of_Grace():
	return render_template("shield-of-grace.html")

@app.route("/shield-salvation")
def Shield_Salvation():
	return render_template("shield-salvation.html")

@app.route("/paragons-guard")
def Paragons_Guard():
	return render_template("paragons-guard.html")

@app.route("/shield-of-reckoning")
def Shield_of_Reckoning():
	return render_template("shield-of-reckoning.html")

@app.route("/shielded-stride")
def Shielded_Stride():
	return render_template("shielded-stride.html")

@app.route("/disarming-stance")
def Disarming_Stance():
	return render_template("disarming-stance.html")

@app.route("/disarming-twist")
def Disarming_Twist():
	return render_template("disarming-twist.html")

@app.route("/flourish")
def Flourish():
	return render_template("flourish.html")

@app.route("/two-handed")
def Two_Handed():
	return render_template("two-handed.html")

@app.route("/dual-handed-assault")
def Dual_Handed_Assault():
	return render_template("dual-handed-assault.html")

@app.route("/dueling-parry")
def Dueling_Parry():
	return render_template("dueling-parry.html")

@app.route("/dueling-dance")
def Dueling_Dance():
	return render_template("dueling-dance.html")

@app.route("/dueling-reposte")
def Dueling_Reposte():
	return render_template("dueling-reposte.html")

@app.route("/duelists-challenge")
def Duelists_Challenge():
	return render_template("duelists-challenge.html")

@app.route("/duelists-edge")
def Duelists_Edge():
	return render_template("duelists-edge.html")

@app.route("/guardians-deflection")
def Guardians_Deflection():
	return render_template("guardians-deflection.html")

@app.route("/guiding-finish")
def Guiding_Finish():
	return render_template("guiding-finish.html")

@app.route("/guiding-reposte")
def Guiding_Reposte():
	return render_template("guiding-reposte.html")

@app.route("/improved-dueling-reposte")
def Improved_Dueling_Reposte():
	return render_template("improved-dueling-reposte.html")

@app.route("/saving-slash")
def Saving_Slash():
	return render_template("saving-slash.html")

@app.route("/selfless-parry")
def Selfless_Parry():
	return render_template("selfless-parry.html")

@app.route("/student-of-the-dueling-arts")
def Student_of_the_Dueling_Arts():
	return render_template("student-of-the-dueling-arts.html")

@app.route("/unnerving-prowess")
def Unnerving_Prowess():
	return render_template("unnerving-prowess.html")

@app.route("/avalanche-strike")
def Avalanche_Strike():
	return render_template("avalanche-strike.html")

@app.route("/clear-the-way")
def Clear_the_Way():
	return render_template("clear-the-way.html")

@app.route("/hammer-quake")
def Hammer_Quake():
	return render_template("hammer-quake.html")

@app.route("/shoving-sweep")
def Shoving_Sweep():
	return render_template("shoving-sweep.html")

@app.route("/positioning-assault")
def Positioning_Assault():
	return render_template("positioning-assault.html")

@app.route("/impossible-flurry")
def Impossible_Flurry():
	return render_template("impossible-flurry.html")

@app.route("/accurate-flurry")
def Accurate_Flurry():
	return render_template("accurate-flurry.html")

@app.route("/double-slice")
def Double_Slice():
	return render_template("double-slice.html")

@app.route("/dual-onslaught")
def Dual_Onslaught():
	return render_template("dual-onslaught.html")

@app.route("/dual-thrower")
def Dual_Thrower():
	return render_template("dual-thrower.html")

@app.route("/dual-weapon-reload")
def Dual_Weapon_Reload():
	return render_template("dual-weapon-reload.html")

@app.route("/flensing-slice")
def Flensing_Slice():
	return render_template("flensing-slice.html")

@app.route("/graceful-poise")
def Graceful_Poise():
	return render_template("graceful-poise.html")

@app.route("/twin-parry")
def Twin_Parry():
	return render_template("twin-parry.html")

@app.route("/twin-reposte-939707")
def Twin_Reposte():
	return render_template("twin-reposte-939707.html")

@app.route("/improved-twin-reposte")
def Improved_Twin_Reposte():
	return render_template("improved-twin-reposte.html")

@app.route("/twinned-defense")
def Twinned_Defense():
	return render_template("twinned-defense.html")

@app.route("/two-weapon-flurry")
def Two_Weapon_Flurry():
	return render_template("two-weapon-flurry.html")

@app.route("/flinging-shove")
def Flinging_Shove():
	return render_template("flinging-shove.html")

@app.route("/powerful-shove")
def Powerful_Shove():
	return render_template("powerful-shove.html")

@app.route("/hurling-charge")
def Hurling_Charge():
	return render_template("hurling-charge.html")

@app.route("/quick-stow-1658530")
def Quick_Stow():
	return render_template("quick-stow-1658530.html")

@app.route("/brutality")
def Brutality():
	return render_template("brutality.html")

@app.route("/exotic-weapon-training")
def Exotic_Weapon_Training():
	return render_template("exotic-weapon-training.html")

@app.route("/stage-fighting")
def Stage_Fighting():
	return render_template("stage-fighting.html")

@app.route("/agile-grace")
def Agile_Grace():
	return render_template("agile-grace.html")

@app.route("/axe-thrower")
def Axe_Thrower():
	return render_template("axe-thrower.html")

@app.route("/staff-acrobat")
def Staff_Acrobat():
	return render_template("staff-acrobat.html")

@app.route("/pivot-strike")
def Pivot_Strike():
	return render_template("pivot-strike.html")

@app.route("/weapon-proficiency")
def Weapon_Proficiency():
	return render_template("weapon-proficiency.html")

@app.route("/whirlwind-staff")
def Whirlwind_Staff():
	return render_template("whirlwind-staff.html")

@app.route("/widen-the-gap")
def Widen_the_Gap():
	return render_template("widen-the-gap.html")

@app.route("/reloading-trick")
def Reloading_Trick():
	return render_template("reloading-trick.html")

@app.route("/shield-warden")
def Shield_Warden():
	return render_template("shield-warden.html")

@app.route("/brutish-shove")
def Brutish_Shove():
	return render_template("brutish-shove.html")

@app.route("/dual-weapon-blitz")
def Dual_Weapon_Blitz():
	return render_template("dual-weapon-blitz.html")

@app.route("/brutal-finish")
def Brutal_Finish():
	return render_template("brutal-finish.html")

@app.route("/twin-feint")
def Twin_Feint():
	return render_template("twin-feint.html")

@app.route("/twin-distraction")
def Twin_Distraction():
	return render_template("twin-distraction.html")

@app.route("/levering-strike")
def Levering_Strike():
	return render_template("levering-strike.html")

@app.route("/staff-sweep")
def Staff_Sweep():
	return render_template("staff-sweep.html")

@app.route("/bullying-staff")
def Bullying_Staff():
	return render_template("bullying-staff.html")

@app.route("/infectious-enthusiasm")
def Infectious_Enthusiasm():
	return render_template("infectious-enthusiasm.html")

@app.route("/puff-of-poison")
def Puff_of_Poison():
	return render_template("puff-of-poison.html")

@app.route("/acid-splash")
def Acid_Splash():
	return render_template("acid-splash.html")

@app.route("/chill-touch")
def Chill_Touch():
	return render_template("chill-touch.html")

@app.route("/dancing-lights")
def Dancing_Lights():
	return render_template("dancing-lights.html")

@app.route("/daze")
def Daze():
	return render_template("daze.html")

@app.route("/bullhorn")
def Bullhorn():
	return render_template("bullhorn.html")

@app.route("/detect-magic-9339784")
def Detect_Magic():
	return render_template("detect-magic-9339784.html")

@app.route("/electric-arc")
def Electric_Arc():
	return render_template("electric-arc.html")

@app.route("/gale-blast")
def Gale_Blast():
	return render_template("gale-blast.html")

@app.route("/ghost-sound")
def Ghost_Sound():
	return render_template("ghost-sound.html")

@app.route("/gouging-claw")
def Gouging_Claw():
	return render_template("gouging-claw.html")

@app.route("/light-224996")
def Light():
	return render_template("light-224996.html")

@app.route("/mage-hand")
def Mage_Hand():
	return render_template("mage-hand.html")

@app.route("/message")
def Message():
	return render_template("message.html")

@app.route("/produce-flame")
def Produce_Flame():
	return render_template("produce-flame.html")

@app.route("/ray-of-frost")
def Ray_of_Frost():
	return render_template("ray-of-frost.html")

@app.route("/read-aura")
def Read_Aura():
	return render_template("read-aura.html")

@app.route("/scatter-scree")
def Scatter_Scree():
	return render_template("scatter-scree.html")

@app.route("/shield")
def Shield():
	return render_template("shield.html")

@app.route("/sigil")
def Sigil():
	return render_template("sigil.html")

@app.route("/spout")
def Spout():
	return render_template("spout.html")

@app.route("/tanglefoot")
def Tanglefoot():
	return render_template("tanglefoot.html")

@app.route("/telekinetic-projectile")
def Telekinetic_Projectile():
	return render_template("telekinetic-projectile.html")

@app.route("/disrupt-undead")
def Disrupt_Undead():
	return render_template("disrupt-undead.html")

@app.route("/divine-lance")
def Divine_Lance():
	return render_template("divine-lance.html")

@app.route("/forbidding-ward")
def Forbidding_Ward():
	return render_template("forbidding-ward.html")

@app.route("/guidance")
def Guidance():
	return render_template("guidance.html")

@app.route("/haunting-hymn")
def Haunting_Hymn():
	return render_template("haunting-hymn.html")

@app.route("/know-direction")
def Know_Direction():
	return render_template("know-direction.html")

@app.route("/read-the-air")
def Read_the_Air():
	return render_template("read-the-air.html")

@app.route("/stabilize")
def Stabilize():
	return render_template("stabilize.html")

@app.route("/wash-your-luck")
def Wash_Your_Luck():
	return render_template("wash-your-luck.html")

@app.route("/protect-companion")
def Protect_Companion():
	return render_template("protect-companion.html")

@app.route("/tame")
def Tame():
	return render_template("tame.html")

@app.route("/join-pasts")
def Join_Pasts():
	return render_template("join-pasts.html")

@app.route("/disbelieving-illusions")
def Disbelieving_Illusions():
	return render_template("disbelieving-illusions.html")

@app.route("/power-lift")
def Power_Lift():
	return render_template("power-lift.html")

@app.route("/athletics-str")
def Athletics__STR_():
	return render_template("athletics-str.html")

@app.route("/elemental-zone")
def Elemental_Zone():
	return render_template("elemental-zone.html")

@app.route("/misdirection")
def Misdirection():
	return render_template("misdirection.html")

@app.route("/identifying-spells")
def Identifying_Spells():
	return render_template("identifying-spells.html")

@app.route("/animal-messenger")
def Animal_Messenger():
	return render_template("animal-messenger.html")

@app.route("/animus-mine")
def Animus_Mine():
	return render_template("animus-mine.html")

@app.route("/augury")
def Augury():
	return render_template("augury.html")

@app.route("/barkskin")
def Barkskin():
	return render_template("barkskin.html")

@app.route("/befitting-attire")
def Befitting_Attire():
	return render_template("befitting-attire.html")

@app.route("/blistering-invective")
def Blistering_Invective():
	return render_template("blistering-invective.html")

@app.route("/blood-vendetta")
def Blood_Vendetta():
	return render_template("blood-vendetta.html")

@app.route("/blur")
def Blur():
	return render_template("blur.html")

@app.route("/brand-the-impenitent")
def Brand_the_Impenitent():
	return render_template("brand-the-impenitent.html")

@app.route("/charitable-urge")
def Charitable_Urge():
	return render_template("charitable-urge.html")

@app.route("/comprehend-language")
def Comprehend_Language():
	return render_template("comprehend-language.html")

@app.route("/continual-flame")
def Continual_Flame():
	return render_template("continual-flame.html")

@app.route("/darkness")
def Darkness():
	return render_template("darkness.html")

@app.route("/deafness-3457243")
def Deafness():
	return render_template("deafness-3457243.html")

@app.route("/dismantle")
def Dismantle():
	return render_template("dismantle.html")

@app.route("/dispel-magic")
def Dispel_Magic():
	return render_template("dispel-magic.html")

@app.route("/endure-elements")
def Endure_Elements():
	return render_template("endure-elements.html")

@app.route("/enlarge")
def Enlarge():
	return render_template("enlarge.html")

@app.route("/expeditious-excavation")
def Expeditious_Excavation():
	return render_template("expeditious-excavation.html")

@app.route("/extract-poison")
def Extract_Poison():
	return render_template("extract-poison.html")

@app.route("/false-life")
def False_Life():
	return render_template("false-life.html")

@app.route("/fear-the-sun")
def Fear_the_Sun():
	return render_template("fear-the-sun.html")

@app.route("/feast-of-ashes")
def Feast_of_Ashes():
	return render_template("feast-of-ashes.html")

@app.route("/final-sacrifice")
def Final_Sacrifice():
	return render_template("final-sacrifice.html")

@app.route("/flame-wisp")
def Flame_Wisp():
	return render_template("flame-wisp.html")

@app.route("/gentle-repose")
def Gentle_Repose():
	return render_template("gentle-repose.html")

@app.route("/glitterdust")
def Glitterdust():
	return render_template("glitterdust.html")

@app.route("/heat-metal")
def Heat_Metal():
	return render_template("heat-metal.html")

@app.route("/hideous-laughter")
def Hideous_Laughter():
	return render_template("hideous-laughter.html")

@app.route("/humanoid-form")
def Humanoid_Form():
	return render_template("humanoid-form.html")

@app.route("/ignite-fireworks")
def Ignite_Fireworks():
	return render_template("ignite-fireworks.html")

@app.route("/illusory-creature")
def Illusory_Creature():
	return render_template("illusory-creature.html")

@app.route("/breath-of-drought")
def Breath_of_Drought():
	return render_template("breath-of-drought.html")

@app.route("/calm-emotions")
def Calm_Emotions():
	return render_template("calm-emotions.html")

@app.route("/clawsong")
def Clawsong():
	return render_template("clawsong.html")

@app.route("/enhance-victuals")
def Enhance_Victuals():
	return render_template("enhance-victuals.html")

@app.route("/entangle")
def Entangle():
	return render_template("entangle.html")

@app.route("/fungal-hyphae")
def Fungal_Hyphae():
	return render_template("fungal-hyphae.html")

@app.route("/ghoulish-cravings")
def Ghoulish_Cravings():
	return render_template("ghoulish-cravings.html")

@app.route("/grave-impressions")
def Grave_Impressions():
	return render_template("grave-impressions.html")

@app.route("/guiding-star")
def Guiding_Star():
	return render_template("guiding-star.html")

@app.route("/impeccable-flow")
def Impeccable_Flow():
	return render_template("impeccable-flow.html")

@app.route("/instant-armor")
def Instant_Armor():
	return render_template("instant-armor.html")

@app.route("/invisibility")
def Invisibility():
	return render_template("invisibility.html")

@app.route("/iron-gut")
def Iron_Gut():
	return render_template("iron-gut.html")

@app.route("/lucky-number")
def Lucky_Number():
	return render_template("lucky-number.html")

@app.route("/magic-mouth")
def Magic_Mouth():
	return render_template("magic-mouth.html")

@app.route("/magnetic-attraction")
def Magnetic_Attraction():
	return render_template("magnetic-attraction.html")

@app.route("/magnetic-repulsion")
def Magnetic_Repulsion():
	return render_template("magnetic-repulsion.html")

@app.route("/mimic-undead")
def Mimic_Undead():
	return render_template("mimic-undead.html")

@app.route("/mind-games")
def Mind_Games():
	return render_template("mind-games.html")

@app.route("/obscuring-mist")
def Obscuring_Mist():
	return render_template("obscuring-mist.html")

@app.route("/paranoia-1770706")
def Paranoia():
	return render_template("paranoia-1770706.html")

@app.route("/penumbral-disguise")
def Penumbral_Disguise():
	return render_template("penumbral-disguise.html")

@app.route("/persistent-servant")
def Persistent_Servant():
	return render_template("persistent-servant.html")

@app.route("/phantasmal-treasure")
def Phantasmal_Treasure():
	return render_template("phantasmal-treasure.html")

@app.route("/phantom-crowd")
def Phantom_Crowd():
	return render_template("phantom-crowd.html")

@app.route("/remove-paralysis")
def Remove_Paralysis():
	return render_template("remove-paralysis.html")

@app.route("/resist-energy")
def Resist_Energy():
	return render_template("resist-energy.html")

@app.route("/restoration")
def Restoration():
	return render_template("restoration.html")

@app.route("/restore-senses")
def Restore_Senses():
	return render_template("restore-senses.html")

@app.route("/sea-surge")
def Sea_Surge():
	return render_template("sea-surge.html")

@app.route("/see-invisibility")
def See_Invisibility():
	return render_template("see-invisibility.html")

@app.route("/shatter")
def Shatter():
	return render_template("shatter.html")

@app.route("/shield-other")
def Shield_Other():
	return render_template("shield-other.html")

@app.route("/shrink")
def Shrink():
	return render_template("shrink.html")

@app.route("/silence")
def Silence():
	return render_template("silence.html")

@app.route("/slough-skin")
def Slough_Skin():
	return render_template("slough-skin.html")

@app.route("/sonata-span")
def Sonata_Span():
	return render_template("sonata-span.html")

@app.route("/speak-with-animals")
def Speak_With_Animals():
	return render_template("speak-with-animals.html")

@app.route("/spectral-hand")
def Spectral_Hand():
	return render_template("spectral-hand.html")

@app.route("/spider-climb")
def Spider_Climb():
	return render_template("spider-climb.html")

@app.route("/spirit-sense")
def Spirit_Sense():
	return render_template("spirit-sense.html")

@app.route("/spiritual-weapon")
def Spiritual_Weapon():
	return render_template("spiritual-weapon.html")

@app.route("/status")
def Status():
	return render_template("status.html")

@app.route("/sudden-blight")
def Sudden_Blight():
	return render_template("sudden-blight.html")

@app.route("/sudden-bolt")
def Sudden_Bolt():
	return render_template("sudden-bolt.html")

@app.route("/telekinetic-manuever")
def Telekinetic_Manuever():
	return render_template("telekinetic-manuever.html")

@app.route("/thundering-dominance")
def Thundering_Dominance():
	return render_template("thundering-dominance.html")

@app.route("/timely-tutor")
def Timely_Tutor():
	return render_template("timely-tutor.html")

@app.route("/touch-of-idiocy")
def Touch_of_Idiocy():
	return render_template("touch-of-idiocy.html")

@app.route("/tree-shape")
def Tree_Shape():
	return render_template("tree-shape.html")

@app.route("/umbral-extraction")
def Umbral_Extraction():
	return render_template("umbral-extraction.html")

@app.route("/undetectable-alignment")
def Undetectable_Alignment():
	return render_template("undetectable-alignment.html")

@app.route("/vomit-swarm")
def Vomit_Swarm():
	return render_template("vomit-swarm.html")

@app.route("/warriors-regret")
def Warriors_Regret():
	return render_template("warriors-regret.html")

@app.route("/water-breathing")
def Water_Breathing():
	return render_template("water-breathing.html")

@app.route("/water-walk")
def Water_Walk():
	return render_template("water-walk.html")

@app.route("/web")
def Web():
	return render_template("web.html")

@app.route("/acidic-burst")
def Acidic_Burst():
	return render_template("acidic-burst.html")

@app.route("/air-bubble")
def Air_Bubble():
	return render_template("air-bubble.html")

@app.route("/airburst")
def Airburst():
	return render_template("airburst.html")

@app.route("/alarm")
def Alarm():
	return render_template("alarm.html")

@app.route("/animate-rope")
def Animate_Rope():
	return render_template("animate-rope.html")

@app.route("/ant-haul")
def Ant_Haul():
	return render_template("ant-haul.html")

@app.route("/anticipate-peril")
def Anticipate_Peril():
	return render_template("anticipate-peril.html")

@app.route("/bane")
def Bane():
	return render_template("bane.html")

@app.route("/bless")
def Bless():
	return render_template("bless.html")

@app.route("/befuddle")
def Befuddle():
	return render_template("befuddle.html")

@app.route("/breadcrumbs")
def Breadcrumbs():
	return render_template("breadcrumbs.html")

@app.route("/charm")
def Charm():
	return render_template("charm.html")

@app.route("/color-spray")
def Color_Spray():
	return render_template("color-spray.html")

@app.route("/command")
def Command():
	return render_template("command.html")

@app.route("/deja-vu")
def Deja_Vu():
	return render_template("deja-vu.html")

@app.route("/detect-alignment")
def Detect_Alignment():
	return render_template("detect-alignment.html")

@app.route("/detect-poison")
def Detect_Poison():
	return render_template("detect-poison.html")

@app.route("/disrupting-weapons")
def Disrupting_Weapons():
	return render_template("disrupting-weapons.html")

@app.route("/echoing-weapon")
def Echoing_Weapon():
	return render_template("echoing-weapon.html")

@app.route("/endure")
def Endure():
	return render_template("endure.html")

@app.route("/illusory-disguise")
def Illusory_Disguise():
	return render_template("illusory-disguise.html")

@app.route("/exchange-image")
def Exchange_Image():
	return render_template("exchange-image.html")

@app.route("/fear-8000793")
def Fear():
	return render_template("fear-8000793.html")

@app.route("/feather-fall")
def Feather_Fall():
	return render_template("feather-fall.html")

@app.route("/fleet-step")
def Fleet_Step():
	return render_template("fleet-step.html")

@app.route("/floating-disk")
def Floating_Disk():
	return render_template("floating-disk.html")

@app.route("/friendfetch")
def Friendfetch():
	return render_template("friendfetch.html")

@app.route("/goblin-pox")
def Goblin_Pox():
	return render_template("goblin-pox.html")

@app.route("/gravitational-pull")
def Gravitational_Pull():
	return render_template("gravitational-pull.html")

@app.route("/grease")
def Grease():
	return render_template("grease.html")

@app.route("/gust-of-wind")
def Gust_of_Wind():
	return render_template("gust-of-wind.html")

@app.route("/ill-omen")
def Ill_Omen():
	return render_template("ill-omen.html")

@app.route("/illusory-object")
def Illusory_Object():
	return render_template("illusory-object.html")

@app.route("/invisible-item")
def invisible_Item():
	return render_template("invisible-item.html")

@app.route("/item-facade")
def Item_Facade():
	return render_template("item-facade.html")

@app.route("/jump")
def Jump():
	return render_template("jump.html")

@app.route("/juvenile-companion")
def Juvenile_Companion():
	return render_template("juvenile-companion.html")

@app.route("/liberating-command")
def Liberating_Command():
	return render_template("liberating-command.html")

@app.route("/lock")
def Lock():
	return render_template("lock.html")

@app.route("/longstrider")
def Longstrider():
	return render_template("longstrider.html")

@app.route("/lose-the-path")
def Lose_the_Path():
	return render_template("lose-the-path.html")

@app.route("/mage-armor")
def Mage_Armor():
	return render_template("mage-armor.html")

@app.route("/magic-aura")
def Magic_Aura():
	return render_template("magic-aura.html")

@app.route("/magic-missile")
def Magic_Missile():
	return render_template("magic-missile.html")

@app.route("/magic-stone")
def Magic_Stone():
	return render_template("magic-stone.html")

@app.route("/magic-weapon")
def Magic_Weapon():
	return render_template("magic-weapon.html")

@app.route("/magic-fang")
def Magic_Fang():
	return render_template("magic-fang.html")

@app.route("/mending")
def Mending():
	return render_template("mending.html")

@app.route("/message-rune")
def Message_Rune():
	return render_template("message-rune.html")

@app.route("/mindlink")
def Mindlink():
	return render_template("mindlink.html")

@app.route("/mud-pit")
def Mud_Pit():
	return render_template("mud-pit.html")

@app.route("/necromancers-generosity")
def Necromancers_Generosity():
	return render_template("necromancers-generosity.html")

@app.route("/negate-aroma")
def Negate_Aroma():
	return render_template("negate-aroma.html")

@app.route("/nudge-the-odds")
def Nudge_the_Odds():
	return render_template("nudge-the-odds.html")

@app.route("/object-reading")
def Object_Reading():
	return render_template("object-reading.html")

@app.route("/pass-without-trace")
def Pass_Without_Trace():
	return render_template("pass-without-trace.html")

@app.route("/penumbral-shroud")
def Penumbral_Shroud():
	return render_template("penumbral-shroud.html")

@app.route("/personal-rain-cloud")
def Personal_Rain_Cloud():
	return render_template("personal-rain-cloud.html")

@app.route("/pet-cache")
def Pet_Cache():
	return render_template("pet-cache.html")

@app.route("/pocket-library")
def Pocket_Library():
	return render_template("pocket-library.html")

@app.route("/protection")
def Protection():
	return render_template("protection.html")

@app.route("/protector-tree")
def Protector_Tree():
	return render_template("protector-tree.html")

@app.route("/purify-food-and-drink")
def Purify_Food_and_Drink():
	return render_template("purify-food-and-drink.html")

@app.route("/putrefy-food-and-drink")
def Putrefy_Food_and_Drink():
	return render_template("putrefy-food-and-drink.html")

@app.route("/quick-sort")
def Quick_Sort():
	return render_template("quick-sort.html")

@app.route("/ray-of-enfeeblement")
def Ray_of_Enfeeblement():
	return render_template("ray-of-enfeeblement.html")

@app.route("/restyle")
def Restyle():
	return render_template("restyle.html")

@app.route("/sanctuary")
def Sanctuary():
	return render_template("sanctuary.html")

@app.route("/scouring-sand")
def Scouring_Sand():
	return render_template("scouring-sand.html")

@app.route("/seashell-of-stolen-sound")
def Seashell_of_Stolen_Sound():
	return render_template("seashell-of-stolen-sound.html")

@app.route("/share-lore")
def Share_Lore():
	return render_template("share-lore.html")

@app.route("/shattering-gem")
def Shattering_Gem():
	return render_template("shattering-gem.html")

@app.route("/shillelagh")
def Shillelagh():
	return render_template("shillelagh.html")

@app.route("/shockwave")
def Shockwave():
	return render_template("shockwave.html")

@app.route("/sleep")
def Sleep():
	return render_template("sleep.html")

@app.route("/spirit-link")
def Spirit_Link():
	return render_template("spirit-link.html")

@app.route("/swampcall")
def Swampcall():
	return render_template("swampcall.html")

@app.route("/synchronize")
def Synchronize():
	return render_template("synchronize.html")

@app.route("/temporary-tool")
def Temporary_Tool():
	return render_template("temporary-tool.html")

@app.route("/tether")
def Tether():
	return render_template("tether.html")

@app.route("/thicket-of-knives")
def Thicket_of_Knives():
	return render_template("thicket-of-knives.html")

@app.route("/thoughtful-gift")
def Thoughtful_Gift():
	return render_template("thoughtful-gift.html")

@app.route("/true-strike")
def True_Strike():
	return render_template("true-strike.html")

@app.route("/unseen-servant")
def Unseen_Servant():
	return render_template("unseen-servant.html")

@app.route("/ventriloquism")
def Ventriloquism():
	return render_template("ventriloquism.html")

@app.route("/verdant-sprout")
def Verdant_Sprout():
	return render_template("verdant-sprout.html")

@app.route("/verminous-lure")
def Verminous_Lure():
	return render_template("verminous-lure.html")

@app.route("/create-food")
def Create_Food():
	return render_template("create-food.html")

@app.route("/create-water")
def Create_Water():
	return render_template("create-water.html")

@app.route("/faerie-fire")
def Faerie_Fire():
	return render_template("faerie-fire.html")

@app.route("/fungal-infestation")
def Fungal_Infestation():
	return render_template("fungal-infestation.html")

@app.route("/death-knell")
def Death_Knell():
	return render_template("death-knell.html")

@app.route("/mirror-image")
def Mirror_Image():
	return render_template("mirror-image.html")

@app.route("/schadenfreude")
def Schadenfreude():
	return render_template("schadenfreude.html")

@app.route("/shape-wood")
def Shape_Wood():
	return render_template("shape-wood.html")

@app.route("/force-bolt")
def Force_Bolt():
	return render_template("force-bolt.html")

@app.route("/elemental-tempest")
def Elemental_Tempest():
	return render_template("elemental-tempest.html")

@app.route("/arcana-feats")
def Arcana_Feats():
	return render_template("arcana-feats.html")

@app.route("/spider-sting")
def Spider_Sting():
	return render_template("spider-sting.html")

@app.route("/acid-arrow")
def Acid_Arrow():
	return render_template("acid-arrow.html")

@app.route("/admonishing-ray")
def Admonishing_Ray():
	return render_template("admonishing-ray.html")

@app.route("/agitate")
def Agitate():
	return render_template("agitate.html")

@app.route("/animal-allies-9723296")
def Animal_Allies():
	return render_template("animal-allies-9723296.html")

@app.route("/animated-assault")
def Animated_Assault():
	return render_template("animated-assault.html")

@app.route("/ash-cloud")
def Ash_Cloud():
	return render_template("ash-cloud.html")

@app.route("/biting-words")
def Biting_Words():
	return render_template("biting-words.html")

@app.route("/burning-hands")
def Burning_Hands():
	return render_template("burning-hands.html")

@app.route("/chilling-spray")
def Chilling_Spray():
	return render_template("chilling-spray.html")

@app.route("/concordant-choir")
def Concordant_Choir():
	return render_template("concordant-choir.html")

@app.route("/draw-ire")
def Draw_Ire():
	return render_template("draw-ire.html")

@app.route("/feral-shades")
def Feral_Shades():
	return render_template("feral-shades.html")

@app.route("/flaming-sphere")
def Flaming_Sphere():
	return render_template("flaming-sphere.html")

@app.route("/grim-tendrils")
def Grim_Tendrils():
	return render_template("grim-tendrils.html")

@app.route("/horizon-thunder-sphere")
def Horizon_Thunder_Sphere():
	return render_template("horizon-thunder-sphere.html")

@app.route("/hydraulic-push")
def Hydraulic_Push():
	return render_template("hydraulic-push.html")

@app.route("/imp-sting")
def Imp_Sting():
	return render_template("imp-sting.html")

@app.route("/noxious-vapors")
def Noxious_Vapors():
	return render_template("noxious-vapors.html")

@app.route("/phantom-pain")
def Phantom_Pain():
	return render_template("phantom-pain.html")

@app.route("/rime-slick")
def Rime_Slick():
	return render_template("rime-slick.html")

@app.route("/scorching-ray")
def Scorching_Ray():
	return render_template("scorching-ray.html")

@app.route("/shocking-grasp-91486")
def Shocking_Grasp():
	return render_template("shocking-grasp-91486.html")

@app.route("/snowball")
def Snowball():
	return render_template("snowball.html")

@app.route("/sound-burst")
def Sound_Burst():
	return render_template("sound-burst.html")

@app.route("/worms-repast")
def Worms_Repast():
	return render_template("worms-repast.html")

@app.route("/bottomless-stomach")
def Bottomless_Stomach():
	return render_template("bottomless-stomach.html")

@app.route("/harm")
def Harm():
	return render_template("harm.html")

@app.route("/agonizing-despair")
def Agonizing_Despair():
	return render_template("agonizing-despair.html")

@app.route("/air-walk")
def Air_Walk():
	return render_template("air-walk.html")

@app.route("/anathemic-reprisal")
def Anathematic_Reprisal():
	return render_template("anathemic-reprisal.html")

@app.route("/animal-vision")
def Animal_Vision():
	return render_template("animal-vision.html")

@app.route("/aqueous-orb")
def Aqueous_Orb():
	return render_template("aqueous-orb.html")

@app.route("/aromatic-lure")
def Aromatic_Lure():
	return render_template("aromatic-lure.html")

@app.route("/bestial-curse")
def Bestial_Curse():
	return render_template("bestial-curse.html")

@app.route("/call-the-blood")
def Call_the_Blood():
	return render_template("call-the-blood.html")

@app.route("/chroma-leach")
def Chroma_Leach():
	return render_template("chroma-leach.html")

@app.route("/chromatic-armor")
def Chromatic_Armor():
	return render_template("chromatic-armor.html")

@app.route("/chilling-darkness")
def Chilling_Darkness():
	return render_template("chilling-darkness.html")

@app.route("/claim-curse")
def Claim_Curse():
	return render_template("claim-curse.html")

@app.route("/circle-of-protection")
def Circle_of_Protection():
	return render_template("circle-of-protection.html")

@app.route("/clairaudience")
def Clairaudience():
	return render_template("clairaudience.html")

@app.route("/clairvoyance")
def Clairvoyance():
	return render_template("clairvoyance.html")

@app.route("/cloak-of-light")
def Cloak_of_Light():
	return render_template("cloak-of-light.html")

@app.route("/hazardous-terrain")
def Hazardous_Terrain():
	return render_template("hazardous-terrain.html")

@app.route("/structure")
def Structure():
	return render_template("structure.html")

@app.route("/cup-of-dust")
def Cup_of_Dust():
	return render_template("cup-of-dust.html")

@app.route("/daydreamers-curse")
def Daydreamers_Curse():
	return render_template("daydreamers-curse.html")

@app.route("/clownish-curse")
def Clownish_Curse():
	return render_template("clownish-curse.html")

@app.route("/confusion")
def Confusion():
	return render_template("confusion.html")

@app.route("/coral-eruption")
def Coral_Eruption():
	return render_template("coral-eruption.html")

@app.route("/countless-eyes")
def Countless_Eyes():
	return render_template("countless-eyes.html")

@app.route("/cozy-cabin")
def Cozy_Cabin():
	return render_template("cozy-cabin.html")

@app.route("/crashing-wave")
def Crashing_Wave():
	return render_template("crashing-wave.html")

@app.route("/creation")
def Creation():
	return render_template("creation.html")

@app.route("/crisis-of-faith")
def Crisis_of_Faith():
	return render_template("crisis-of-faith.html")

@app.route("/curse-of-lost-time")
def Curse_of_Lost_Time():
	return render_template("curse-of-lost-time.html")

@app.route("/days-weight")
def Days_Weight():
	return render_template("days-weight.html")

@app.route("/detect-scrying")
def Detect_Scrying():
	return render_template("detect-scrying.html")

@app.route("/dimension-door")
def Dimension_Door():
	return render_template("dimension-door.html")

@app.route("/dimensional-anchor")
def Dimensional_Anchor():
	return render_template("dimensional-anchor.html")

@app.route("/discern-lies")
def Discern_Lies():
	return render_template("discern-lies.html")

@app.route("/distracting-chatter")
def Distracting_Chatter():
	return render_template("distracting-chatter.html")

@app.route("/divine-wrath")
def Divine_Wrath():
	return render_template("divine-wrath.html")

@app.route("/fireball")
def Fireball():
	return render_template("fireball.html")

@app.route("/draw-the-lightning")
def Draw_the_Lightning():
	return render_template("draw-the-lightning.html")

@app.route("/dream-message")
def Dream_Message():
	return render_template("dream-message.html")

@app.route("/dull-ambition")
def Dull_Ambition():
	return render_template("dull-ambition.html")

@app.route("/earthbind")
def Earthbind():
	return render_template("earthbind.html")

@app.route("/elemental-absorption")
def Elemental_Absorption():
	return render_template("elemental-absorption.html")

@app.route("/elemental-annihilation-wave")
def Elemental_Annihilation_Wave():
	return render_template("elemental-annihilation-wave.html")

@app.route("/elemental-gift")
def Elemental_Gift():
	return render_template("elemental-gift.html")

@app.route("/enervation")
def Enervation():
	return render_template("enervation.html")

@app.route("/enthrall")
def Enthrall():
	return render_template("enthrall.html")

@app.route("/envenom-companion")
def Envenom_Companion():
	return render_template("envenom-companion.html")

@app.route("/sustain-a-spell")
def Sustain_a_Spell():
	return render_template("sustain-a-spell.html")

@app.route("/familiars-face")
def Familiars_Face():
	return render_template("familiars-face.html")

@app.route("/favorable-review")
def Favorable_Review():
	return render_template("favorable-review.html")

@app.route("/feet-to-fins")
def Feet_to_Fins():
	return render_template("feet-to-fins.html")

@app.route("/fire-shield")
def Fire_Shield():
	return render_template("fire-shield.html")

@app.route("/fly-9005114")
def Fly():
	return render_template("fly-9005114.html")

@app.route("/forgotten-lines")
def Forgotten_Lines():
	return render_template("forgotten-lines.html")

@app.route("/gaseous-form")
def Gaseous_Form():
	return render_template("gaseous-form.html")

@app.route("/gasping-marsh")
def Gasping_Marsh():
	return render_template("gasping-marsh.html")

@app.route("/ghostly-weapon")
def Ghostly_Weapon():
	return render_template("ghostly-weapon.html")

@app.route("/girzanjes-march")
def Girzanjes_March():
	return render_template("girzanjes-march.html")

@app.route("/glibness")
def Glibness():
	return render_template("glibness.html")

@app.route("/globe-of-invulnerability")
def Globe_of_Invulnerability():
	return render_template("globe-of-invulnerability.html")

@app.route("/glyph-of-warding")
def Glyph_of_Warding():
	return render_template("glyph-of-warding.html")

@app.route("/gravity-well")
def Gravity_Well():
	return render_template("gravity-well.html")

@app.route("/ghostly-tragedy")
def Ghostly_Tragedy():
	return render_template("ghostly-tragedy.html")

@app.route("/hallucinatory-terrain")
def Hallucinatory_Terrain():
	return render_template("hallucinatory-terrain.html")

@app.route("/haste")
def Haste():
	return render_template("haste.html")

@app.route("/heroism")
def Heroism():
	return render_template("heroism.html")

@app.route("/holy-cascade")
def Holy_Cascade():
	return render_template("holy-cascade.html")

@app.route("/hydraulic-torrent")
def Hydraulic_Torrent():
	return render_template("hydraulic-torrent.html")

@app.route("/hypercognition")
def Hypercognition():
	return render_template("hypercognition.html")

@app.route("/hypnotic-pattern")
def Hypnotic_Pattern():
	return render_template("hypnotic-pattern.html")

@app.route("/ice-storm")
def Ice_Storm():
	return render_template("ice-storm.html")

@app.route("/impending-doom")
def Impending_Doom():
	return render_template("impending-doom.html")

@app.route("/infectious-melody")
def Infectious_Melody():
	return render_template("infectious-melody.html")

@app.route("/internal-insurrection")
def Internal_Insurrection():
	return render_template("internal-insurrection.html")

@app.route("/levitate")
def Levitate():
	return render_template("levitate.html")

@app.route("/invisibility-sphere")
def Invisibility_Sphere():
	return render_template("invisibility-sphere.html")

@app.route("/invisibility-curtain")
def Invisibility_Curtain():
	return render_template("invisibility-curtain.html")

@app.route("/life-connection")
def Life_Connection():
	return render_template("life-connection.html")

@app.route("/lightning-bolt")
def Lightning_Bolt():
	return render_template("lightning-bolt.html")

@app.route("/locate")
def Locate():
	return render_template("locate.html")

@app.route("/mad-monkeys")
def Mad_Monkeys():
	return render_template("mad-monkeys.html")

@app.route("/magic-mailbox")
def Magic_Mailbox():
	return render_template("magic-mailbox.html")

@app.route("/magnetic-acceleration")
def Magnetic_Acceleration():
	return render_template("magnetic-acceleration.html")

@app.route("/magical-fetters")
def Magical_Fetters():
	return render_template("magical-fetters.html")

@app.route("/meld-into-stone")
def Meld_Into_Stone():
	return render_template("meld-into-stone.html")

@app.route("/mind-of-menace")
def Mind_of_Menace():
	return render_template("mind-of-menace.html")

@app.route("/mind-reading")
def Mind_Reading():
	return render_template("mind-reading.html")

@app.route("/mirrors-misfortune")
def Mirrors_Misfortune():
	return render_template("mirrors-misfortune.html")

@app.route("/modify-memory")
def Modify_Memory():
	return render_template("modify-memory.html")

@app.route("/moonlight-ray")
def Moonlight_Ray():
	return render_template("moonlight-ray.html")

@app.route("/murderous-vine")
def Murderous_Vine():
	return render_template("murderous-vine.html")

@app.route("/neutralize-poison")
def Neutralize_Poison():
	return render_template("neutralize-poison.html")

@app.route("/necrotic-radiation")
def Necrotic_Radiation():
	return render_template("necrotic-radiation.html")

@app.route("/nondetection")
def Nondetection():
	return render_template("nondetection.html")

@app.route("/nightmare")
def Nightmare():
	return render_template("nightmare.html")

@app.route("/oneiric-mire")
def Oneiric_Mire():
	return render_template("oneiric-mire.html")

@app.route("/organsight")
def Organsight():
	return render_template("organsight.html")

@app.route("/outcasts-curse")
def Outcasts_Curse():
	return render_template("outcasts-curse.html")

@app.route("/painful-vibrations")
def Painful_Vibrations():
	return render_template("painful-vibrations.html")

@app.route("/perseis-precautions")
def Perseis_Precautions():
	return render_template("perseis-precautions.html")

@app.route("/petal-storm")
def Petal_Storm():
	return render_template("petal-storm.html")

@app.route("/phantasmal-killer")
def Phantasmal_Killer():
	return render_template("phantasmal-killer.html")

@app.route("/phantom-prison")
def Phantom_Prison():
	return render_template("phantom-prison.html")

@app.route("/pillar-of-water")
def Pillar_of_Water():
	return render_template("pillar-of-water.html")

@app.route("/private-sanctum")
def Private_Sanctum():
	return render_template("private-sanctum.html")

@app.route("/pyrotechnics")
def Pyrotechnics():
	return render_template("pyrotechnics.html")

@app.route("/read-omens")
def Read_Omens():
	return render_template("read-omens.html")

@app.route("/resounding-barrier")
def Resounding_Barrier():
	return render_template("resounding-barrier.html")

@app.route("/reflective-scales")
def Reflective_Scales():
	return render_template("reflective-scales.html")

@app.route("/remove-curse")
def Remove_Curse():
	return render_template("remove-curse.html")

@app.route("/remove-disease")
def Remove_Disease():
	return render_template("remove-disease.html")

@app.route("/replicate")
def Replicate():
	return render_template("replicate.html")

@app.route("/resilient-sphere")
def Resilient_Sphere():
	return render_template("resilient-sphere.html")

@app.route("/roaring-applause")
def Roaring_Applause():
	return render_template("roaring-applause.html")

@app.route("/rouse-skeletons")
def Rouse_Skeletons():
	return render_template("rouse-skeletons.html")

@app.route("/rusting-grasp")
def Rusting_Grasp():
	return render_template("rusting-grasp.html")

@app.route("/rope-trick")
def Rope_Trick():
	return render_template("rope-trick.html")

@app.route("/sanctified-ground")
def Sanctified_Ground():
	return render_template("sanctified-ground.html")

@app.route("/sanguine-mist")
def Sanguine_Mist():
	return render_template("sanguine-mist.html")

@app.route("/savants-curse")
def Savants_Curse():
	return render_template("savants-curse.html")

@app.route("/sculpt-sound")
def Sculpt_Sound():
	return render_template("sculpt-sound.html")

@app.route("/seal-fate")
def Seal_Fate():
	return render_template("seal-fate.html")

@app.route("/searing-light")
def Searing_Light():
	return render_template("searing-light.html")

@app.route("/secret-page")
def Secret_Page():
	return render_template("secret-page.html")

@app.route("/shadow-projectile")
def Shadow_Projectile():
	return render_template("shadow-projectile.html")

@app.route("/shape-stone")
def Shape_Stone():
	return render_template("shape-stone.html")

@app.route("/shift-blame")
def Shift_Blame():
	return render_template("shift-blame.html")

@app.route("/shifting-sand")
def Shifting_Sand():
	return render_template("shifting-sand.html")

@app.route("/show-the-way")
def Show_the_Way():
	return render_template("show-the-way.html")

@app.route("/shrink-item")
def Shrink_Item():
	return render_template("shrink-item.html")

@app.route("/solid-fog")
def Solid_Fog():
	return render_template("solid-fog.html")

@app.route("/soothing-blossoms")
def Soothing_Blossoms():
	return render_template("soothing-blossoms.html")

@app.route("/speak-with-plants-3775319")
def Speak_With_Plants():
	return render_template("speak-with-plants-3775319.html")

@app.route("/spell-immunity")
def Spell_Immunity():
	return render_template("spell-immunity.html")

@app.route("/spike-stones")
def Spike_Stones():
	return render_template("spike-stones.html")

@app.route("/spiritual-anamnesis")
def Spiritual_Anamnesis():
	return render_template("spiritual-anamnesis.html")

@app.route("/spiritual-attunement")
def Spiritual_Attunement():
	return render_template("spiritual-attunement.html")

@app.route("/stinking-cloud")
def Stinking_Cloud():
	return render_template("stinking-cloud.html")

@app.route("/stoneskin")
def Stoneskin():
	return render_template("stoneskin.html")

@app.route("/sudden-recollection")
def Sudden_Recollection():
	return render_template("sudden-recollection.html")

@app.route("/suggestion")
def Suggestion():
	return render_template("suggestion.html")

@app.route("/swarming-wasp-stings")
def Swarming_Wasp_Stings():
	return render_template("swarming-wasp-stings.html")

@app.route("/talking-corpse")
def Talking_Corpse():
	return render_template("talking-corpse.html")

@app.route("/telepathy")
def Telepathy():
	return render_template("telepathy.html")

@app.route("/threefold-aspect")
def Threefold_Aspect():
	return render_template("threefold-aspect.html")

@app.route("/time-jump")
def Time_Jump():
	return render_template("time-jump.html")

@app.route("/tortoise-and-the-hare")
def Tortoise_and_the_Hare():
	return render_template("tortoise-and-the-hare.html")

@app.route("/umbral-graft")
def Umbral_Graft():
	return render_template("umbral-graft.html")

@app.route("/unseasonable-squall")
def Unseasonable_Squall():
	return render_template("unseasonable-squall.html")

@app.route("/vampiric-maiden")
def Vampiric_Maiden():
	return render_template("vampiric-maiden.html")

@app.route("/vampiric-touch")
def Vampiric_Touch():
	return render_template("vampiric-touch.html")

@app.route("/variable-gravity")
def Variable_Gravity():
	return render_template("variable-gravity.html")

@app.route("/veil")
def Veil():
	return render_template("veil.html")

@app.route("/wall-of-fire")
def Wall_of_Fire():
	return render_template("wall-of-fire.html")

@app.route("/wall-of-radiance")
def Wall_of_Radiance():
	return render_template("wall-of-radiance.html")

@app.route("/wall-of-shadow")
def Wall_of_Shadow():
	return render_template("wall-of-shadow.html")

@app.route("/wall-of-thorns")
def Wall_of_Thorns():
	return render_template("wall-of-thorns.html")

@app.route("/wall-of-water")
def Wall_of_Water():
	return render_template("wall-of-water.html")

@app.route("/wall-of-wind")
def Wall_of_Wind():
	return render_template("wall-of-wind.html")

@app.route("/wanderers-guide")
def Wanderers_Guide():
	return render_template("wanderers-guide.html")

@app.route("/warding-aggression")
def Warding_Aggression():
	return render_template("warding-aggression.html")

@app.route("/weapon-storm")
def Weapon_Storm():
	return render_template("weapon-storm.html")

@app.route("/web-of-eyes")
def Web_of_Eyes():
	return render_template("web-of-eyes.html")

@app.route("/whirling-scarves")
def Whirling_Scarves():
	return render_template("whirling-scarves.html")

@app.route("/winning-streak")
def Winning_Streak():
	return render_template("winning-streak.html")

@app.route("/zone-of-truth")
def Zone_of_Truth():
	return render_template("zone-of-truth.html")

@app.route("/bind-undead")
def Bind_Undead():
	return render_template("bind-undead.html")

@app.route("/blazing-dive")
def Blazing_Dive():
	return render_template("blazing-dive.html")

@app.route("/blindness-6255307")
def Blindness():
	return render_template("blindness-6255307.html")

@app.route("/blink")
def Blink():
	return render_template("blink.html")

@app.route("/bloodspray-curse")
def Bloodspray_Curse():
	return render_template("bloodspray-curse.html")

@app.route("/freedom-of-movement")
def Freedom_of_Movement():
	return render_template("freedom-of-movement.html")

@app.route("/ocular-overload")
def Ocular_Overload():
	return render_template("ocular-overload.html")

@app.route("/paralyze")
def Paralyze():
	return render_template("paralyze.html")

@app.route("/pernicious-poltergeist")
def Pernicious_Poltergeist():
	return render_template("pernicious-poltergeist.html")

@app.route("/safe-passage")
def Safe_Passage():
	return render_template("safe-passage.html")

@app.route("/slow")
def Slow():
	return render_template("slow.html")

@app.route("/abyssal-plague")
def Abyssal_Plague():
	return render_template("abyssal-plague.html")

@app.route("/acid-storm")
def Acid_Storm():
	return render_template("acid-storm.html")

@app.route("/aura-of-the-unremarkable")
def Aura_of_the_Unremarkable():
	return render_template("aura-of-the-unremarkable.html")

@app.route("/baleful-polymorph")
def Baleful_Polymorph():
	return render_template("baleful-polymorph.html")

@app.route("/bandits-doom")
def Bandits_Doom():
	return render_template("bandits-doom.html")

@app.route("/banishment")
def Banishment():
	return render_template("banishment.html")

@app.route("/black-tentacles")
def Black_Tentacles():
	return render_template("black-tentacles.html")

@app.route("/blackfingers-blades")
def Blackfingers_Blades():
	return render_template("blackfingers-blades.html")

@app.route("/blade-barrier")
def Blade_Barrier():
	return render_template("blade-barrier.html")

@app.route("/blanket-of-stars")
def Blanket_of_Stars():
	return render_template("blanket-of-stars.html")

@app.route("/blazing-fissure")
def Blazing_Fissure():
	return render_template("blazing-fissure.html")

@app.route("/blessing-of-defiance")
def Blessing_of_Defiance():
	return render_template("blessing-of-defiance.html")

@app.route("/blinding-fury")
def Blinding_Fury():
	return render_template("blinding-fury.html")

@app.route("/blink-charge")
def Blink_Charge():
	return render_template("blink-charge.html")

@app.route("/blister")
def Blister():
	return render_template("blister.html")

@app.route("/blood-feast")
def Blood_Feast():
	return render_template("blood-feast.html")

@app.route("/cast-into-time")
def Cast_Into_Time():
	return render_template("cast-into-time.html")

@app.route("/chain-lightning")
def Chain_Lightning():
	return render_template("chain-lightning.html")

@app.route("/chameleon-coat")
def Chameleon_Coat():
	return render_template("chameleon-coat.html")

@app.route("/chromatic-image")
def Chromatic_Image():
	return render_template("chromatic-image.html")

@app.route("/cloak-of-colors")
def Cloak_of_Colors():
	return render_template("cloak-of-colors.html")

@app.route("/cloudkill")
def Cloudkill():
	return render_template("cloudkill.html")

@app.route("/collective-transposition")
def Collective_Transposition():
	return render_template("collective-transposition.html")

@app.route("/cone-of-cold")
def Cone_of_Cold():
	return render_template("cone-of-cold.html")

@app.route("/control-water")
def Control_Water():
	return render_template("control-water.html")

@app.route("/crushing-despair")
def Crushing_Despair():
	return render_template("crushing-despair.html")

@app.route("/death-ward")
def Death_Ward():
	return render_template("death-ward.html")

@app.route("/disintegrate")
def Disintegrate():
	return render_template("disintegrate.html")

@app.route("/dominate")
def Dominate():
	return render_template("dominate.html")

@app.route("/dreaming-potential")
def Dreaming_Potential():
	return render_template("dreaming-potential.html")

@app.route("/drop-dead")
def Drop_Dead():
	return render_template("drop-dead.html")

@app.route("/ectoplasmic-expulsion")
def Ectoplasmic_Expulsion():
	return render_template("ectoplasmic-expulsion.html")

@app.route("/elemental-confluence")
def Elemental_Confluence():
	return render_template("elemental-confluence.html")

@app.route("/false-vision")
def False_Vision():
	return render_template("false-vision.html")

@app.route("/feeblemind")
def Feeblemind():
	return render_template("feeblemind.html")

@app.route("/field-of-life")
def Field_of_Life():
	return render_template("field-of-life.html")

@app.route("/fire-seeds")
def Fire_Seeds():
	return render_template("fire-seeds.html")

@app.route("/flame-strike")
def Flame_Strike():
	return render_template("flame-strike.html")

@app.route("/flame-vortex")
def Flame_Vortex():
	return render_template("flame-vortex.html")

@app.route("/flammable-fumes")
def Flammable_Fumes():
	return render_template("flammable-fumes.html")

@app.route("/flesh-to-stone")
def Flesh_to_Stone():
	return render_template("flesh-to-stone.html")

@app.route("/flowing-strike")
def Flowing_Strike():
	return render_template("flowing-strike.html")

@app.route("/fly-5624108")
def Fly():
	return render_template("fly-5624108.html")

@app.route("/forceful-hand")
def Forceful_Hand():
	return render_template("forceful-hand.html")

@app.route("/geyser")
def Geyser():
	return render_template("geyser.html")

@app.route("/glimmer-of-charm")
def Glimmer_of_Charm():
	return render_template("glimmer-of-charm.html")

@app.route("/grisly-growths")
def Grisly_Growths():
	return render_template("grisly-growths.html")

@app.route("/halcyon-infusion")
def Halcyon_Infusion():
	return render_template("halcyon-infusion.html")

@app.route("/hallucination")
def Hallucination():
	return render_template("hallucination.html")

@app.route("/illusory-scene")
def Illusory_Scene():
	return render_template("illusory-scene.html")

@app.route("/impaling-spike")
def Impaling_Spike():
	return render_template("impaling-spike.html")

@app.route("/healing-well")
def Healing_Well():
	return render_template("healing-well.html")

@app.route("/inevitable-disaster")
def Inevitable_Disaster():
	return render_template("inevitable-disaster.html")

@app.route("/invoke-spirits")
def Invoke_Spirits():
	return render_template("invoke-spirits.html")

@app.route("/lightning-storm")
def Lightning_Storm():
	return render_template("lightning-storm.html")

@app.route("/mantle-of-the-frozen-heart")
def Mantle_of_the_Frozen_Heart():
	return render_template("mantle-of-the-frozen-heart.html")

@app.route("/mantle-of-the-magma-heart")
def Mantle_of_the_Magma_Heart():
	return render_template("mantle-of-the-magma-heart.html")

@app.route("/mariners-curse")
def Mariners_Curse():
	return render_template("mariners-curse.html")

@app.route("/mind-probe")
def Mind_Probe():
	return render_template("mind-probe.html")

@app.route("/mirecloak")
def Mirecloak():
	return render_template("mirecloak.html")

@app.route("/mirror-malefactors")
def Mirror_Malefactors():
	return render_template("mirror-malefactors.html")

@app.route("/mislead")
def Mislead():
	return render_template("mislead.html")

@app.route("/moon-frenzy")
def Moon_Frenzy():
	return render_template("moon-frenzy.html")

@app.route("/natures-reprisal")
def Natures_Reprisal():
	return render_template("natures-reprisal.html")

@app.route("/necrotize")
def Necrotize():
	return render_template("necrotize.html")

@app.route("/passwall")
def Passwall():
	return render_template("passwall.html")

@app.route("/phantasmal-calamity")
def Phantasmal_Calamity():
	return render_template("phantasmal-calamity.html")

@app.route("/pillars-of-sand")
def Pillars_of_Sand():
	return render_template("pillars-of-sand.html")

@app.route("/portrait-of-the-artist")
def Portrait_of_the_Artist():
	return render_template("portrait-of-the-artist.html")

@app.route("/prying-eye")
def Prying_Eye():
	return render_template("prying-eye.html")

@app.route("/purple-worm-sting")
def Purple_Worm_Sting():
	return render_template("purple-worm-sting.html")

@app.route("/ravening-maw")
def Ravening_Maw():
	return render_template("ravening-maw.html")

@app.route("/repelling-pulse")
def Repelling_Pulse():
	return render_template("repelling-pulse.html")

@app.route("/repulsion")
def Repulsion():
	return render_template("repulsion.html")

@app.route("/return-beacon")
def Return_Beacon():
	return render_template("return-beacon.html")

@app.route("/rewinding-step")
def Rewinding_Step():
	return render_template("rewinding-step.html")

@app.route("/rip-the-spirit")
def Rip_the_Spirit():
	return render_template("rip-the-spirit.html")

@app.route("/secret-chest")
def Secret_Chest():
	return render_template("secret-chest.html")

@app.route("/scrying")
def Scrying():
	return render_template("scrying.html")

@app.route("/sending")
def Sending():
	return render_template("sending.html")

@app.route("/shadow-blast")
def Shadow_Blast():
	return render_template("shadow-blast.html")

@app.route("/spirit-blast")
def Spirit_Blast():
	return render_template("spirit-blast.html")

@app.route("/spiritual-guardian")
def Spiritual_Guardian():
	return render_template("spiritual-guardian.html")

@app.route("/stormburst")
def Stormburst():
	return render_template("stormburst.html")

@app.route("/strange-geometry")
def Strange_Geometry():
	return render_template("strange-geometry.html")

@app.route("/synaptic-pulse")
def Synaptic_Pulse():
	return render_template("synaptic-pulse.html")

@app.route("/synesthesia")
def Synesthesia():
	return render_template("synesthesia.html")

@app.route("/telekinetic-haul")
def Telekinetic_Haul():
	return render_template("telekinetic-haul.html")

@app.route("/tangling-creepers")
def Tangling_Creepers():
	return render_template("tangling-creepers.html")

@app.route("/unexpected-transposition")
def Unexpected_Transposition():
	return render_template("unexpected-transposition.html")

@app.route("/vampiric-exsanguination")
def Vampiric_Exsanguination():
	return render_template("vampiric-exsanguination.html")

@app.route("/vibrant-pattern")
def Vibrant_Pattern():
	return render_template("vibrant-pattern.html")

@app.route("/wall-of-force")
def Wall_of_Force():
	return render_template("wall-of-force.html")

@app.route("/wall-of-ice")
def Wall_of_Ice():
	return render_template("wall-of-ice.html")

@app.route("/wall-of-stone")
def Wall_of_Stone():
	return render_template("wall-of-stone.html")

@app.route("/wyvern-sting")
def Wyvern_Sting():
	return render_template("wyvern-sting.html")

@app.route("/zealous-conviction")
def Zealous_Conviction():
	return render_template("zealous-conviction.html")

@app.route("/scintillating-safeguard")
def Scintillating_Safeguard():
	return render_template("scintillating-safeguard.html")

@app.route("/shadow-syphon")
def Shadow_Syphon():
	return render_template("shadow-syphon.html")

@app.route("/spellwrack")
def Spellwrack():
	return render_template("spellwrack.html")

@app.route("/stone-tell")
def Stone_Tell():
	return render_template("stone-tell.html")

@app.route("/stone-to-flesh")
def Stone_to_Flesh():
	return render_template("stone-to-flesh.html")

@app.route("/subconscious-suggestion")
def Subconscious_Suggestion():
	return render_template("subconscious-suggestion.html")

@app.route("/telepathic-bond")
def Telepathic_Bond():
	return render_template("telepathic-bond.html")

@app.route("/temporal-ward")
def Temporal_Ward():
	return render_template("temporal-ward.html")

@app.route("/temporary-glyph")
def Temporary_Glyph():
	return render_template("temporary-glyph.html")

@app.route("/tongues")
def Tongues():
	return render_template("tongues.html")

@app.route("/transmute-rock-to-mud")
def Transmute_Rock_to_Mud():
	return render_template("transmute-rock-to-mud.html")

@app.route("/tree-stride")
def Tree_Stride():
	return render_template("tree-stride.html")

@app.route("/true-seeing")
def True_Seeing():
	return render_template("true-seeing.html")

@app.route("/wall-of-flesh")
def Wall_of_Flesh():
	return render_template("wall-of-flesh.html")

@app.route("/zero-gravity")
def Zero_Gravity():
	return render_template("zero-gravity.html")

@app.route("/all-is-one-one-is-all")
def All_is_One_One_is_All():
	return render_template("all-is-one-one-is-all.html")

@app.route("/antimagic-field")
def Antimagic_Field():
	return render_template("antimagic-field.html")

@app.route("/blightburn-blast")
def Blightburn_Blast():
	return render_template("blightburn-blast.html")

@app.route("/burning-blossoms")
def Burning_Blossoms():
	return render_template("burning-blossoms.html")

@app.route("/deitys-strike")
def Deitys_Strike():
	return render_template("deitys-strike.html")

@app.route("/deluge")
def Deluge():
	return render_template("deluge.html")

@app.route("/devour-life")
def Devour_Life():
	return render_template("devour-life.html")

@app.route("/disappearance")
def Disappearance():
	return render_template("disappearance.html")

@app.route("/divine-armageddon")
def Divine_Armageddon():
	return render_template("divine-armageddon.html")

@app.route("/divine-aura")
def Divine_Aura():
	return render_template("divine-aura.html")

@app.route("/divine-decree")
def Divine_Decree():
	return render_template("divine-decree.html")

@app.route("/divine-inspiration")
def Divine_Inspiration():
	return render_template("divine-inspiration.html")

@app.route("/divine-vessel")
def Divine_Vessel():
	return render_template("divine-vessel.html")

@app.route("/dream-council")
def Dream_Council():
	return render_template("dream-council.html")

@app.route("/duplicate-foe")
def Duplicate_Foe():
	return render_template("duplicate-foe.html")

@app.route("/eclipse-burst")
def Eclipse_Burst():
	return render_template("eclipse-burst.html")

@app.route("/energy-aegis")
def Energy_Aegis():
	return render_template("energy-aegis.html")

@app.route("/entrancing-eyes")
def Entrancing_Eyes():
	return render_template("entrancing-eyes.html")

@app.route("/ethereal-jaunt")
def Ethereal_Jaunt():
	return render_template("ethereal-jaunt.html")

@app.route("/corrosive-body")
def Corrosive_Body():
	return render_template("corrosive-body.html")

@app.route("/frigid-flurry")
def Frigid_Flurry():
	return render_template("frigid-flurry.html")

@app.route("/horrid-wilting")
def Horrid_Wilting():
	return render_template("horrid-wilting.html")

@app.route("/inexhaustible-cynicism")
def Inexhaustible_Cynicism():
	return render_template("inexhaustible-cynicism.html")

@app.route("/leng-sting")
def Leng_Sting():
	return render_template("leng-sting.html")

@app.route("/mask-of-terror")
def Mask_of_Terror():
	return render_template("mask-of-terror.html")

@app.route("/mind-blank")
def Mind_Blank():
	return render_template("mind-blank.html")

@app.route("/moment-of-renewal")
def Moment_of_Renewal():
	return render_template("moment-of-renewal.html")

@app.route("/moonburst")
def Moonburst():
	return render_template("moonburst.html")

@app.route("/planeshift")
def Planeshift():
	return render_template("planeshift.html")

@app.route("/polar-ray")
def Polar_Ray():
	return render_template("polar-ray.html")

@app.route("/possession")
def Possession():
	return render_template("possession.html")

@app.route("/power-word-blind")
def Power_Word_Blind():
	return render_template("power-word-blind.html")

@app.route("/prismatic-armor")
def Prismatic_Armor():
	return render_template("prismatic-armor.html")

@app.route("/project-image")
def Project_Image():
	return render_template("project-image.html")

@app.route("/punishing-winds")
def Punishing_Winds():
	return render_template("punishing-winds.html")

@app.route("/retrocognition")
def Retrocognition():
	return render_template("retrocognition.html")

@app.route("/reverse-gravity")
def Reverse_Gravity():
	return render_template("reverse-gravity.html")

@app.route("/scintillating-pattern")
def Scintillating_Pattern():
	return render_template("scintillating-pattern.html")

@app.route("/shadow-raid")
def Shadow_Raid():
	return render_template("shadow-raid.html")

@app.route("/spell-turning")
def Spell_Turning():
	return render_template("spell-turning.html")

@app.route("/spirit-song")
def Spirit_Song():
	return render_template("spirit-song.html")

@app.route("/spiritual-epidemic")
def Spiritual_Epidemic():
	return render_template("spiritual-epidemic.html")

@app.route("/summon-archmage")
def Summon_Archmage():
	return render_template("summon-archmage.html")

@app.route("/summon-deific-herald")
def Summon_Deific_Herald():
	return render_template("summon-deific-herald.html")

@app.route("/sunburst")
def Sunburst():
	return render_template("sunburst.html")

@app.route("/tempest-of-shades")
def Tempest_of_Shades():
	return render_template("tempest-of-shades.html")

@app.route("/time-beacon")
def Time_Beacon():
	return render_template("time-beacon.html")

@app.route("/true-target")
def True_Target():
	return render_template("true-target.html")

@app.route("/uncontrollable-dance")
def Uncontrollable_Dance():
	return render_template("uncontrollable-dance.html")

@app.route("/undermine-reality")
def Undermine_Reality():
	return render_template("undermine-reality.html")

@app.route("/unfettered-pack")
def Unfettered_Pack():
	return render_template("unfettered-pack.html")

@app.route("/unrelenting-observation")
def Unrelenting_Observation():
	return render_template("unrelenting-observation.html")

@app.route("/visions-of-danger")
def Visions_of_Danger():
	return render_template("visions-of-danger.html")

@app.route("/volcanic-eruption")
def Volcanic_Eruption():
	return render_template("volcanic-eruption.html")

@app.route("/warp-mind")
def Warp_Mind():
	return render_template("warp-mind.html")

@app.route("/whirlwind")
def Whirlwind():
	return render_template("whirlwind.html")

@app.route("/boil-blood")
def Boil_Blood():
	return render_template("boil-blood.html")

@app.route("/canticle-of-everlasting-grief")
def Canticle_of_Everlasting_Grief():
	return render_template("canticle-of-everlasting-grief.html")

@app.route("/clone-companion")
def Clone_Companion():
	return render_template("clone-companion.html")

@app.route("/contingency")
def Contingency():
	return render_template("contingency.html")

@app.route("/control-sand")
def Control_Sand():
	return render_template("control-sand.html")

@app.route("/dimensional-lock")
def Dimensional_Lock():
	return render_template("dimensional-lock.html")

@app.route("/discern-location")
def Discern_Location():
	return render_template("discern-location.html")

@app.route("/earthquake")
def Earthquake():
	return render_template("earthquake.html")

@app.route("/fiery-body")
def Fiery_Body():
	return render_template("fiery-body.html")

@app.route("/finger-of-death")
def Finger_of_Death():
	return render_template("finger-of-death.html")

@app.route("/force-cage")
def Force_Cage():
	return render_template("force-cage.html")

@app.route("/power-word-stun")
def Power_Word_Stun():
	return render_template("power-word-stun.html")

@app.route("/prismatic-wall")
def Prismatic_Wall():
	return render_template("prismatic-wall.html")

@app.route("/return-to-essence")
def Return_to_Essence():
	return render_template("return-to-essence.html")

@app.route("/golem")
def Golem():
	return render_template("golem.html")

@app.route("/frightful-presence-monster")
def Frightful_Presence__Monster_():
	return render_template("frightful-presence-monster.html")

@app.route("/polymorph")
def Polymorph():
	return render_template("polymorph.html")

@app.route("/grab-monster-ability")
def Grab__Monster_Ability_():
	return render_template("grab-monster-ability.html")

@app.route("/trample-monster-ability")
def Trample__Monster_Ability_():
	return render_template("trample-monster-ability.html")

@app.route("/swallow-whole-monster-ability")
def Swallow_Whole__Monster_Ability_():
	return render_template("swallow-whole-monster-ability.html")

@app.route("/constrict-monster-action")
def Constrict__Monster_Action_():
	return render_template("constrict-monster-action.html")

@app.route("/pest-form")
def Pest_Form():
	return render_template("pest-form.html")

@app.route("/swarm-9641624")
def Swarm():
	return render_template("swarm-9641624.html")

@app.route("/aquatic")
def Aquatic():
	return render_template("aquatic.html")

@app.route("/amphibious-6493034")
def Amphibious():
	return render_template("amphibious-6493034.html")

@app.route("/narwhal")
def Narwhal():
	return render_template("narwhal.html")

@app.route("/piranah-swarm")
def Piranah_Swarm():
	return render_template("piranah-swarm.html")

@app.route("/aasimar-redeemer")
def Aasimar_Redeemer():
	return render_template("aasimar-redeemer.html")

@app.route("/abandoned-zealot")
def Abandoned_Zealot():
	return render_template("abandoned-zealot.html")

@app.route("/abrikandilu-wrecker-demon")
def Abrikandilu__Wrecker_Demon_():
	return render_template("abrikandilu-wrecker-demon.html")

@app.route("/adamantine-golem")
def Adamantine_Golem():
	return render_template("adamantine-golem.html")

@app.route("/adhukait")
def Adhukait():
	return render_template("adhukait.html")

@app.route("/adlet-thrower")
def Adlet_Thrower():
	return render_template("adlet-thrower.html")

@app.route("/tiger")
def Tiger():
	return render_template("tiger.html")

@app.route("/rhinoceros")
def Rhinoceros():
	return render_template("rhinoceros.html")

@app.route("/emperor-cobra")
def Emperor_Cobra():
	return render_template("emperor-cobra.html")

@app.route("/cave-bear")
def Cave_Bear():
	return render_template("cave-bear.html")

@app.route("/dire-wolf")
def Dire_Wolf():
	return render_template("dire-wolf.html")

@app.route("/giant-moray-eel")
def Giant_Moray_Eel():
	return render_template("giant-moray-eel.html")

@app.route("/owlbear")
def Owlbear():
	return render_template("owlbear.html")

@app.route("/giant-tarantula")
def Giant_Tarantula():
	return render_template("giant-tarantula.html")

@app.route("/great-white-shark")
def Great_White_Shark():
	return render_template("great-white-shark.html")

@app.route("/elephant")
def Elephant():
	return render_template("elephant.html")

@app.route("/megalania")
def Megalania():
	return render_template("megalania.html")

@app.route("/blood-boar")
def Blood_Boar():
	return render_template("blood-boar.html")

@app.route("/improved-grab")
def Improved_Grab():
	return render_template("improved-grab.html")

@app.route("/giant-squid")
def Giant_Squid():
	return render_template("giant-squid.html")

@app.route("/deadly-mantis")
def Deadly_Mantis():
	return render_template("deadly-mantis.html")

@app.route("/megaprimatus")
def Megaprimatus():
	return render_template("megaprimatus.html")

@app.route("/aurumvorax")
def Aurumvorax():
	return render_template("aurumvorax.html")

@app.route("/bulette")
def Bulette():
	return render_template("bulette.html")

@app.route("/krooth")
def Krooth():
	return render_template("krooth.html")

@app.route("/lion")
def Lion():
	return render_template("lion.html")

@app.route("/grizzly-bear")
def Grizzly_Bear():
	return render_template("grizzly-bear.html")

@app.route("/giant-wasp")
def Giant_Wasp():
	return render_template("giant-wasp.html")

@app.route("/gryphon")
def Gryphon():
	return render_template("gryphon.html")

@app.route("/quetzcoatlus")
def Quetzcoatlus():
	return render_template("quetzcoatlus.html")

@app.route("/mist-stalker")
def Mist_Stalker():
	return render_template("mist-stalker.html")

@app.route("/filth-fire")
def Filth_Fire():
	return render_template("filth-fire.html")

@app.route("/earthen-destrier")
def Earthen_Destrier():
	return render_template("earthen-destrier.html")

@app.route("/living-thunderclap")
def Living_Thunderclap():
	return render_template("living-thunderclap.html")

@app.route("/living-landslide")
def Living_Landslide():
	return render_template("living-landslide.html")

@app.route("/living-waterfall")
def Living_Waterfall():
	return render_template("living-waterfall.html")

@app.route("/living-whirlwind")
def Living_Whirlwind():
	return render_template("living-whirlwind.html")

@app.route("/living-wildfire")
def Living_Wildfire():
	return render_template("living-wildfire.html")

@app.route("/belker")
def Belker():
	return render_template("belker.html")

@app.route("/blizzardborn")
def Blizzardborn():
	return render_template("blizzardborn.html")

@app.route("/sand-sentry")
def Sand_Sentry():
	return render_template("sand-sentry.html")

@app.route("/striding-fire")
def Striding_Fire():
	return render_template("striding-fire.html")

@app.route("/invisible-stalker")
def Invisible_Stalker():
	return render_template("invisible-stalker.html")

@app.route("/quatoid")
def Quatoid():
	return render_template("quatoid.html")

@app.route("/salamander")
def Salamander():
	return render_template("salamander.html")

@app.route("/xorn")
def Xorn():
	return render_template("xorn.html")

@app.route("/summon-construct")
def Summon_Construct():
	return render_template("summon-construct.html")

@app.route("/dryad")
def Dryad():
	return render_template("dryad.html")

@app.route("/tooth-fairy-swarm")
def Tooth_Fairy_Swarm():
	return render_template("tooth-fairy-swarm.html")

@app.route("/unicorn")
def Unicorn():
	return render_template("unicorn.html")

@app.route("/minion")
def Minion():
	return render_template("minion.html")

@app.route("/pixie")
def Pixie():
	return render_template("pixie.html")

@app.route("/satyr")
def Satyr():
	return render_template("satyr.html")

@app.route("/redcap")
def Redcap():
	return render_template("redcap.html")

@app.route("/kelpie")
def Kelpie():
	return render_template("kelpie.html")

@app.route("/grimstalker")
def Grimstalker():
	return render_template("grimstalker.html")

@app.route("/lurker-in-light")
def Lurker_in_Light():
	return render_template("lurker-in-light.html")

@app.route("/eloko")
def Eloko():
	return render_template("eloko.html")

@app.route("/elananx")
def Elananx():
	return render_template("elananx.html")

@app.route("/pummeling-rubble")
def Pummeling_Rubble():
	return render_template("pummeling-rubble.html")

@app.route("/lampad")
def Lampad():
	return render_template("lampad.html")

@app.route("/summon-fey")
def Summon_Fey():
	return render_template("summon-fey.html")

@app.route("/esobok")
def Esobok():
	return render_template("esobok.html")

@app.route("/hell-hound")
def Hell_Hound():
	return render_template("hell-hound.html")

@app.route("/lantern-archon")
def Lantern_Archon():
	return render_template("lantern-archon.html")

@app.route("/summon-lesser-servitor")
def Summon_Lesser_Servitor():
	return render_template("summon-lesser-servitor.html")

@app.route("/arboreal-warden")
def Arboreal_Warden():
	return render_template("arboreal-warden.html")

@app.route("/calathgar")
def Calathgar():
	return render_template("calathgar.html")

@app.route("/myceloid")
def Myceloid():
	return render_template("myceloid.html")

@app.route("/awakened-tree")
def Awakened_Tree():
	return render_template("awakened-tree.html")

@app.route("/basidirond")
def Basidirond():
	return render_template("basidirond.html")

@app.route("/wizard-sponge")
def Wizard_Sponge():
	return render_template("wizard-sponge.html")

@app.route("/arboreal-reaper")
def Arboreal_Reaper():
	return render_template("arboreal-reaper.html")

@app.route("/tendriculos")
def Tendriculos():
	return render_template("tendriculos.html")

@app.route("/scythe-tree")
def Scythe_Tree():
	return render_template("scythe-tree.html")

@app.route("/arboreal-regeant")
def Arboreal_Regeant():
	return render_template("arboreal-regeant.html")

@app.route("/counteflora")
def Counteflora():
	return render_template("counteflora.html")

@app.route("/dezullon")
def Dezullon():
	return render_template("dezullon.html")

@app.route("/drakauthix")
def Drakauthix():
	return render_template("drakauthix.html")

@app.route("/summon-plant-or-fungus")
def Summon_Plant_or_Fungus():
	return render_template("summon-plant-or-fungus.html")

@app.route("/lilend")
def Lilend():
	return render_template("lilend.html")

@app.route("/naunet")
def Naunet():
	return render_template("naunet.html")

@app.route("/nabasu-glutton-demon")
def Nabasu__Glutton_Demon_():
	return render_template("nabasu-glutton-demon.html")

@app.route("/einherjar")
def Einherjar():
	return render_template("einherjar.html")

@app.route("/garuda")
def Garuda():
	return render_template("garuda.html")

@app.route("/vrock")
def Vrock():
	return render_template("vrock.html")

@app.route("/summon-anarch")
def Summon_Anarch():
	return render_template("summon-anarch.html")

@app.route("/axiomite")
def Axiomite():
	return render_template("axiomite.html")

@app.route("/erinyes-fury-devil")
def Erinyes__Fury_Devil_():
	return render_template("erinyes-fury-devil.html")

@app.route("/legion-archon")
def Legion_Archon():
	return render_template("legion-archon.html")

@app.route("/sacristan")
def Sacristan():
	return render_template("sacristan.html")

@app.route("/zelekhut")
def Zelekhut():
	return render_template("zelekhut.html")

@app.route("/summon-axiom")
def Summon_Axiom():
	return render_template("summon-axiom.html")

@app.route("/balisse-confessor-angel")
def Balisse__Confessor_Angel_():
	return render_template("balisse-confessor-angel.html")

@app.route("/procyal")
def Procyal():
	return render_template("procyal.html")

@app.route("/summon-celestial")
def Summon_Celestial():
	return render_template("summon-celestial.html")

@app.route("/movanic-deva")
def Movanic_Deva():
	return render_template("movanic-deva.html")

@app.route("/monadic-deva")
def Monadic_Deva():
	return render_template("monadic-deva.html")

@app.route("/adult-black-dragon")
def Adult_Black_Dragon():
	return render_template("adult-black-dragon.html")

@app.route("/summon-dragon")
def Summon_Dragon():
	return render_template("summon-dragon.html")

@app.route("/destrachan")
def Destrachan():
	return render_template("destrachan.html")

@app.route("/rend-monster-ability")
def Rend__Monster_Ability_():
	return render_template("rend-monster-ability.html")

@app.route("/gug")
def Gug():
	return render_template("gug.html")

@app.route("/ofalth")
def Ofalth():
	return render_template("ofalth.html")

@app.route("/summon-entity")
def Summon_Entity():
	return render_template("summon-entity.html")

@app.route("/hellcat")
def Hellcat():
	return render_template("hellcat.html")

@app.route("/invidiak")
def Invidiak():
	return render_template("invidiak.html")

@app.route("/night-hag")
def Night_Hag():
	return render_template("night-hag.html")

@app.route("/leukodaemon-pestilence-demon")
def Leukodaemon__Pestilence_Demon_():
	return render_template("leukodaemon-pestilence-demon.html")

@app.route("/summon-fiend")
def Summon_Fiend():
	return render_template("summon-fiend.html")

@app.route("/catch")
def Catch():
	return render_template("catch.html")

@app.route("/hill-giant")
def Hill_Giant():
	return render_template("hill-giant.html")

@app.route("/ettin")
def Ettin():
	return render_template("ettin.html")

@app.route("/fire-giant")
def Fire_Giant():
	return render_template("fire-giant.html")

@app.route("/frost-giant")
def Frost_Giant():
	return render_template("frost-giant.html")

@app.route("/summon-giant")
def Summon_Giant():
	return render_template("summon-giant.html")

@app.route("/giant-mosquito")
def Giant_Mosquito():
	return render_template("giant-mosquito.html")

@app.route("/giant-dragonfly")
def Giant_Dragonfly():
	return render_template("giant-dragonfly.html")

@app.route("/giant-eagle")
def Giant_Eagle():
	return render_template("giant-eagle.html")

@app.route("/anklyosaurus")
def Anklyosaurus():
	return render_template("anklyosaurus.html")

@app.route("/stegosaurus")
def Stegosaurus():
	return render_template("stegosaurus.html")

@app.route("/triceratops")
def Triceratops():
	return render_template("triceratops.html")

@app.route("/tyrannosaurus")
def Tyrannosaurus():
	return render_template("tyrannosaurus.html")

@app.route("/dinosaur-form")
def Dinosaur_Form():
	return render_template("dinosaur-form.html")

@app.route("/engulf")
def Engulf():
	return render_template("engulf.html")

@app.route("/gelatinous-cube")
def Gelatinous_Cube():
	return render_template("gelatinous-cube.html")

@app.route("/blood-ooze")
def Blood_Ooze():
	return render_template("blood-ooze.html")

@app.route("/black-pudding")
def Black_Pudding():
	return render_template("black-pudding.html")

@app.route("/verdurous-ooze")
def Verdurous_Ooze():
	return render_template("verdurous-ooze.html")

@app.route("/ooze-form")
def Ooze_Form():
	return render_template("ooze-form.html")

@app.route("/chuul")
def Chuul():
	return render_template("chuul.html")

@app.route("/aerial-form")
def Aerial_Form():
	return render_template("aerial-form.html")

@app.route("/quoppopak")
def Quoppopak():
	return render_template("quoppopak.html")

@app.route("/gogiteth")
def Gogiteth():
	return render_template("gogiteth.html")

@app.route("/aberrant-form")
def Aberrant_Form():
	return render_template("aberrant-form.html")

@app.route("/nessian-warhound")
def Nessian_Warhound():
	return render_template("nessian-warhound.html")

@app.route("/hellwasp-swarm")
def Hellwasp_Swarm():
	return render_template("hellwasp-swarm.html")

@app.route("/kalavakus-slaver-demon")
def Kalavakus__Slaver_Demon_():
	return render_template("kalavakus-slaver-demon.html")

@app.route("/piscodaemon-venom-daemon")
def Piscodaemon__Venom_Daemon_():
	return render_template("piscodaemon-venom-daemon.html")

@app.route("/fiend-form")
def Fiend_Form():
	return render_template("fiend-form.html")

@app.route("/dragon-form")
def Dragon_Form():
	return render_template("dragon-form.html")

@app.route("/magma-scorpion")
def Magma_Scorpion():
	return render_template("magma-scorpion.html")

@app.route("/tidal-master")
def Tidal_Master():
	return render_template("tidal-master.html")

@app.route("/elemental-form")
def Elemental_Form():
	return render_template("elemental-form.html")

@app.route("/giant-flytrap")
def Giant_Flytrap():
	return render_template("giant-flytrap.html")

@app.route("/plant-form")
def Plant_Form():
	return render_template("plant-form.html")

@app.route("/nereid")
def Nereid():
	return render_template("nereid.html")

@app.route("/millindemalion")
def Millindemalion():
	return render_template("millindemalion.html")

@app.route("/fey-form")
def Fey_Form():
	return render_template("fey-form.html")

@app.route("/shield-archon")
def Shield_Archon():
	return render_template("shield-archon.html")

@app.route("/angel-form")
def Angel_Form():
	return render_template("angel-form.html")

@app.route("/purple-worm")
def Purple_Worm():
	return render_template("purple-worm.html")

@app.route("/sea-serpent")
def Sea_Serpent():
	return render_template("sea-serpent.html")

@app.route("/monstrosity-form")
def Monstrosity_Form():
	return render_template("monstrosity-form.html")

@app.route("/elven-absynthe")
def Elven_Absynthe():
	return render_template("elven-absynthe.html")

@app.route("/alcohol")
def Alcohol():
	return render_template("alcohol.html")

@app.route("/qat")
def Qat():
	return render_template("qat.html")

@app.route("/bloodeye-coffee")
def Bloodeye_Coffee():
	return render_template("bloodeye-coffee.html")

@app.route("/flayleaf")
def Flayleaf():
	return render_template("flayleaf.html")

@app.route("/refined-pesh")
def Refined_Pesh():
	return render_template("refined-pesh.html")

@app.route("/grit")
def Grit():
	return render_template("grit.html")

@app.route("/groina")
def Groina():
	return render_template("groina.html")

@app.route("/blood-sap")
def Blood_Sap():
	return render_template("blood-sap.html")

@app.route("/shiver")
def Shiver():
	return render_template("shiver.html")

@app.route("/dreamtime-tea")
def Dreamtime_Tea():
	return render_template("dreamtime-tea.html")

@app.route("/zerk")
def Zerk():
	return render_template("zerk.html")

@app.route("/diluted-hype")
def Diluted_Hype():
	return render_template("diluted-hype.html")

@app.route("/cytillesh")
def Cytillesh():
	return render_template("cytillesh.html")

@app.route("/demon-dust")
def Demon_Dust():
	return render_template("demon-dust.html")

@app.route("/succubus-kiss")
def Succubus_Kiss():
	return render_template("succubus-kiss.html")

@app.route("/scour")
def Scour():
	return render_template("scour.html")

@app.route("/hype")
def Hype():
	return render_template("hype.html")

@app.route("/plasma-hype")
def Plasma_Hype():
	return render_template("plasma-hype.html")

@app.route("/popdust")
def Popdust():
	return render_template("popdust.html")

@app.route("/tindertwig")
def Tindertwig():
	return render_template("tindertwig.html")

@app.route("/snake-oil")
def Snake_Oil():
	return render_template("snake-oil.html")

@app.route("/blindpepper-tube")
def Blindpepper_Tube():
	return render_template("blindpepper-tube.html")

@app.route("/bookthief-brew")
def Bookthief_Brew():
	return render_template("bookthief-brew.html")

@app.route("/forensic-dye")
def Forensic_Dye():
	return render_template("forensic-dye.html")

@app.route("/ghost-ink")
def Ghost_Ink():
	return render_template("ghost-ink.html")

@app.route("/sunrod")
def Sunrod():
	return render_template("sunrod.html")

@app.route("/lovers-ink")
def Lovers_Ink():
	return render_template("lovers-ink.html")

@app.route("/origin-unguent")
def Origin_Unguent():
	return render_template("origin-unguent.html")

@app.route("/silvensheen")
def Silvensheen():
	return render_template("silvensheen.html")

@app.route("/impossible-cake")
def Impossible_Cake():
	return render_template("impossible-cake.html")

@app.route("/cold-iron-blanch")
def Cold_Iron_Blanch():
	return render_template("cold-iron-blanch.html")

@app.route("/quickpatch-glue")
def Quickpatch_Glue():
	return render_template("quickpatch-glue.html")

@app.route("/swamp-lily-quilt")
def Swamp_Lily_Quilt():
	return render_template("swamp-lily-quilt.html")

@app.route("/aurifying-salts")
def Aurifying_Salts():
	return render_template("aurifying-salts.html")

@app.route("/timeless-salts")
def Timeless_Salts():
	return render_template("timeless-salts.html")

@app.route("/fungal-walk-musk")
def Fungal_Walk_Musk():
	return render_template("fungal-walk-musk.html")

@app.route("/universal-solvent")
def Universal_Solvent():
	return render_template("universal-solvent.html")

@app.route("/smokestick")
def Smokestick():
	return render_template("smokestick.html")

@app.route("/dragons-blood-pudding")
def Dragons_Blood_Pudding():
	return render_template("dragons-blood-pudding.html")

@app.route("/bloodhound-mask")
def Bloodhound_Mask():
	return render_template("bloodhound-mask.html")

@app.route("/metalmist-sphere")
def Metalmist_Sphere():
	return render_template("metalmist-sphere.html")

@app.route("/skinstich-salve")
def Skinstich_Salve():
	return render_template("skinstich-salve.html")

@app.route("/sovereign-glue")
def Sovereign_Glue():
	return render_template("sovereign-glue.html")

@app.route("/cold-comfort")
def Cold_Comfort():
	return render_template("cold-comfort.html")

@app.route("/vermin-repellent-agent")
def Vermin_Repellent_Agent():
	return render_template("vermin-repellent-agent.html")

@app.route("/brewers-regret")
def Brewers_Regret():
	return render_template("brewers-regret.html")

@app.route("/green-gut")
def Green_Gut():
	return render_template("green-gut.html")

@app.route("/false-death")
def False_Death():
	return render_template("false-death.html")

@app.route("/looters-lethargy")
def Looters_Lethargy():
	return render_template("looters-lethargy.html")

@app.route("/black-adder-venom")
def Black_Adder_Venom():
	return render_template("black-adder-venom.html")

@app.route("/black-smear-poison")
def Black_Smear_Poison():
	return render_template("black-smear-poison.html")

@app.route("/spear-frog-poison")
def Spear_Frog_Poison():
	return render_template("spear-frog-poison.html")

@app.route("/giant-centipede-venom")
def Giant_Centipede_Venom():
	return render_template("giant-centipede-venom.html")

@app.route("/toad-tears")
def Toad_Tears():
	return render_template("toad-tears.html")

@app.route("/yellow-musk-vial")
def Yellow_Musk_Vial():
	return render_template("yellow-musk-vial.html")

@app.route("/violet-venom")
def Violet_Venom():
	return render_template("violet-venom.html")

@app.route("/beladonna")
def Beladonna():
	return render_template("beladonna.html")

@app.route("/arsenic")
def Arsenic():
	return render_template("arsenic.html")

@app.route("/leaden-leg")
def Leaden_Leg():
	return render_template("leaden-leg.html")

@app.route("/graveroot")
def Graveroot():
	return render_template("graveroot.html")

@app.route("/blue-dragonfly-poison")
def Blue_Dragonfly_Poison():
	return render_template("blue-dragonfly-poison.html")

@app.route("/hunting-spider-venom")
def Hunting_Spider_Venom():
	return render_template("hunting-spider-venom.html")

@app.route("/giant-scorpion-venom")
def Giant_Scorpion_Venom():
	return render_template("giant-scorpion-venom.html")

@app.route("/forgetful-ink")
def Forgetful_Ink():
	return render_template("forgetful-ink.html")

@app.route("/isolation-draught")
def Isolation_Draught():
	return render_template("isolation-draught.html")

@app.route("/sloughing-toxin")
def Sloughing_Toxin():
	return render_template("sloughing-toxin.html")

@app.route("/addlebrain")
def Addlebrain():
	return render_template("addlebrain.html")

@app.route("/malyass-root-paste")
def Malyass_Root_Paste():
	return render_template("malyass-root-paste.html")

@app.route("/knockout-dram")
def Knockout_Dram():
	return render_template("knockout-dram.html")

@app.route("/lich-dust")
def Lich_Dust():
	return render_template("lich-dust.html")

@app.route("/abysium-powder")
def Abysium_Powder():
	return render_template("abysium-powder.html")

@app.route("/wyvern-poison")
def Wyvern_Poison():
	return render_template("wyvern-poison.html")

@app.route("/wolfsbane")
def Wolfsbane():
	return render_template("wolfsbane.html")

@app.route("/fearweed")
def Fearweed():
	return render_template("fearweed.html")

@app.route("/honeyscent")
def Honeyscent():
	return render_template("honeyscent.html")

@app.route("/blightburn-resin")
def Blightburn_Resin():
	return render_template("blightburn-resin.html")

@app.route("/hunger-oil")
def Hunger_Oil():
	return render_template("hunger-oil.html")

@app.route("/mage-bane")
def Mage_Bane():
	return render_template("mage-bane.html")

@app.route("/slumber-wine")
def Slumber_Wine():
	return render_template("slumber-wine.html")

@app.route("/spell-eating-pitch")
def Spell_Eating_Pitch():
	return render_template("spell-eating-pitch.html")

@app.route("/deathcap-powder")
def Deathcap_Powder():
	return render_template("deathcap-powder.html")

@app.route("/spectral-nightshade")
def Spectral_Nightshade():
	return render_template("spectral-nightshade.html")

@app.route("/gorgons-breath")
def Gorgons_Breath():
	return render_template("gorgons-breath.html")

@app.route("/daylight-vapor")
def Daylight_Vapor():
	return render_template("daylight-vapor.html")

@app.route("/death-knell-powder")
def Death_Knell_Powder():
	return render_template("death-knell-powder.html")

@app.route("/liars-demise")
def Liars_Demise():
	return render_template("liars-demise.html")

@app.route("/mindfog-mist")
def Mindfog_Mist():
	return render_template("mindfog-mist.html")

@app.route("/lifeblight-residue")
def Lifeblight_Residue():
	return render_template("lifeblight-residue.html")

@app.route("/weeping-midnight")
def Weeping_Midnight():
	return render_template("weeping-midnight.html")

@app.route("/cerulean-scourge")
def Cerulean_Scourge():
	return render_template("cerulean-scourge.html")

@app.route("/dragon-bile")
def Dragon_Bile():
	return render_template("dragon-bile.html")

@app.route("/brimstone-fumes")
def Brimstone_Fumes():
	return render_template("brimstone-fumes.html")

@app.route("/frenzy-oil")
def Frenzy_Oil():
	return render_template("frenzy-oil.html")

@app.route("/repulsion-resin")
def Repulsion_Resin():
	return render_template("repulsion-resin.html")

@app.route("/hemlock")
def Hemlock():
	return render_template("hemlock.html")

@app.route("/kings-sleep")
def Kings_Sleep():
	return render_template("kings-sleep.html")

@app.route("/black-lotus-extract")
def Black_Lotus_Extract():
	return render_template("black-lotus-extract.html")

@app.route("/oblivion-essence")
def Oblivion_Essence():
	return render_template("oblivion-essence.html")

@app.route("/tears-of-death")
def Tears_of_Death():
	return render_template("tears-of-death.html")

@app.route("/addiction")
def Addiction():
	return render_template("addiction.html")

@app.route("/addiction-suppressant")
def Addiction_Suppressant():
	return render_template("addiction-suppressant.html")

@app.route("/antidote")
def Antidote():
	return render_template("antidote.html")

@app.route("/antiplague")
def Antiplague():
	return render_template("antiplague.html")

@app.route("/cheetahs-elixir")
def Cheetahs_Elixir():
	return render_template("cheetahs-elixir.html")

@app.route("/lastwall-soup")
def Lastwall_Soup():
	return render_template("lastwall-soup.html")

@app.route("/leapers-elixir")
def Leapers_Elixir():
	return render_template("leapers-elixir.html")

@app.route("/bestial-mutagen")
def Bestial_Mutagen():
	return render_template("bestial-mutagen.html")

@app.route("/cognitive-mutagen")
def Cognitive_Mutagen():
	return render_template("cognitive-mutagen.html")

@app.route("/drakeheart-mutagen")
def Drakeheart_Mutagen():
	return render_template("drakeheart-mutagen.html")

@app.route("/eagle-eye-elixir")
def Eagle_Eye_Elixir():
	return render_template("eagle-eye-elixir.html")

@app.route("/juggernaut-mutagen")
def Juggernaut_Mutagen():
	return render_template("juggernaut-mutagen.html")

@app.route("/quicksilver-mutagen")
def Quicksilver_Mutagen():
	return render_template("quicksilver-mutagen.html")

@app.route("/energy-mutagen")
def Energy_Mutagen():
	return render_template("energy-mutagen.html")

@app.route("/serene-mutagen")
def Serene_Mutagen():
	return render_template("serene-mutagen.html")

@app.route("/silvertongue-mutagen")
def Silvertongue_Mutagen():
	return render_template("silvertongue-mutagen.html")

@app.route("/skeptics-elixir")
def Skeptics_Elixir():
	return render_template("skeptics-elixir.html")

@app.route("/sinew-shock-serum")
def Sinew_Shock_Serum():
	return render_template("sinew-shock-serum.html")

@app.route("/darkvision-elixir")
def Darkvision_Elixir():
	return render_template("darkvision-elixir.html")

@app.route("/infiltrators-elixir")
def Infiltrators_Elixir():
	return render_template("infiltrators-elixir.html")

@app.route("/focus-cathartic")
def Focus_Cathartic():
	return render_template("focus-cathartic.html")

@app.route("/bravos-brew")
def Bravos_Brew():
	return render_template("bravos-brew.html")

@app.route("/cats-eye-elixir")
def Cats_Eye_Elixir():
	return render_template("cats-eye-elixir.html")

@app.route("/olfactory-obfuscator")
def Olfactory_Obfuscator():
	return render_template("olfactory-obfuscator.html")

@app.route("/spiderfoot-brew")
def Spiderfoot_Brew():
	return render_template("spiderfoot-brew.html")

@app.route("/stonefist-elixir")
def Stonefist_Elixir():
	return render_template("stonefist-elixir.html")

@app.route("/bombers-eye-elixir")
def Bombers_Eye_Elixir():
	return render_template("bombers-eye-elixir.html")

@app.route("/salamander-elixir")
def Salamander_Elixir():
	return render_template("salamander-elixir.html")

@app.route("/winter-wolf-elixir")
def Winter_Wolf_Elixir():
	return render_template("winter-wolf-elixir.html")

@app.route("/mistform-elixir")
def Mistform_Elixir():
	return render_template("mistform-elixir.html")

@app.route("/sea-touch-elixir")
def Sea_Touch_Elixir():
	return render_template("sea-touch-elixir.html")

@app.route("/stone-body-mutagen")
def Stone_Body_Mutagen():
	return render_template("stone-body-mutagen.html")

@app.route("/malleable-mixture")
def Malleable_Mixture():
	return render_template("malleable-mixture.html")

@app.route("/mnemonic-acid")
def Mnemonic_Acid():
	return render_template("mnemonic-acid.html")

@app.route("/acid-flask")
def Acid_Flask():
	return render_template("acid-flask.html")

@app.route("/blight-bomb")
def Blight_Bomb():
	return render_template("blight-bomb.html")

@app.route("/dread-ampoule")
def Dread_Ampoule():
	return render_template("dread-ampoule.html")

@app.route("/ghost-charge")
def Ghost_Charge():
	return render_template("ghost-charge.html")

@app.route("/necrotic-bomb")
def Necrotic_Bomb():
	return render_template("necrotic-bomb.html")

@app.route("/peshpine-grenade")
def Peshpine_Grenade():
	return render_template("peshpine-grenade.html")

@app.route("/redpitch-bomb")
def Redpitch_Bomb():
	return render_template("redpitch-bomb.html")

@app.route("/tanglefoot-bag")
def Tanglefoot_Bag():
	return render_template("tanglefoot-bag.html")

@app.route("/thunderstone")
def Thunderstone():
	return render_template("thunderstone.html")

@app.route("/alignment-ampoule")
def Alignment_Ampoule():
	return render_template("alignment-ampoule.html")

@app.route("/junk-bomb")
def Junk_Bomb():
	return render_template("junk-bomb.html")

@app.route("/pressure-bomb")
def Pressure_Bomb():
	return render_template("pressure-bomb.html")

@app.route("/sulfur-bomb")
def Sulfur_Bomb():
	return render_template("sulfur-bomb.html")

@app.route("/vexing-vapor")
def Vexing_Vapor():
	return render_template("vexing-vapor.html")

@app.route("/dwarven-daisy")
def Dwarven_Daisy():
	return render_template("dwarven-daisy.html")

@app.route("/blindpepper-bomb")
def Blindpepper_Bomb():
	return render_template("blindpepper-bomb.html")

@app.route("/frost-vial")
def Frost_Vial():
	return render_template("frost-vial.html")

@app.route("/base-armor-rules")
def Base_Armor_Rules():
	return render_template("base-armor-rules.html")

@app.route("/padded-armor")
def Padded_Armor():
	return render_template("padded-armor.html")

@app.route("/comfort")
def Comfort():
	return render_template("comfort.html")

@app.route("/leather-armor")
def Leather_Armor():
	return render_template("leather-armor.html")

@app.route("/studded-leather")
def Studded_Leather():
	return render_template("studded-leather.html")

@app.route("/flexible-9314415")
def Flexible():
	return render_template("flexible-9314415.html")

@app.route("/noisy-8581790")
def Noisy():
	return render_template("noisy-8581790.html")

@app.route("/chain-shirt")
def Chain_Shirt():
	return render_template("chain-shirt.html")

@app.route("/hide-armor")
def Hide_Armor():
	return render_template("hide-armor.html")

@app.route("/scale-mail")
def Scale_Mail():
	return render_template("scale-mail.html")

@app.route("/chain-mail")
def Chain_Mail():
	return render_template("chain-mail.html")

@app.route("/breastplate")
def Breastplate():
	return render_template("breastplate.html")

@app.route("/splint-mail")
def Splint_Mail():
	return render_template("splint-mail.html")

@app.route("/half-plate")
def Half_Plate():
	return render_template("half-plate.html")

@app.route("/bulwark-6066934")
def Bulwark():
	return render_template("bulwark-6066934.html")

@app.route("/full-plate")
def Full_Plate():
	return render_template("full-plate.html")

@app.route("/unarmed-strike")
def Unarmed_Strike():
	return render_template("unarmed-strike.html")

@app.route("/battle-lute")
def Battle_Lute():
	return render_template("battle-lute.html")

@app.route("/juggling-club")
def Juggling_Club():
	return render_template("juggling-club.html")

@app.route("/dagger")
def Dagger():
	return render_template("dagger.html")

@app.route("/club")
def Club():
	return render_template("club.html")

@app.route("/clan-dagger-3460910")
def Clan_Dagger():
	return render_template("clan-dagger-3460910.html")

@app.route("/katar")
def Katar():
	return render_template("katar.html")

@app.route("/knuckle-duster")
def Knuckle_Duster():
	return render_template("knuckle-duster.html")

@app.route("/longspear")
def Longspear():
	return render_template("longspear.html")

@app.route("/light-mace")
def Light_Mace():
	return render_template("light-mace.html")

@app.route("/mace")
def Mace():
	return render_template("mace.html")

@app.route("/morningstar")
def Morningstar():
	return render_template("morningstar.html")

@app.route("/sickle")
def Sickle():
	return render_template("sickle.html")

@app.route("/spear")
def Spear():
	return render_template("spear.html")

@app.route("/spiked-gauntlet")
def Spiked_Gauntlet():
	return render_template("spiked-gauntlet.html")

@app.route("/throwing-knife")
def Throwing_Knife():
	return render_template("throwing-knife.html")

@app.route("/thundermace")
def Thundermace():
	return render_template("thundermace.html")

@app.route("/tri-bladed-katar")
def Tri_Bladed_Katar():
	return render_template("tri-bladed-katar.html")

@app.route("/asp-coil")
def Asp_Coil():
	return render_template("asp-coil.html")

@app.route("/staff")
def Staff():
	return render_template("staff.html")

@app.route("/bastard-sword")
def Bastard_Sword():
	return render_template("bastard-sword.html")

@app.route("/battle-axe")
def Battle_Axe():
	return render_template("battle-axe.html")

@app.route("/bladed-scarf")
def Bladed_Scarf():
	return render_template("bladed-scarf.html")

@app.route("/bo-staff")
def Bo_Staff():
	return render_template("bo-staff.html")

@app.route("/boarding-axe")
def Boarding_Axe():
	return render_template("boarding-axe.html")

@app.route("/boarding-pike")
def Boarding_Pike():
	return render_template("boarding-pike.html")

@app.route("/buugeng")
def Buugeng():
	return render_template("buugeng.html")

@app.route("/claw-blade")
def Claw_Blade():
	return render_template("claw-blade.html")

@app.route("/combat-grapnel")
def Combat_Grapnel():
	return render_template("combat-grapnel.html")

@app.route("/dueling-spear")
def Dueling_Spear():
	return render_template("dueling-spear.html")

@app.route("/elven-branched-spear")
def Elven_Branched_Spear():
	return render_template("elven-branched-spear.html")

@app.route("/elven-curved-blade")
def Elven_Curved_Blade():
	return render_template("elven-curved-blade.html")

@app.route("/exquisite-sword-cane")
def Exquisite_Sword_Cane():
	return render_template("exquisite-sword-cane.html")

@app.route("/exquisite-sword-cane-sheath")
def Exquisite_Sword_Cane_Sheath():
	return render_template("exquisite-sword-cane-sheath.html")

@app.route("/falchion")
def Falchion():
	return render_template("falchion.html")

@app.route("/fangwire")
def Fangwire():
	return render_template("fangwire.html")

@app.route("/fauchard")
def Fauchard():
	return render_template("fauchard.html")

@app.route("/fighting-fan")
def Fighting_Fan():
	return render_template("fighting-fan.html")

@app.route("/fighting-stick")
def Fighting_Stick():
	return render_template("fighting-stick.html")

@app.route("/filchers-fork")
def Filchers_Fork():
	return render_template("filchers-fork.html")

@app.route("/flail")
def Flail():
	return render_template("flail.html")

@app.route("/gaff")
def Gaff():
	return render_template("gaff.html")

@app.route("/glaive")
def Glaive():
	return render_template("glaive.html")

@app.route("/gnome-hooked-hammer")
def Gnome_Hooked_Hammer():
	return render_template("gnome-hooked-hammer.html")

@app.route("/greataxe")
def Greataxe():
	return render_template("greataxe.html")

@app.route("/greatclub")
def Greatclub():
	return render_template("greatclub.html")

@app.route("/greatpick")
def Greatpick():
	return render_template("greatpick.html")

@app.route("/greatsword")
def Greatsword():
	return render_template("greatsword.html")

@app.route("/griffon-cane")
def Griffon_Cane():
	return render_template("griffon-cane.html")

@app.route("/guisarme")
def Guisarme():
	return render_template("guisarme.html")

@app.route("/halberd")
def Halberd():
	return render_template("halberd.html")

@app.route("/adze")
def Adze():
	return render_template("adze.html")

@app.route("/hand-adze")
def Hand_Adze():
	return render_template("hand-adze.html")

@app.route("/injection-spear")
def Injection_Spear():
	return render_template("injection-spear.html")

@app.route("/kama")
def Kama():
	return render_template("kama.html")

@app.route("/katana")
def Katana():
	return render_template("katana.html")

@app.route("/khakkara")
def Khakkara():
	return render_template("khakkara.html")

@app.route("/hatchet")
def Hatchet():
	return render_template("hatchet.html")

@app.route("/khopesh")
def Khopesh():
	return render_template("khopesh.html")

@app.route("/kukri")
def Kukri():
	return render_template("kukri.html")

@app.route("/kusarigama")
def Kusarigama():
	return render_template("kusarigama.html")

@app.route("/lance")
def Lance():
	return render_template("lance.html")

@app.route("/leiomana")
def Leiomana():
	return render_template("leiomana.html")

@app.route("/light-hammer")
def Light_Hammer():
	return render_template("light-hammer.html")

@app.route("/lion-scythe")
def Lion_Scythe():
	return render_template("lion-scythe.html")

@app.route("/longsword")
def Longsword():
	return render_template("longsword.html")

@app.route("/machete")
def Machete():
	return render_template("machete.html")

@app.route("/main-gauche")
def Main_Gauche():
	return render_template("main-gauche.html")

@app.route("/mambele")
def Mambele():
	return render_template("mambele.html")

@app.route("/maul")
def Maul():
	return render_template("maul.html")

@app.route("/meteor-hammer")
def Meteor_Hammer():
	return render_template("meteor-hammer.html")

@app.route("/monkeys-fist")
def Monkeys_Fist():
	return render_template("monkeys-fist.html")

@app.route("/naginata")
def Naginata():
	return render_template("naginata.html")

@app.route("/nine-ring-sword")
def Nine_Ring_Sword():
	return render_template("nine-ring-sword.html")

@app.route("/nunchuku")
def Nunchuku():
	return render_template("nunchuku.html")

@app.route("/ogre-hook")
def Ogre_Hook():
	return render_template("ogre-hook.html")

@app.route("/orc-knuckle-dagger")
def Orc_Knuckle_Dagger():
	return render_template("orc-knuckle-dagger.html")

@app.route("/pick")
def Pick():
	return render_template("pick.html")

@app.route("/piranha-kiss")
def Piranha_Kiss():
	return render_template("piranha-kiss.html")

@app.route("/polytool")
def Polytool():
	return render_template("polytool.html")

@app.route("/probing-cane")
def Probing_Cane():
	return render_template("probing-cane.html")

@app.route("/ranseur")
def Ranseur():
	return render_template("ranseur.html")

@app.route("/rapier")
def Rapier():
	return render_template("rapier.html")

@app.route("/rungu")
def Rungu():
	return render_template("rungu.html")

@app.route("/sai")
def Sai():
	return render_template("sai.html")

@app.route("/sap")
def Sap():
	return render_template("sap.html")

@app.route("/scimitar")
def Scimitar():
	return render_template("scimitar.html")

@app.route("/scorpion-whip")
def Scorpion_Whip():
	return render_template("scorpion-whip.html")

@app.route("/scourge")
def Scourge():
	return render_template("scourge.html")

@app.route("/scythe")
def Scythe():
	return render_template("scythe.html")

@app.route("/shauth-blade")
def Shauth_Blade():
	return render_template("shauth-blade.html")

@app.route("/shield-bash")
def Shield_Bash():
	return render_template("shield-bash.html")

@app.route("/shield-boss")
def Shield_Boss():
	return render_template("shield-boss.html")

@app.route("/shield-spikes")
def Shield_Spikes():
	return render_template("shield-spikes.html")

@app.route("/shortsword")
def Shortsword():
	return render_template("shortsword.html")

@app.route("/spiked-chain")
def Spiked_Chain():
	return render_template("spiked-chain.html")

@app.route("/starknife")
def Starknife():
	return render_template("starknife.html")

@app.route("/sword-cane")
def Sword_Cane():
	return render_template("sword-cane.html")

@app.route("/tekko-kagi")
def Tekko_Kagi():
	return render_template("tekko-kagi.html")

@app.route("/temple-sword")
def Temple_Sword():
	return render_template("temple-sword.html")

@app.route("/tengu-gale-blade")
def Tengu_Gale_Blade():
	return render_template("tengu-gale-blade.html")

@app.route("/tonfa")
def Tonfa():
	return render_template("tonfa.html")

@app.route("/trident")
def Trident():
	return render_template("trident.html")

@app.route("/umbrella-injector")
def Umbrella_Injector():
	return render_template("umbrella-injector.html")

@app.route("/urumi")
def Urumi():
	return render_template("urumi.html")

@app.route("/wakizashi")
def Wakizashi():
	return render_template("wakizashi.html")

@app.route("/war-flail")
def War_Flail():
	return render_template("war-flail.html")

@app.route("/war-razor")
def War_Razor():
	return render_template("war-razor.html")

@app.route("/warhammer")
def Warhammer():
	return render_template("warhammer.html")

@app.route("/whip")
def Whip():
	return render_template("whip.html")

@app.route("/wish-blade")
def Wish_Blade():
	return render_template("wish-blade.html")

@app.route("/wish-knife")
def Wish_Knife():
	return render_template("wish-knife.html")

@app.route("/aklys")
def Aklys():
	return render_template("aklys.html")

@app.route("/aldori-dueling-sword")
def Aldori_Dueling_Sword():
	return render_template("aldori-dueling-sword.html")

@app.route("/bladed-diabolo")
def Bladed_Diabolo():
	return render_template("bladed-diabolo.html")

@app.route("/bladed-hoop")
def Bladed_Hoop():
	return render_template("bladed-hoop.html")

@app.route("/butchering-axe")
def Butchering_Axe():
	return render_template("butchering-axe.html")

@app.route("/butterfly-sword")
def Butterfly_Sword():
	return render_template("butterfly-sword.html")

@app.route("/dwarven-war-axe")
def Dwarven_War_Axe():
	return render_template("dwarven-war-axe.html")

@app.route("/hook-sword")
def Hook_Sword():
	return render_template("hook-sword.html")

@app.route("/karambit")
def Karambit():
	return render_template("karambit.html")

@app.route("/orc-necksplitter")
def Orc_Necksplitter():
	return render_template("orc-necksplitter.html")

@app.route("/rhoka-sword")
def Rhoka_Sword():
	return render_template("rhoka-sword.html")

@app.route("/sawtooth-saber")
def Sawtooth_Saber():
	return render_template("sawtooth-saber.html")

@app.route("/shauth-lash")
def Shauth_Lash():
	return render_template("shauth-lash.html")

@app.route("/sickle-saber")
def Sickle_Saber():
	return render_template("sickle-saber.html")

@app.route("/spiral-rapier")
def Spiral_Rapier():
	return render_template("spiral-rapier.html")

@app.route("/switchscythe")
def Switchscythe():
	return render_template("switchscythe.html")

@app.route("/tamchal-chakram")
def Tamchal_Chakram():
	return render_template("tamchal-chakram.html")

@app.route("/tricky-pick")
def Tricky_Pick():
	return render_template("tricky-pick.html")

@app.route("/whip-claw")
def Whip_Claw():
	return render_template("whip-claw.html")

@app.route("/wind-and-fire-wheel")
def Wind_and_Fire_Wheel():
	return render_template("wind-and-fire-wheel.html")

@app.route("/alchemical-crossbow")
def Alchemical_Crossbow():
	return render_template("alchemical-crossbow.html")

@app.route("/arrows")
def Arrows():
	return render_template("arrows.html")

@app.route("/blowgun-darts")
def Blowgun_Darts():
	return render_template("blowgun-darts.html")

@app.route("/bolts")
def Bolts():
	return render_template("bolts.html")

@app.route("/sling-bullets")
def Sling_Bullets():
	return render_template("sling-bullets.html")

@app.route("/blowgun")
def Blowgun():
	return render_template("blowgun.html")

@app.route("/heavy-crossbow")
def Heavy_Crossbow():
	return render_template("heavy-crossbow.html")

@app.route("/hand-crossbow")
def Hand_Crossbow():
	return render_template("hand-crossbow.html")

@app.route("/dart")
def Dart():
	return render_template("dart.html")

@app.route("/crossbow")
def Crossbow():
	return render_template("crossbow.html")

@app.route("/javelin")
def Javelin():
	return render_template("javelin.html")

@app.route("/sling")
def Sling():
	return render_template("sling.html")

@app.route("/alchemical-bomb")
def Alchemical_Bomb():
	return render_template("alchemical-bomb.html")

@app.route("/bola")
def Bola():
	return render_template("bola.html")

@app.route("/chakram")
def Chakram():
	return render_template("chakram.html")

@app.route("/composite-longbow")
def Composite_Longbow():
	return render_template("composite-longbow.html")

@app.route("/composite-shortbow")
def Composite_Shortbow():
	return render_template("composite-shortbow.html")

@app.route("/halfling-slingstaff")
def Halfling_Slingstaff():
	return render_template("halfling-slingstaff.html")

@app.route("/shortbow")
def Shortbow():
	return render_template("shortbow.html")

@app.route("/shuriken")
def Shuriken():
	return render_template("shuriken.html")

@app.route("/sun-shot")
def Sun_Shot():
	return render_template("sun-shot.html")

@app.route("/thunder-sling")
def Thunder_Sling():
	return render_template("thunder-sling.html")

@app.route("/wooden-taws")
def Wooden_Taws():
	return render_template("wooden-taws.html")

@app.route("/daikyu")
def Daikyu():
	return render_template("daikyu.html")

@app.route("/hongali-hornbow")
def Hongali_Hornbow():
	return render_template("hongali-hornbow.html")

@app.route("/taw-launcher")
def Taw_Launcher():
	return render_template("taw-launcher.html")

@app.route("/resonant")
def Resonant():
	return render_template("resonant.html")

@app.route("/free-hand-4441605")
def Free_Hand():
	return render_template("free-hand-4441605.html")

@app.route("/holly-and-mistletoe")
def Holly_and_Mistletoe():
	return render_template("holly-and-mistletoe.html")

@app.route("/puzzle-box")
def Puzzle_Box():
	return render_template("puzzle-box.html")

@app.route("/candle")
def Candle():
	return render_template("candle.html")

@app.route("/chalk")
def Chalk():
	return render_template("chalk.html")

@app.route("/clay")
def Clay():
	return render_template("clay.html")

@app.route("/oil")
def Oil():
	return render_template("oil.html")

@app.route("/sack")
def Sack():
	return render_template("sack.html")

@app.route("/ten-foot-pole")
def Ten_Foot_Pole():
	return render_template("ten-foot-pole.html")

@app.route("/torch")
def Torch():
	return render_template("torch.html")

@app.route("/bedroll")
def Bedroll():
	return render_template("bedroll.html")

@app.route("/soap")
def Soap():
	return render_template("soap.html")

@app.route("/ball")
def Ball():
	return render_template("ball.html")

@app.route("/ladder")
def Ladder():
	return render_template("ladder.html")

@app.route("/kite")
def Kite():
	return render_template("kite.html")

@app.route("/bandalore")
def Bandalore():
	return render_template("bandalore.html")

@app.route("/flint-and-steel")
def Flint_and_Steel():
	return render_template("flint-and-steel.html")

@app.route("/water-purifier")
def Water_Purifier():
	return render_template("water-purifier.html")

@app.route("/mask")
def Mask():
	return render_template("mask.html")

@app.route("/waterskin")
def Waterskin():
	return render_template("waterskin.html")

@app.route("/signal-whistle")
def Signal_Whistle():
	return render_template("signal-whistle.html")

@app.route("/air-bladder")
def Air_Bladder():
	return render_template("air-bladder.html")

@app.route("/backpack")
def Backpack():
	return render_template("backpack.html")

@app.route("/blocks")
def Blocks():
	return render_template("blocks.html")

@app.route("/clothing")
def Clothing():
	return render_template("clothing.html")

@app.route("/disguise-kit")
def Disguise_Kit():
	return render_template("disguise-kit.html")

@app.route("/doll")
def Doll():
	return render_template("doll.html")

@app.route("/grappling-hook")
def Grappling_Hook():
	return render_template("grappling-hook.html")

@app.route("/hammer")
def Hammer():
	return render_template("hammer.html")

@app.route("/powder")
def Powder():
	return render_template("powder.html")

@app.route("/religious-symbol")
def Religious_Symbol():
	return render_template("religious-symbol.html")

@app.route("/shield-sconce")
def Shield_Sconce():
	return render_template("shield-sconce.html")

@app.route("/writing-set")
def Writing_Set():
	return render_template("writing-set.html")

@app.route("/grappling-arrow")
def Grappling_Arrow():
	return render_template("grappling-arrow.html")

@app.route("/lock-4874732")
def Lock():
	return render_template("lock-4874732.html")

@app.route("/marbles")
def Marbles():
	return render_template("marbles.html")

@app.route("/merchant-scale")
def Merchant_Scale():
	return render_template("merchant-scale.html")

@app.route("/saddlebags")
def Saddlebags():
	return render_template("saddlebags.html")

@app.route("/caltrops")
def Caltrops():
	return render_template("caltrops.html")

@app.route("/manacles")
def Manacles():
	return render_template("manacles.html")

@app.route("/thieves-tools")
def Thieves_Tools():
	return render_template("thieves-tools.html")

@app.route("/rations")
def Rations():
	return render_template("rations.html")

@app.route("/tool")
def Tool():
	return render_template("tool.html")

@app.route("/climbing-kit")
def Climbing_Kit():
	return render_template("climbing-kit.html")

@app.route("/crowbar")
def Crowbar():
	return render_template("crowbar.html")

@app.route("/dueling-cape")
def Dueling_Cape():
	return render_template("dueling-cape.html")

@app.route("/games")
def Games():
	return render_template("games.html")

@app.route("/material-component-pouch")
def Material_Component_Pouch():
	return render_template("material-component-pouch.html")

@app.route("/parrying-scabbard")
def Parrying_Scabbard():
	return render_template("parrying-scabbard.html")

@app.route("/playing-cards")
def Playing_Cards():
	return render_template("playing-cards.html")

@app.route("/rope")
def Rope():
	return render_template("rope.html")

@app.route("/tear-away-clothing")
def Tear_Away_Clothing():
	return render_template("tear-away-clothing.html")

@app.route("/windup-toy-carriage")
def Windup_Toy_Carriage():
	return render_template("windup-toy-carriage.html")

@app.route("/wheelbarrow")
def Wheelbarrow():
	return render_template("wheelbarrow.html")

@app.route("/chest")
def Chest():
	return render_template("chest.html")

@app.route("/lantern")
def Lantern():
	return render_template("lantern.html")

@app.route("/fishing-tackle")
def Fishing_Tackle():
	return render_template("fishing-tackle.html")

@app.route("/musical-instrument")
def Musical_Instrument():
	return render_template("musical-instrument.html")

@app.route("/tent")
def Tent():
	return render_template("tent.html")

@app.route("/brass-ear")
def Brass_Ear():
	return render_template("brass-ear.html")

@app.route("/compass")
def Compass():
	return render_template("compass.html")

@app.route("/cookware")
def Cookware():
	return render_template("cookware.html")

@app.route("/depth-gauge")
def Depth_Gauge():
	return render_template("depth-gauge.html")

@app.route("/mirror")
def Mirror():
	return render_template("mirror.html")

@app.route("/net")
def Net():
	return render_template("net.html")

@app.route("/paint-set")
def Paint_Set():
	return render_template("paint-set.html")

@app.route("/religious-text")
def Religious_Text():
	return render_template("religious-text.html")

@app.route("/rubbing-set")
def Rubbing_Set():
	return render_template("rubbing-set.html")

@app.route("/wax-key-blank")
def Wax_Key_Blank():
	return render_template("wax-key-blank.html")

@app.route("/adventurers-pack")
def Adventurers_Pack():
	return render_template("adventurers-pack.html")

@app.route("/extendible-pincer")
def Extendible_Pincer():
	return render_template("extendible-pincer.html")

@app.route("/jellyfish-lamp")
def Jellyfish_Lamp():
	return render_template("jellyfish-lamp.html")

@app.route("/repair-kit")
def Repair_Kit():
	return render_template("repair-kit.html")

@app.route("/alchemists-tools")
def Alchemists_Tools():
	return render_template("alchemists-tools.html")

@app.route("/comealong")
def Comealong():
	return render_template("comealong.html")

@app.route("/folding-ladder")
def Folding_Ladder():
	return render_template("folding-ladder.html")

@app.route("/grappling-gun")
def Grappling_Gun():
	return render_template("grappling-gun.html")

@app.route("/hourglass")
def Hourglass():
	return render_template("hourglass.html")

@app.route("/artisans-tools")
def Artisans_Tools():
	return render_template("artisans-tools.html")

@app.route("/chain")
def Chain():
	return render_template("chain.html")

@app.route("/tack")
def Tack():
	return render_template("tack.html")

@app.route("/alchemists-lab")
def Alchemists_Lab():
	return render_template("alchemists-lab.html")

@app.route("/buoyancy-vest")
def Buoyancy_Vest():
	return render_template("buoyancy-vest.html")

@app.route("/familiar-satchel")
def Familiar_Satchel():
	return render_template("familiar-satchel.html")

@app.route("/glass-cutter")
def Glass_Cutter():
	return render_template("glass-cutter.html")

@app.route("/healers-tools")
def Healers_Tools():
	return render_template("healers-tools.html")

@app.route("/snare-kit")
def Snare_Kit():
	return render_template("snare-kit.html")

@app.route("/swim-fins")
def Swim_Fins():
	return render_template("swim-fins.html")

@app.route("/false-manacles")
def False_Manacles():
	return render_template("false-manacles.html")

@app.route("/snowshoes")
def Snowshoes():
	return render_template("snowshoes.html")

@app.route("/clockwork-dial")
def Clockwork_Dial():
	return render_template("clockwork-dial.html")

@app.route("/spyglass")
def Spyglass():
	return render_template("spyglass.html")

@app.route("/igniter")
def Igniter():
	return render_template("igniter.html")

@app.route("/waterproof-journal")
def Waterproof_Journal():
	return render_template("waterproof-journal.html")

@app.route("/communication-bangle")
def Communication_Bangle():
	return render_template("communication-bangle.html")

@app.route("/mechanical-torch")
def Mechanical_Torch():
	return render_template("mechanical-torch.html")

@app.route("/timepiece")
def Timepiece():
	return render_template("timepiece.html")

@app.route("/clockwork-megaphone")
def Clockwork_Megaphone():
	return render_template("clockwork-megaphone.html")

@app.route("/deployable-cover")
def Deployable_Cover():
	return render_template("deployable-cover.html")

@app.route("/swarmsuit")
def Swarmsuit():
	return render_template("swarmsuit.html")

@app.route("/book-of-translation")
def Book_of_Translation():
	return render_template("book-of-translation.html")

@app.route("/experimental-clothing")
def Experimental_Clothing():
	return render_template("experimental-clothing.html")

@app.route("/periscope")
def Periscope():
	return render_template("periscope.html")

@app.route("/day-goggles")
def Day_Goggles():
	return render_template("day-goggles.html")

@app.route("/sturdy-satchel")
def Sturdy_Satchel():
	return render_template("sturdy-satchel.html")

@app.route("/scholarly-journal")
def Scholarly_Journal():
	return render_template("scholarly-journal.html")

@app.route("/camouflage-suit")
def Camouflage_Suit():
	return render_template("camouflage-suit.html")

@app.route("/recovery-bladder")
def Recovery_Bladder():
	return render_template("recovery-bladder.html")

@app.route("/survey-map")
def Survey_Map():
	return render_template("survey-map.html")

@app.route("/portable-ram")
def Portable_Ram():
	return render_template("portable-ram.html")

@app.route("/smoked-goggles")
def Smoked_Goggles():
	return render_template("smoked-goggles.html")

@app.route("/concealed-sheath")
def Concealed_Sheath():
	return render_template("concealed-sheath.html")

@app.route("/detectives-kit")
def Detectives_Kit():
	return render_template("detectives-kit.html")

@app.route("/fingerprinting-kit")
def Fingerprinting_Kit():
	return render_template("fingerprinting-kit.html")

@app.route("/handcuffs")
def Handcuffs():
	return render_template("handcuffs.html")

@app.route("/magnifying-glass")
def Magnifying_Glass():
	return render_template("magnifying-glass.html")

@app.route("/cartographers-kit")
def Cartographers_Kit():
	return render_template("cartographers-kit.html")

@app.route("/pickpockets-tailoring")
def Pickpockets_Tailoring():
	return render_template("pickpockets-tailoring.html")

@app.route("/piton")
def Piton():
	return render_template("piton.html")

@app.route("/grappling-bolt")
def Grappling_Bolt():
	return render_template("grappling-bolt.html")

@app.route("/astrolabe")
def Astrolabe():
	return render_template("astrolabe.html")

@app.route("/fake-blood-pack")
def Fake_Blood_Pack():
	return render_template("fake-blood-pack.html")

@app.route("/alchemical-drugs")
def Alchemical_Drugs():
	return render_template("alchemical-drugs.html")

@app.route("/sneezing-powder")
def Sneezing_Powder():
	return render_template("sneezing-powder.html")

@app.route("/lethargy-poison-2242769")
def Lethargy_Poison():
	return render_template("lethargy-poison-2242769.html")

@app.route("/stupor-poison")
def Stupor_Poison():
	return render_template("stupor-poison.html")

@app.route("/shadow-essence")
def Shadow_Essence():
	return render_template("shadow-essence.html")

@app.route("/purple-worm-venom")
def Purple_Worm_Venom():
	return render_template("purple-worm-venom.html")

@app.route("/nightmare-vapor")
def Nightmare_Vapor():
	return render_template("nightmare-vapor.html")

@app.route("/alchemical-poisons")
def Alchemical_Poisons():
	return render_template("alchemical-poisons.html")

@app.route("/comprehension-elixir")
def Comprehension_Elixir():
	return render_template("comprehension-elixir.html")

@app.route("/alchemists-fire")
def Alchemists_Fire():
	return render_template("alchemists-fire.html")

@app.route("/bottled-lightning")
def Bottled_Lightning():
	return render_template("bottled-lightning.html")

@app.route("/alchemical-bombs")
def Alchemical_Bombs():
	return render_template("alchemical-bombs.html")

@app.route("/all-spells")
def All_Spells():
	return render_template("all-spells.html")

@app.route("/quench")
def Quench():
	return render_template("quench.html")

@app.route("/radiant-field")
def Radiant_Field():
	return render_template("radiant-field.html")

@app.route("/darkvision-5323541")
def Darkvision():
	return render_template("darkvision-5323541.html")

@app.route("/rapid-adaptation")
def Rapid_Adaptation():
	return render_template("rapid-adaptation.html")

@app.route("/reapers-lantern")
def Reapers_Lantern():
	return render_template("reapers-lantern.html")

@app.route("/remove-fear")
def Remove_Fear():
	return render_template("remove-fear.html")

@app.route("/historic-allies")
def Historic_Allies():
	return render_template("historic-allies.html")

@app.route("/killjoy")
def Killjoy():
	return render_template("killjoy.html")

@app.route("/duty")
def Duty():
	return render_template("duty.html")

@app.route("/selfish")
def Selfish():
	return render_template("selfish.html")

@app.route("/research-ritualized-casting")
def Research_Ritualized_Casting():
	return render_template("research-ritualized-casting.html")

@app.route("/bulk-and-lifting")
def Bulk_and_Lifting():
	return render_template("bulk-and-lifting.html")

@app.route("/ghoul")
def Ghoul():
	return render_template("ghoul.html")

@app.route("/plague-zombie")
def Plague_Zombie():
	return render_template("plague-zombie.html")

@app.route("/flaming-skull")
def Flaming_Skull():
	return render_template("flaming-skull.html")

@app.route("/skeletal-champion")
def Skeletal_Champion():
	return render_template("skeletal-champion.html")

@app.route("/zombie-brute")
def Zombie_Brute():
	return render_template("zombie-brute.html")

@app.route("/mummy-guardian")
def Mummy_Guardian():
	return render_template("mummy-guardian.html")

@app.route("/shadow")
def Shadow():
	return render_template("shadow.html")

@app.route("/zombie-hulk")
def Zombie_Hulk():
	return render_template("zombie-hulk.html")

@app.route("/dread-wraith")
def Dread_Wraith():
	return render_template("dread-wraith.html")

@app.route("/graveknight")
def Graveknight():
	return render_template("graveknight.html")

@app.route("/mohrg")
def Mohrg():
	return render_template("mohrg.html")

@app.route("/fell-rider")
def Fell_Rider():
	return render_template("fell-rider.html")

@app.route("/beast-tamer")
def Beast_Tamer():
	return render_template("beast-tamer.html")

@app.route("/polyglot")
def Polyglot():
	return render_template("polyglot.html")

@app.route("/unassuming-dedication")
def Unassuming_Dedication():
	return render_template("unassuming-dedication.html")

@app.route("/undead-companion")
def Undead_Companion():
	return render_template("undead-companion.html")

@app.route("/defy-the-darkness")
def Defy_the_Darkness():
	return render_template("defy-the-darkness.html")

@app.route("/corgi-mount")
def Corgi_Mount():
	return render_template("corgi-mount.html")

@app.route("/tupilaq-carver")
def Tupilaq_Carver():
	return render_template("tupilaq-carver.html")

@app.route("/animate-dead")
def Animate_Dead():
	return render_template("animate-dead.html")

@app.route("/phantom-steed")
def Phantom_Steed():
	return render_template("phantom-steed.html")

@app.route("/summon-instrument")
def Summon_Instrument():
	return render_template("summon-instrument.html")

@app.route("/crystal-shards")
def Crystal_Shards():
	return render_template("crystal-shards.html")

@app.route("/concecrate")
def Concecrate():
	return render_template("concecrate.html")

@app.route("/elemental-sentinel")
def Elemental_Sentinel():
	return render_template("elemental-sentinel.html")

@app.route("/fey-abeyance")
def Fey_Abeyance():
	return render_template("fey-abeyance.html")

@app.route("/heartbond")
def Heartbond():
	return render_template("heartbond.html")

@app.route("/arcane-weaving")
def Arcane_Weaving():
	return render_template("arcane-weaving.html")

@app.route("/atone")
def Atone():
	return render_template("atone.html")

@app.route("/awaken-portal")
def Awaken_Portal():
	return render_template("awaken-portal.html")

@app.route("/blight")
def Blight():
	return render_template("blight.html")

@app.route("/repair-public-work")
def Repair_Public_Work():
	return render_template("repair-public-work.html")

@app.route("/concealments-curtain")
def Concealments_Curtain():
	return render_template("concealments-curtain.html")

@app.route("/geas")
def Geas():
	return render_template("geas.html")

@app.route("/guardians-aegis")
def Guardians_Aegis():
	return render_template("guardians-aegis.html")

@app.route("/mystic-carriage")
def Mystic_Carriage():
	return render_template("mystic-carriage.html")

@app.route("/plant-growth")
def Plant_Growth():
	return render_template("plant-growth.html")

@app.route("/rest-eternal")
def Rest_Eternal():
	return render_template("rest-eternal.html")

@app.route("/simulacrum")
def Simulacrum():
	return render_template("simulacrum.html")

@app.route("/tattoo-whisperers")
def Tattoo_Whisperers():
	return render_template("tattoo-whisperers.html")

@app.route("/unseen-custodians")
def Unseen_Custodians():
	return render_template("unseen-custodians.html")

@app.route("/asmodean-wager")
def Asmodean_Wager():
	return render_template("asmodean-wager.html")

@app.route("/astral-projection")
def Astral_Projection():
	return render_template("astral-projection.html")

@app.route("/awaken-animal")
def Awaken_Animal():
	return render_template("awaken-animal.html")

@app.route("/awaken-object")
def Awaken_Object():
	return render_template("awaken-object.html")

@app.route("/call-spirit")
def Call_Spirit():
	return render_template("call-spirit.html")

@app.route("/commune")
def Commune():
	return render_template("commune.html")

@app.route("/commune-with-nature")
def Commune_with_Nature():
	return render_template("commune-with-nature.html")

@app.route("/dread-ambience")
def Dread_Ambience():
	return render_template("dread-ambience.html")

@app.route("/ideal-mimicry")
def Ideal_Mimicry():
	return render_template("ideal-mimicry.html")

@app.route("/mind-swap")
def Mind_Swap():
	return render_template("mind-swap.html")

@app.route("/mosquito-blight")
def Mosquito_Blight():
	return render_template("mosquito-blight.html")

@app.route("/planar-ally")
def Planar_Ally():
	return render_template("planar-ally.html")

@app.route("/primal-call")
def Primal_Call():
	return render_template("primal-call.html")

@app.route("/statuette")
def Statuette():
	return render_template("statuette.html")

@app.route("/terminate-bloodline")
def Terminate_Bloodline():
	return render_template("terminate-bloodline.html")

@app.route("/the-worlds-a-stage")
def The_Worlds_a_Stage():
	return render_template("the-worlds-a-stage.html")

@app.route("/waters-of-prediction")
def Waters_of_Prediction():
	return render_template("waters-of-prediction.html")

@app.route("/ward-domain")
def Ward_Domain():
	return render_template("ward-domain.html")

@app.route("/bathe-in-blood")
def Bathe_in_Blood():
	return render_template("bathe-in-blood.html")

@app.route("/control-weather")
def Control_Weather():
	return render_template("control-weather.html")

@app.route("/planar-traits")
def Planar_Traits():
	return render_template("planar-traits.html")

@app.route("/create-demiplane")
def Create_Demiplane():
	return render_template("create-demiplane.html")

@app.route("/freedom")
def Freedom():
	return render_template("freedom.html")

@app.route("/imprisonment")
def Imprisonment():
	return render_template("imprisonment.html")

@app.route("/legend-lore")
def Legend_Lore():
	return render_template("legend-lore.html")

@app.route("/remove-greater-curse")
def Remove_Greater_Curse():
	return render_template("remove-greater-curse.html")

@app.route("/summoned")
def Summoned():
	return render_template("summoned.html")

@app.route("/summon-elemental")
def Summon_Elemental():
	return render_template("summon-elemental.html")

@app.route("/chromatic-wall")
def Chromatic_Wall():
	return render_template("chromatic-wall.html")

@app.route("/prismatic-spray")
def Prismatic_Spray():
	return render_template("prismatic-spray.html")

@app.route("/maze-of-locked-doors")
def Maze_of_Locked_Doors():
	return render_template("maze-of-locked-doors.html")

@app.route("/maze")
def Maze():
	return render_template("maze.html")

@app.route("/magnificent-mansion")
def Magnificent_Mansion():
	return render_template("magnificent-mansion.html")

@app.route("/righteous-might")
def Righteous_Might():
	return render_template("righteous-might.html")

@app.route("/gray-shadow")
def Gray_Shadow():
	return render_template("gray-shadow.html")

@app.route("/mimic")
def Mimic():
	return render_template("mimic.html")

@app.route("/ravenous-portal")
def Ravenous_Portal():
	return render_template("ravenous-portal.html")

@app.route("/knock")
def Knock():
	return render_template("knock.html")

@app.route("/imprint-message")
def Imprint_Message():
	return render_template("imprint-message.html")

@app.route("/familiar")
def Familiar():
	return render_template("familiar.html")

@app.route("/sleep-eldritch-arrow")
def Sleep_Eldritch_Arrow():
	return render_template("sleep-eldritch-arrow.html")

@app.route("/unfolding-wind-rush")
def Unfolding_Wind_Rush():
	return render_template("unfolding-wind-rush.html")

@app.route("/quaking-stomp")
def Quaking_Stomp():
	return render_template("quaking-stomp.html")

@app.route("/dragon-transformation")
def Dragon_Transformation():
	return render_template("dragon-transformation.html")

@app.route("/animal-rage")
def Animal_Rage():
	return render_template("animal-rage.html")

@app.route("/parry-and-riposte")
def Parry_and_Riposte():
	return render_template("parry-and-riposte.html")

@app.route("/legendary-shot")
def Legendary_Shot():
	return render_template("legendary-shot.html")

@app.route("/rangers-twin-riposte")
def Rangers_Twin_Riposte():
	return render_template("rangers-twin-riposte.html")

@app.route("/mantis-form")
def Mantis_Form():
	return render_template("mantis-form.html")

@app.route("/vexing-tumble")
def Vexing_Tumble():
	return render_template("vexing-tumble.html")

@app.route("/nameless-anonymity")
def Nameless_Anonymity():
	return render_template("nameless-anonymity.html")

@app.route("/hidden-paragon")
def Hidden_Paragon():
	return render_template("hidden-paragon.html")

@app.route("/shadow-magic-dance-of-darkness")
def Shadow_Magic__Dance_of_Darkness():
	return render_template("shadow-magic-dance-of-darkness.html")

@app.route("/shadow-illusion")
def Shadow_Illusion():
	return render_template("shadow-illusion.html")

@app.route("/fey-caller")
def Fey_Caller():
	return render_template("fey-caller.html")

@app.route("/detect-magic")
def Detect_Magic():
	return render_template("detect-magic.html")

@app.route("/spell-tinker")
def Spell_Tinker():
	return render_template("spell-tinker.html")

@app.route("/interweave-dispel")
def Interweave_Dispel():
	return render_template("interweave-dispel.html")

@app.route("/elaborate-flourish")
def Elaborate_Flourish():
	return render_template("elaborate-flourish.html")

@app.route("/swift-banishment")
def Swift_Banishment():
	return render_template("swift-banishment.html")

@app.route("/aberrant-bloodline")
def Aberrant_Bloodline():
	return render_template("aberrant-bloodline.html")

@app.route("/form-retention")
def Form_Retention():
	return render_template("form-retention.html")

@app.route("/command-undead")
def Command_Undead():
	return render_template("command-undead.html")

@app.route("/persistent-creation")
def Persistent_Creation():
	return render_template("persistent-creation.html")

@app.route("/magical-scholastics")
def Magical_Scholastics():
	return render_template("magical-scholastics.html")

@app.route("/greater-magical-scholastics")
def Greater_Magical_Scholastics():
	return render_template("greater-magical-scholastics.html")

@app.route("/eternal-blessing")
def Eternal_Blessing():
	return render_template("eternal-blessing.html")

@app.route("/holy-water")
def Holy_Water():
	return render_template("holy-water.html")

@app.route("/sanctify-water")
def Sanctify_Water():
	return render_template("sanctify-water.html")

@app.route("/undead-bloodline-focus-undeaths-blessing")
def Undead_Bloodline_Focus__Undeaths_Blessing():
	return render_template("undead-bloodline-focus-undeaths-blessing.html")

@app.route("/angelic-bloodline-focus-angelic-wings")
def Angelic_Bloodline_Focus__Angelic_Wings():
	return render_template("angelic-bloodline-focus-angelic-wings.html")

@app.route("/read-disaster")
def Read_Disaster():
	return render_template("read-disaster.html")

@app.route("/true-perception")
def True_Perception():
	return render_template("true-perception.html")

@app.route("/lesson-of-mischief")
def Lesson_of_Mischief():
	return render_template("lesson-of-mischief.html")

@app.route("/familiar-form")
def Familiar_Form():
	return render_template("familiar-form.html")

@app.route("/plant-shape-3221644")
def Plant_Shape():
	return render_template("plant-shape-3221644.html")

@app.route("/rangers-bramble")
def Rangers_Bramble():
	return render_template("rangers-bramble.html")

@app.route("/thousand-faces")
def Thousand_Faces():
	return render_template("thousand-faces.html")

@app.route("/dragon-shape")
def Dragon_Shape():
	return render_template("dragon-shape.html")

@app.route("/monstrocity-shape")
def Monstrocity_Shape():
	return render_template("monstrocity-shape.html")

@app.route("/soaring-shape")
def Soaring_Shape():
	return render_template("soaring-shape.html")

@app.route("/ferocious-shape")
def Ferocious_Shape():
	return render_template("ferocious-shape.html")

@app.route("/elemental-shape")
def Elemental_Shape():
	return render_template("elemental-shape.html")

@app.route("/wild-shape")
def Wild_Shape():
	return render_template("wild-shape.html")

@app.route("/verdant-metamorphosis")
def Verdant_Metamorphosis():
	return render_template("verdant-metamorphosis.html")

@app.route("/green-tongue")
def Green_Tongue():
	return render_template("green-tongue.html")

@app.route("/mounted-shield")
def Mounted_Shield():
	return render_template("mounted-shield.html")

@app.route("/stormwind-flight")
def Stormwind_Flight():
	return render_template("stormwind-flight.html")

@app.route("/swarm-domain-swarm-sense")
def Swarm_Domain__Swarm_Sense():
	return render_template("swarm-domain-swarm-sense.html")

@app.route("/invoke-disaster")
def Invoke_Disaster():
	return render_template("invoke-disaster.html")

@app.route("/wind-caller")
def Wind_Caller():
	return render_template("wind-caller.html")

@app.route("/impaling-briars")
def Impaling_Briars():
	return render_template("impaling-briars.html")

@app.route("/fey-bloodline-focus-fey-glamour")
def Fey_Bloodline_Focus__Fey_Glamour():
	return render_template("fey-bloodline-focus-fey-glamour.html")

@app.route("/bonded-guardian")
def Bonded_Guardian():
	return render_template("bonded-guardian.html")

@app.route("/beast-speaker")
def Beast_Speaker():
	return render_template("beast-speaker.html")

@app.route("/stealthy-companion")
def Stealthy_Companion():
	return render_template("stealthy-companion.html")

@app.route("/talented-companion")
def Talented_Companion():
	return render_template("talented-companion.html")

@app.route("/animal-companion")
def Animal_Companion():
	return render_template("animal-companion.html")

@app.route("/tyranny-domain-commanding-lash")
def Tyranny_Domain__Commanding_Lash():
	return render_template("tyranny-domain-commanding-lash.html")

@app.route("/minion-guise")
def Minion_Guise():
	return render_template("minion-guise.html")

@app.route("/perfect-distraction")
def Perfect_Distraction():
	return render_template("perfect-distraction.html")

@app.route("/snare-rules")
def Snare_Rules():
	return render_template("snare-rules.html")

@app.route("/alarm-snare")
def Alarm_Snare():
	return render_template("alarm-snare.html")

@app.route("/appetizing-flavor-snare")
def Appetizing_Flavor_Snare():
	return render_template("appetizing-flavor-snare.html")

@app.route("/caltrop-snare")
def Caltrop_Snare():
	return render_template("caltrop-snare.html")

@app.route("/dust-pods")
def Dust_Pods():
	return render_template("dust-pods.html")

@app.route("/hampering-snare")
def Hampering_Snare():
	return render_template("hampering-snare.html")

@app.route("/marking-snare")
def Marking_Snare():
	return render_template("marking-snare.html")

@app.route("/signaling-snare")
def Signaling_Snare():
	return render_template("signaling-snare.html")

@app.route("/spike-snare")
def Spike_Snare():
	return render_template("spike-snare.html")

@app.route("/flare-snare")
def Flare_Snare():
	return render_template("flare-snare.html")

@app.route("/deadweight-snare")
def Deadweight_Snare():
	return render_template("deadweight-snare.html")

@app.route("/expulsion-snare")
def Expulsion_Snare():
	return render_template("expulsion-snare.html")

@app.route("/noisemaker-snare")
def Noisemaker_Snare():
	return render_template("noisemaker-snare.html")

@app.route("/static-snare")
def Static_Snare():
	return render_template("static-snare.html")

@app.route("/thunder-snare")
def Thunder_Snare():
	return render_template("thunder-snare.html")

@app.route("/clockwork-chirper")
def Clockwork_Chirper():
	return render_template("clockwork-chirper.html")

@app.route("/rock-ripper-snare")
def Rock_Ripper_Snare():
	return render_template("rock-ripper-snare.html")

@app.route("/grasping-tree")
def Grasping_Tree():
	return render_template("grasping-tree.html")

@app.route("/torrent-snare")
def Torrent_Snare():
	return render_template("torrent-snare.html")

@app.route("/fire-box")
def Fire_Box():
	return render_template("fire-box.html")

@app.route("/detonating-gears-snare")
def Detonating_Gears_Snare():
	return render_template("detonating-gears-snare.html")

@app.route("/acid-spitter")
def Acid_Spitter():
	return render_template("acid-spitter.html")

@app.route("/biting-snare")
def Biting_Snare():
	return render_template("biting-snare.html")

@app.route("/hobbling-snare")
def Hobbling_Snare():
	return render_template("hobbling-snare.html")

@app.route("/stalker-bane-snare")
def Stalker_Bane_Snare():
	return render_template("stalker-bane-snare.html")

@app.route("/tar-rocket-snare")
def Tar_Rocket_Snare():
	return render_template("tar-rocket-snare.html")

@app.route("/trip-snare")
def Trip_Snare():
	return render_template("trip-snare.html")

@app.route("/warning-snare")
def Warning_Snare():
	return render_template("warning-snare.html")

@app.route("/boom-snare")
def Boom_Snare():
	return render_template("boom-snare.html")

@app.route("/glittering-snare")
def Glittering_Snare():
	return render_template("glittering-snare.html")

@app.route("/fang-snare")
def Fang_Snare():
	return render_template("fang-snare.html")

@app.route("/clinging-ooze-snare")
def Clinging_Ooze_Snare():
	return render_template("clinging-ooze-snare.html")

@app.route("/tin-cobra")
def Tin_Cobra():
	return render_template("tin-cobra.html")

@app.route("/flame-drake-snare")
def Flame_Drake_Snare():
	return render_template("flame-drake-snare.html")

@app.route("/pummeling-snare")
def Pummeling_Snare():
	return render_template("pummeling-snare.html")

@app.route("/wet-shock-snare")
def Wet_Shock_Snare():
	return render_template("wet-shock-snare.html")

@app.route("/mirror-ball-snare")
def Mirror_Ball_Snare():
	return render_template("mirror-ball-snare.html")

@app.route("/nauseating-snare")
def Nauseating_Snare():
	return render_template("nauseating-snare.html")

@app.route("/piercing-whistle-snare")
def Piercing_Whistle_Snare():
	return render_template("piercing-whistle-snare.html")

@app.route("/envenomed-snare")
def Envenomed_Snare():
	return render_template("envenomed-snare.html")

@app.route("/bomb-snare")
def Bomb_Snare():
	return render_template("bomb-snare.html")

@app.route("/grasping-snare")
def Grasping_Snare():
	return render_template("grasping-snare.html")

@app.route("/rusting-snare")
def Rusting_Snare():
	return render_template("rusting-snare.html")

@app.route("/striking-snare")
def Striking_Snare():
	return render_template("striking-snare.html")

@app.route("/spirit-snare")
def Spirit_Snare():
	return render_template("spirit-snare.html")

@app.route("/frost-worm-snare")
def Frost_Worm_Snare():
	return render_template("frost-worm-snare.html")

@app.route("/puff-dragon")
def Puff_Dragon():
	return render_template("puff-dragon.html")

@app.route("/binding-snare")
def Binding_Snare():
	return render_template("binding-snare.html")

@app.route("/burning-badger-guts-snare")
def Burning_Badger_Guts_Snare():
	return render_template("burning-badger-guts-snare.html")

@app.route("/mudrock-snare")
def Mudrock_Snare():
	return render_template("mudrock-snare.html")

@app.route("/snagging-hook-snare")
def Snagging_Hook_Snare():
	return render_template("snagging-hook-snare.html")

@app.route("/scything-blade-snare")
def Scything_Blade_Snare():
	return render_template("scything-blade-snare.html")

@app.route("/bleeding-spines-snare")
def Bleeding_Spines_Snare():
	return render_template("bleeding-spines-snare.html")

@app.route("/stunning-snare")
def Stunning_Snare():
	return render_template("stunning-snare.html")

@app.route("/shrapnel-snare")
def Shrapnel_Snare():
	return render_template("shrapnel-snare.html")

@app.route("/snares")
def Snares():
	return render_template("snares.html")

@app.route("/snare-crafting")
def Snare_Crafting():
	return render_template("snare-crafting.html")

@app.route("/stone-communion")
def Stone_Communion():
	return render_template("stone-communion.html")

@app.route("/attunement-to-stone")
def Attunement_to_Stone():
	return render_template("attunement-to-stone.html")

@app.route("/judgement-of-the-monolith")
def Judgement_of_the_Monolith():
	return render_template("judgement-of-the-monolith.html")

@app.route("/ka-stone-ritual")
def Ka_Stone_Ritual():
	return render_template("ka-stone-ritual.html")

@app.route("/lethargy-poison")
def Lethargy_Poison():
	return render_template("lethargy-poison.html")

@app.route("/eye-of-the-arclords")
def Eye_of_the_Arclords():
	return render_template("eye-of-the-arclords.html")

@app.route("/arcane-sense")
def Arcane_Sense():
	return render_template("arcane-sense.html")

@app.route("/magical-hideaway")
def Magical_Hideaway():
	return render_template("magical-hideaway.html")

@app.route("/invisibility-cloak")
def Invisibility_Cloak():
	return render_template("invisibility-cloak.html")

@app.route("/shape-of-the-dragon")
def Shape_of_the_Dragon():
	return render_template("shape-of-the-dragon.html")

@app.route("/perpetual-surgeon")
def Perpetual_Surgeon():
	return render_template("perpetual-surgeon.html")

@app.route("/subtle-delivery")
def Subtle_Delivery():
	return render_template("subtle-delivery.html")

@app.route("/mindblank-mutagen")
def Mindblank_Mutagen():
	return render_template("mindblank-mutagen.html")

@app.route("/invincible-mutagen")
def Invincible_Mutagen():
	return render_template("invincible-mutagen.html")

@app.route("/glib-mutagen")
def Glib_Mutagen():
	return render_template("glib-mutagen.html")

@app.route("/genius-mutagen")
def Genius_Mutagen():
	return render_template("genius-mutagen.html")

@app.route("/elastic-mutagen")
def Elastic_Mutagen():
	return render_template("elastic-mutagen.html")

@app.route("/miracle-worker")
def Miracle_Worker():
	return render_template("miracle-worker.html")

@app.route("/tumbling-opportunist")
def Tumbling_Opportunist():
	return render_template("tumbling-opportunist.html")

@app.route("/fortify-shield")
def Fortify_Shield():
	return render_template("fortify-shield.html")

@app.route("/shadow-pact")
def Shadow_Pact():
	return render_template("shadow-pact.html")

@app.route("/anarchic-arcana")
def Anarchic_Arcana():
	return render_template("anarchic-arcana.html")

@app.route("/plant-shape")
def Plant_Shape():
	return render_template("plant-shape.html")

@app.route("/breath-paragon")
def Breath_Paragon():
	return render_template("breath-paragon.html")

@app.route("/alchemical-crafting")
def Alchemical_Crafting():
	return render_template("alchemical-crafting.html")

@app.route("/alchemical-items")
def Alchemical_Items():
	return render_template("alchemical-items.html")

@app.route("/warrior-feats")
def Warrior_Feats():
	return render_template("warrior-feats.html")

@app.route("/focus-spells")
def Focus_Spells():
	return render_template("focus-spells.html")

@app.route("/gauntlet")
def Gauntlet():
	return render_template("gauntlet.html")

@app.route("/absent-minded")
def Absent_Minded():
	return render_template("absent-minded.html")

@app.route("/gill-hook")
def Gill_Hook():
	return render_template("gill-hook.html")

@app.route("/longbow")
def Longbow():
	return render_template("longbow.html")

@app.route("/sun-sling")
def Sun_Sling():
	return render_template("sun-sling.html")

@app.route("/weapons-list")
def Weapons_List():
	return render_template("weapons-list.html")

@app.route("/crane-stance")
def Crane_Stance():
	return render_template("crane-stance.html")

@app.route("/clinging-shadows-stance")
def Clinging_Shadows_Stance():
	return render_template("clinging-shadows-stance.html")

@app.route("/cobra-stance")
def Cobra_Stance():
	return render_template("cobra-stance.html")

@app.route("/powerful-fist")
def Powerful_Fist():
	return render_template("powerful-fist.html")

@app.route("/ritual-rules")
def Ritual_Rules():
	return render_template("ritual-rules.html")

@app.route("/ritual-list")
def Ritual_List():
	return render_template("ritual-list.html")

@app.route("/chromatic-ray")
def Chromatic_Ray():
	return render_template("chromatic-ray.html")

@app.route("/arcane-spells")
def Arcane_Spells():
	return render_template("arcane-spells.html")

@app.route("/knockdown-monster-ability")
def Knockdown__Monster_ability_():
	return render_template("knockdown-monster-ability.html")

@app.route("/shadow-mage-occult-caster")
def Shadow_Mage__Occult_Caster_():
	return render_template("shadow-mage-occult-caster.html")

@app.route("/encounter-mode")
def Encounter_Mode():
	return render_template("encounter-mode.html")

@app.route("/animal-form")
def Animal_Form():
	return render_template("animal-form.html")

@app.route("/arcane-cascade")
def Arcane_Cascade():
	return render_template("arcane-cascade.html")

@app.route("/laughing-shadow")
def Laughing_Shadow():
	return render_template("laughing-shadow.html")

@app.route("/inexorable-iron")
def Inexorable_Iron():
	return render_template("inexorable-iron.html")

@app.route("/raise-a-tome")
def Raise_a_Tome():
	return render_template("raise-a-tome.html")

@app.route("/sparkling-targe")
def Sparkling_Targe():
	return render_template("sparkling-targe.html")

@app.route("/twisting-tree")
def Twisting_Tree():
	return render_template("twisting-tree.html")

@app.route("/maguss-analysis")
def Maguss_Analysis():
	return render_template("maguss-analysis.html")

@app.route("/force-fang")
def Force_Fang():
	return render_template("force-fang.html")

@app.route("/spell-parry")
def Spell_Parry():
	return render_template("spell-parry.html")

@app.route("/devastating-spellstrike")
def Devastating_Spellstrike():
	return render_template("devastating-spellstrike.html")

@app.route("/distracting-spellstrike")
def Distracting_Spellstrike():
	return render_template("distracting-spellstrike.html")

@app.route("/emergency-targe")
def Emergency_Targe():
	return render_template("emergency-targe.html")

@app.route("/starlit-eyes")
def Starlit_Eyes():
	return render_template("starlit-eyes.html")

@app.route("/shielded-tome")
def Shielded_Tome():
	return render_template("shielded-tome.html")

@app.route("/capture-magic")
def Capture_Magic():
	return render_template("capture-magic.html")

@app.route("/runic-impression")
def Runic_Impression():
	return render_template("runic-impression.html")

@app.route("/dazzling-block")
def Dazzling_Block():
	return render_template("dazzling-block.html")

@app.route("/rapid-recharge")
def Rapid_Recharge():
	return render_template("rapid-recharge.html")

@app.route("/sustaining-steel")
def Sustaining_Steel():
	return render_template("sustaining-steel.html")

@app.route("/preternatural-parry")
def Preternatural_Parry():
	return render_template("preternatural-parry.html")

@app.route("/expansive-spellstrike")
def Expansive_Spellstrike():
	return render_template("expansive-spellstrike.html")

@app.route("/spirit-sheath")
def Spirit_Sheath():
	return render_template("spirit-sheath.html")

@app.route("/cascade-countermeasure")
def Cascade_Countermeasure():
	return render_template("cascade-countermeasure.html")

@app.route("/spell-swipe")
def Spell_Swipe():
	return render_template("spell-swipe.html")

@app.route("/cascading-ray")
def Cascading_Ray():
	return render_template("cascading-ray.html")

@app.route("/dimensional-disappearance")
def Dimensional_Disappearance():
	return render_template("dimensional-disappearance.html")

@app.route("/lunging-spellstrike")
def Lunging_Spellstrike():
	return render_template("lunging-spellstrike.html")

@app.route("/meteoric-spellstrike")
def Meteoric_Spellstrike():
	return render_template("meteoric-spellstrike.html")

@app.route("/overwhelming-spellstrike")
def Overwhelming_Spellstrike():
	return render_template("overwhelming-spellstrike.html")

@app.route("/arcane-shroud")
def Arcane_Shroud():
	return render_template("arcane-shroud.html")

@app.route("/hasted-assault")
def Hasted_Assault():
	return render_template("hasted-assault.html")

@app.route("/dispelling-spellstrike")
def Dispelling_Spellstrike():
	return render_template("dispelling-spellstrike.html")

@app.route("/resounding-cascade")
def Resounding_Cascade():
	return render_template("resounding-cascade.html")

@app.route("/whirlwind-spell")
def Whirlwind_Spell():
	return render_template("whirlwind-spell.html")

@app.route("/long-strider")
def Long_Strider():
	return render_template("long-strider.html")

@app.route("/eldritch-archer")
def Eldritch_Archer():
	return render_template("eldritch-archer.html")

@app.route("/cauldron")
def Cauldron():
	return render_template("cauldron.html")

@app.route("/temporary-potions")
def Temporary_Potions():
	return render_template("temporary-potions.html")

@app.route("/intimidating-prowess")
def Intimidating_Prowess():
	return render_template("intimidating-prowess.html")

@app.route("/intimidation-feats")
def Intimidation_Feats():
	return render_template("intimidation-feats.html")

@app.route("/incapacitation")
def Incapacitation():
	return render_template("incapacitation.html")

@app.route("/shadow-walk")
def Shadow_Walk():
	return render_template("shadow-walk.html")

@app.route("/glimpse-of-redemption")
def Glimpse_of_Redemption():
	return render_template("glimpse-of-redemption.html")

@app.route("/elite-manticore")
def Elite_Manticore():
	return render_template("elite-manticore.html")

@app.route("/ghost")
def Ghost():
	return render_template("ghost.html")

@app.route("/ghost-mage")
def Ghost_Mage():
	return render_template("ghost-mage.html")

@app.route("/bestial")
def Bestial():
	return render_template("bestial.html")

@app.route("/chummy")
def Chummy():
	return render_template("chummy.html")

@app.route("/fanaticism")
def Fanaticism():
	return render_template("fanaticism.html")

@app.route("/hidebound")
def Hidebound():
	return render_template("hidebound.html")

@app.route("/laziness")
def Laziness():
	return render_template("laziness.html")

@app.route("/low-empathy")
def Low_Empathy():
	return render_template("low-empathy.html")

@app.route("/megalomania")
def Megalomania():
	return render_template("megalomania.html")

@app.route("/overconfident")
def Overconfident():
	return render_template("overconfident.html")

@app.route("/magical-crafting")
def Magical_Crafting():
	return render_template("magical-crafting.html")

@app.route("/buckler")
def Buckler():
	return render_template("buckler.html")

@app.route("/wooden-shield")
def Wooden_Shield():
	return render_template("wooden-shield.html")

@app.route("/steel-shield")
def Steel_Shield():
	return render_template("steel-shield.html")

@app.route("/tower-shield")
def Tower_Shield():
	return render_template("tower-shield.html")

@app.route("/shield-rules")
def Shield_Rules():
	return render_template("shield-rules.html")

@app.route("/critical-misses")
def Critical_Misses():
	return render_template("critical-misses.html")

@app.route("/crafters-appraisal")
def Crafters_Appraisal():
	return render_template("crafters-appraisal.html")

@app.route("/evanescent-wings")
def Evanescent_Wings():
	return render_template("evanescent-wings.html")

@app.route("/spellstrike")
def Spellstrike():
	return render_template("spellstrike.html")

@app.route("/improved-knockback")
def Improved_Knockback():
	return render_template("improved-knockback.html")

@app.route("/all-about-complications")
def All_About_Complications():
	return render_template("all-about-complications.html")

@app.route("/alchemical-tools")
def Alchemical_Tools():
	return render_template("alchemical-tools.html")

@app.route("/mana-oil")
def Mana_Oil():
	return render_template("mana-oil.html")

@app.route("/assassin")
def Assassin():
	return render_template("assassin.html")

@app.route("/poisonous-deluge")
def Poisonous_Deluge():
	return render_template("poisonous-deluge.html")

@app.route("/rope-master")
def Rope_Master():
	return render_template("rope-master.html")

@app.route("/athletics-class-feats")
def Athletics_Class_Feats():
	return render_template("athletics-class-feats.html")

@app.route("/innocent-butterfly")
def Innocent_Butterfly():
	return render_template("innocent-butterfly.html")

@app.route("/beneath-notice")
def Beneath_Notice():
	return render_template("beneath-notice.html")

@app.route("/deception-feats")
def Deception_Feats():
	return render_template("deception-feats.html")

@app.route("/phoenix-bloodline-focus-shroud-of-flame")
def Phoenix_Bloodline_Focus__Shroud_of_Flame():
	return render_template("phoenix-bloodline-focus-shroud-of-flame.html")

@app.route("/phoenix-bloodline-focus-cleansing-flames")
def Phoenix_Bloodline_Focus__Cleansing_Flames():
	return render_template("phoenix-bloodline-focus-cleansing-flames.html")

@app.route("/all-the-time-in-the-world")
def All_the_Time_in_the_World():
	return render_template("all-the-time-in-the-world.html")

@app.route("/perception-feats")
def Perception_Feats():
	return render_template("perception-feats.html")

@app.route("/head-of-the-night-parade")
def Head_of_the_Night_Parade():
	return render_template("head-of-the-night-parade.html")

@app.route("/criminal-dedication")
def Criminal_Dedication():
	return render_template("criminal-dedication.html")

@app.route("/worldsphere-gravity")
def Worldsphere_Gravity():
	return render_template("worldsphere-gravity.html")

@app.route("/shift-spell")
def Shift_Spell():
	return render_template("shift-spell.html")

@app.route("/phoenix-bloodline")
def Phoenix_Bloodline():
	return render_template("phoenix-bloodline.html")

@app.route("/ruby-resurrection")
def Ruby_Resurrection():
	return render_template("ruby-resurrection.html")

@app.route("/extradimensional-stash")
def Extradimensional_Stash():
	return render_template("extradimensional-stash.html")

@app.route("/thievery-feats")
def Thievery_Feats():
	return render_template("thievery-feats.html")

@app.route("/entwined-energy-ki")
def Entwined_Energy_Ki():
	return render_template("entwined-energy-ki.html")

@app.route("/wronged-monks-wrath")
def Wronged_Monks_Wrath():
	return render_template("wronged-monks-wrath.html")

@app.route("/jellyfish-stance")
def Jellyfish_Stance():
	return render_template("jellyfish-stance.html")

@app.route("/effortless-reach")
def Effortless_Reach():
	return render_template("effortless-reach.html")

@app.route("/electric-counter")
def Electric_Counter():
	return render_template("electric-counter.html")

@app.route("/sense-ki")
def Sense_Ki():
	return render_template("sense-ki.html")

@app.route("/vitality-manipulating-stance")
def Vitality_Manipulating_Stance():
	return render_template("vitality-manipulating-stance.html")

@app.route("/sever-space")
def Sever_Space():
	return render_template("sever-space.html")

@app.route("/whirlwind-toss")
def Whirlwind_Toss():
	return render_template("whirlwind-toss.html")

@app.route("/ghost-eater")
def Ghost_Eater():
	return render_template("ghost-eater.html")

@app.route("/reach-beyond")
def Reach_Beyond():
	return render_template("reach-beyond.html")

@app.route("/disrupting-strikes")
def Disrupting_Strikes():
	return render_template("disrupting-strikes.html")

@app.route("/ever-distant-defense")
def Ever_distant_Defense():
	return render_template("ever-distant-defense.html")

@app.route("/six-pillars-stance")
def Six_Pillars_Stance():
	return render_template("six-pillars-stance.html")

@app.route("/maneuvering-spell")
def Maneuvering_Spell():
	return render_template("maneuvering-spell.html")

@app.route("/touch-focus")
def Touch_Focus():
	return render_template("touch-focus.html")

@app.route("/warrior-spellcaster-feats")
def Warrior___Spellcaster_Feats():
	return render_template("warrior-spellcaster-feats.html")

@app.route("/vivacious-afterimage")
def Vivacious_Afterimage():
	return render_template("vivacious-afterimage.html")

@app.route("/time-dilation-cascade")
def Time_Dilation_Cascade():
	return render_template("time-dilation-cascade.html")

@app.route("/changelog-march-10-2022")
def Changelog__March_10_2022():
	return render_template("changelog-march-10-2022.html")

@app.route("/ogre-glutton")
def Ogre_Glutton():
	return render_template("ogre-glutton.html")

@app.route("/harpy")
def Harpy():
	return render_template("harpy.html")

@app.route("/banshee")
def Banshee():
	return render_template("banshee.html")

@app.route("/zombie-sharks")
def Zombie_Sharks():
	return render_template("zombie-sharks.html")

@app.route("/orc-marauder")
def Orc_Marauder():
	return render_template("orc-marauder.html")

@app.route("/approximate")
def Approximate():
	return render_template("approximate.html")

@app.route("/what-is-this-game")
def What_is_this_game():
	return render_template("what-is-this-game.html")

@app.route("/crimson-shroud")
def Crimson_Shroud():
	return render_template("crimson-shroud.html")

@app.route("/blade-ally")
def Blade_Ally():
	return render_template("blade-ally.html")

@app.route("/religion-warrior-feats")
def Religion___Warrior_Feats():
	return render_template("religion-warrior-feats.html")

@app.route("/radiant-blade-spirit")
def Radiant_Blade_Spirit():
	return render_template("radiant-blade-spirit.html")

@app.route("/witchs-hut")
def Witchs_Hut():
	return render_template("witchs-hut.html")

@app.route("/snare-specialist")
def Snare_Specialist():
	return render_template("snare-specialist.html")

@app.route("/heal-animal")
def Heal_Animal():
	return render_template("heal-animal.html")

@app.route("/nature-domain-natures-bounty")
def Nature_Domain__Natures_Bounty():
	return render_template("nature-domain-natures-bounty.html")

@app.route("/phoenix-bloodline-focus-rejuvenating-flames")
def Phoenix_Bloodline_Focus__Rejuvenating_Flames():
	return render_template("phoenix-bloodline-focus-rejuvenating-flames.html")

@app.route("/focused-locks")
def Focused_Locks():
	return render_template("focused-locks.html")

@app.route("/composition-spells")
def Composition_Spells():
	return render_template("composition-spells.html")

@app.route("/runescarred")
def Runescarred():
	return render_template("runescarred.html")

@app.route("/minor-magic")
def Minor_Magic():
	return render_template("minor-magic.html")

@app.route("/elite-anchorite-of-talos")
def Elite_Anchorite_of_Talos():
	return render_template("elite-anchorite-of-talos.html")

@app.route("/adult-white-dragon")
def Adult_White_Dragon():
	return render_template("adult-white-dragon.html")

@app.route("/elite-white-dragon")
def Elite_White_Dragon():
	return render_template("elite-white-dragon.html")

@app.route("/prestidigitation")
def Prestidigitation():
	return render_template("prestidigitation.html")

@app.route("/inner-radiance-torrent")
def Inner_Radiance_Torrent():
	return render_template("inner-radiance-torrent.html")

@app.route("/elite-mimic")
def Elite_Mimic():
	return render_template("elite-mimic.html")

@app.route("/assassin-5866037")
def Assassin():
	return render_template("assassin-5866037.html")

@app.route("/gnome-in-an-auto-turret")
def Gnome_in_an_Auto_Turret():
	return render_template("gnome-in-an-auto-turret.html")

@app.route("/ochre-jelly")
def Ochre_Jelly():
	return render_template("ochre-jelly.html")

@app.route("/redclaw-orc-ranger")
def Redclaw_Orc_Ranger():
	return render_template("redclaw-orc-ranger.html")

@app.route("/cutthroat-thug")
def Cutthroat_Thug():
	return render_template("cutthroat-thug.html")

@app.route("/redclaw-orc-skirmishers")
def Redclaw_Orc_Skirmishers():
	return render_template("redclaw-orc-skirmishers.html")

@app.route("/heroes-feast")
def Heroes_Feast():
	return render_template("heroes-feast.html")

@app.route("/school-specialist")
def School_Specialist():
	return render_template("school-specialist.html")

@app.route("/spell-prodigy")
def Spell_Prodigy():
	return render_template("spell-prodigy.html")

@app.route("/debilitating-strike")
def Debilitating_Strike():
	return render_template("debilitating-strike.html")

@app.route("/relentless-stalker")
def Relentless_Stalker():
	return render_template("relentless-stalker.html")

@app.route("/crafting-feats")
def Crafting_Feats():
	return render_template("crafting-feats.html")

@app.route("/living-monolith")
def Living_Monolith():
	return render_template("living-monolith.html")

@app.route("/perform-surgery")
def Perform_Surgery():
	return render_template("perform-surgery.html")

@app.route("/stabilize-injuries")
def Stabilize_Injuries():
	return render_template("stabilize-injuries.html")

@app.route("/medicine-int")
def Medicine__INT_():
	return render_template("medicine-int.html")

@app.route("/hit-locations")
def Hit_Locations():
	return render_template("hit-locations.html")

@app.route("/body-fruit")
def Body_Fruit():
	return render_template("body-fruit.html")

@app.route("/glory-and-valor")
def Glory_and_Valor():
	return render_template("glory-and-valor.html")

@app.route("/dying")
def Dying():
	return render_template("dying.html")

@app.route("/death-dying-and-recovery")
def Death_Dying_and_Recovery():
	return render_template("death-dying-and-recovery.html")

@app.route("/incredibly-hardy")
def Incredibly_Hardy():
	return render_template("incredibly-hardy.html")

@app.route("/internal-cohesion")
def Internal_Cohesion():
	return render_template("internal-cohesion.html")

@app.route("/regenerative-blood")
def Regenerative_Blood():
	return render_template("regenerative-blood.html")

@app.route("/rejuvenation")
def Rejuvenation():
	return render_template("rejuvenation.html")

@app.route("/revivification")
def Revivification():
	return render_template("revivification.html")

@app.route("/revivifying-mutagen")
def Revivifying_Mutagen():
	return render_template("revivifying-mutagen.html")

@app.route("/consume-spell")
def Consume_Spell():
	return render_template("consume-spell.html")

@app.route("/familiars")
def Familiars():
	return render_template("familiars.html")

@app.route("/communal-healing")
def Communal_Healing():
	return render_template("communal-healing.html")

@app.route("/magic-hands")
def Magic_Hands():
	return render_template("magic-hands.html")

@app.route("/resurrectionist")
def Resurrectionist():
	return render_template("resurrectionist.html")

@app.route("/healing")
def Healing():
	return render_template("healing.html")

@app.route("/healing-transformation")
def Healing_Transformation():
	return render_template("healing-transformation.html")

@app.route("/superstition-instinct")
def Superstition_Instinct():
	return render_template("superstition-instinct.html")

@app.route("/shall-not-falter-shall-not-rout")
def Shall_not_falter_shall_not_rout():
	return render_template("shall-not-falter-shall-not-rout.html")

@app.route("/numb-to-death")
def Numb_to_Death():
	return render_template("numb-to-death.html")

@app.route("/fast-recovery")
def Fast_Recovery():
	return render_template("fast-recovery.html")

@app.route("/life-syphon")
def Life_Syphon():
	return render_template("life-syphon.html")

@app.route("/align-ki")
def Align_Ki():
	return render_template("align-ki.html")

@app.route("/warrior-ki-arts-feats")
def Warrior_Ki_Arts_Feats():
	return render_template("warrior-ki-arts-feats.html")

@app.route("/battle-medicine")
def Battle_Medicine():
	return render_template("battle-medicine.html")

@app.route("/superior-medic")
def Superior_Medic():
	return render_template("superior-medic.html")

@app.route("/godless-healing")
def Godless_Healing():
	return render_template("godless-healing.html")

@app.route("/continual-recovery")
def Continual_Recovery():
	return render_template("continual-recovery.html")

@app.route("/risky-surgery")
def Risky_Surgery():
	return render_template("risky-surgery.html")

@app.route("/nature-feats")
def Nature_Feats():
	return render_template("nature-feats.html")

@app.route("/soothing-mist")
def Soothing_Mist():
	return render_template("soothing-mist.html")

@app.route("/wholeness-of-body")
def Wholeness_of_Body():
	return render_template("wholeness-of-body.html")

@app.route("/lesson-of-life")
def Lesson_of_Life():
	return render_template("lesson-of-life.html")

@app.route("/goodberry")
def Goodberry():
	return render_template("goodberry.html")

@app.route("/occultism-feats")
def Occultism_Feats():
	return render_template("occultism-feats.html")

@app.route("/performance-feats")
def Performance_Feats():
	return render_template("performance-feats.html")

@app.route("/healing-domain-rebuke-death")
def Healing_Domain_Rebuke_Death():
	return render_template("healing-domain-rebuke-death.html")

@app.route("/lay-on-hands")
def Lay_on_Hands():
	return render_template("lay-on-hands.html")

@app.route("/religion-feats")
def Religion_Feats():
	return render_template("religion-feats.html")

@app.route("/heal")
def Heal():
	return render_template("heal.html")

@app.route("/soothing-spring")
def Soothing_Spring():
	return render_template("soothing-spring.html")

@app.route("/positive-attunement")
def Positive_Attunement():
	return render_template("positive-attunement.html")

@app.route("/primal-spells")
def Primal_Spells():
	return render_template("primal-spells.html")

@app.route("/vital-beacon")
def Vital_Beacon():
	return render_template("vital-beacon.html")

@app.route("/occult-spells")
def Occult_Spells():
	return render_template("occult-spells.html")

@app.route("/healing-plaster")
def Healing_Plaster():
	return render_template("healing-plaster.html")

@app.route("/medicine-feats")
def Medicine_Feats():
	return render_template("medicine-feats.html")

@app.route("/soften-fall")
def Soften_Fall():
	return render_template("soften-fall.html")

@app.route("/ward-opening")
def Ward_Opening():
	return render_template("ward-opening.html")

@app.route("/elemental-shield")
def Elemental_Shield():
	return render_template("elemental-shield.html")

@app.route("/kinetic-shield")
def Kinetic_Shield():
	return render_template("kinetic-shield.html")

@app.route("/esoteric-shield")
def Esoteric_Shield():
	return render_template("esoteric-shield.html")

@app.route("/waterproofing")
def Waterproofing():
	return render_template("waterproofing.html")

@app.route("/sight-ward")
def Sight_Ward():
	return render_template("sight-ward.html")

@app.route("/sound-ward")
def Sound_Ward():
	return render_template("sound-ward.html")

@app.route("/reflect-blow")
def Reflect_Blow():
	return render_template("reflect-blow.html")

@app.route("/resist-motion")
def Resist_Motion():
	return render_template("resist-motion.html")

@app.route("/soothing-ballad")
def Soothing_Ballad():
	return render_template("soothing-ballad.html")

@app.route("/armor-proficiency")
def Armor_Proficiency():
	return render_template("armor-proficiency.html")

@app.route("/quick-copy")
def Quick_Copy():
	return render_template("quick-copy.html")

@app.route("/transfer-ink")
def Transfer_Ink():
	return render_template("transfer-ink.html")

@app.route("/formation-master")
def Formation_Master():
	return render_template("formation-master.html")

@app.route("/squad-tactics")
def Squad_Tactics():
	return render_template("squad-tactics.html")

@app.route("/mirror-shield")
def Mirror_Shield():
	return render_template("mirror-shield.html")

@app.route("/reflecting-reposte")
def Reflecting_Reposte():
	return render_template("reflecting-reposte.html")

@app.route("/warrior-weapon-style-feats")
def Warrior_Weapon_Style_Feats():
	return render_template("warrior-weapon-style-feats.html")

@app.route("/water-born")
def Water_Born():
	return render_template("water-born.html")

@app.route("/swim")
def Swim():
	return render_template("swim.html")

@app.route("/water-dancer")
def Water_Dancer():
	return render_template("water-dancer.html")

@app.route("/natural-swimmer")
def Natural_Swimmer():
	return render_template("natural-swimmer.html")

@app.route("/strong-swimmer")
def Strong_Swimmer():
	return render_template("strong-swimmer.html")

@app.route("/aquatic-adaptation")
def Aquatic_Adaptation():
	return render_template("aquatic-adaptation.html")

@app.route("/avenge-ally")
def Avenge_Ally():
	return render_template("avenge-ally.html")

@app.route("/pride-in-arms")
def Pride_in_Arms():
	return render_template("pride-in-arms.html")

@app.route("/shoulder-the-load")
def Shoulder_the_Load():
	return render_template("shoulder-the-load.html")

@app.route("/cover-foibles")
def Cover_Foibles():
	return render_template("cover-foibles.html")

@app.route("/touch-telepath")
def Touch_Telepath():
	return render_template("touch-telepath.html")

@app.route("/helpful")
def Helpful():
	return render_template("helpful.html")

@app.route("/battleforger")
def Battleforger():
	return render_template("battleforger.html")

@app.route("/innocuous")
def Innocuous():
	return render_template("innocuous.html")

@app.route("/oath-keeper")
def Oath_keeper():
	return render_template("oath-keeper.html")

@app.route("/dragons-breath")
def Dragons_Breath():
	return render_template("dragons-breath.html")

@app.route("/yamarajs-grandeur")
def Yamarajs_Grandeur():
	return render_template("yamarajs-grandeur.html")

@app.route("/ancestral-friend")
def Ancestral_Friend():
	return render_template("ancestral-friend.html")

@app.route("/heat-acclimatization")
def Heat_Acclimatization():
	return render_template("heat-acclimatization.html")

@app.route("/cold-acclimatization")
def Cold_Acclimatization():
	return render_template("cold-acclimatization.html")

@app.route("/terrain-skirmisher-538899")
def Terrain_Skirmisher():
	return render_template("terrain-skirmisher-538899.html")

@app.route("/wilderness-survivor")
def Wilderness_Survivor():
	return render_template("wilderness-survivor.html")

@app.route("/environmental-stalker")
def Environmental_Stalker():
	return render_template("environmental-stalker.html")

@app.route("/uncanny-cheeks")
def Uncanny_Cheeks():
	return render_template("uncanny-cheeks.html")

@app.route("/hardy-traveler")
def Hardy_Traveler():
	return render_template("hardy-traveler.html")

@app.route("/scout")
def Scout():
	return render_template("scout.html")

@app.route("/inspirit-hazard")
def Inspirit_Hazard():
	return render_template("inspirit-hazard.html")

@app.route("/bounce-back")
def Bounce_Back():
	return render_template("bounce-back.html")

@app.route("/vivacious-conduit")
def Vivacious_Conduit():
	return render_template("vivacious-conduit.html")

@app.route("/ghost-hunter")
def Ghost_Hunter():
	return render_template("ghost-hunter.html")

@app.route("/spirit-strike")
def Spirit_Strike():
	return render_template("spirit-strike.html")

@app.route("/occult-resistance")
def Occult_Resistance():
	return render_template("occult-resistance.html")

@app.route("/steely-gaze")
def Steely_Gaze():
	return render_template("steely-gaze.html")

@app.route("/climbing-appendage")
def Climbing_Appendage():
	return render_template("climbing-appendage.html")

@app.route("/scavenger")
def Scavenger():
	return render_template("scavenger.html")

@app.route("/fluid-squeeze")
def Fluid_Squeeze():
	return render_template("fluid-squeeze.html")

@app.route("/powerful-claws")
def Powerful_Claws():
	return render_template("powerful-claws.html")

@app.route("/aggravating-scratch")
def Aggravating_Scratch():
	return render_template("aggravating-scratch.html")

@app.route("/accursed-claws")
def Accursed_Claws():
	return render_template("accursed-claws.html")

@app.route("/increased-consumption")
def Increased_Consumption():
	return render_template("increased-consumption.html")

@app.route("/slow-eater")
def Slow_Eater():
	return render_template("slow-eater.html")

@app.route("/dependents")
def Dependents():
	return render_template("dependents.html")

@app.route("/all-class-and-skill-feats")
def All_Class_and_Skill_Feats():
	return render_template("all-class-and-skill-feats.html")

@app.route("/long-lived-3256488")
def Long_Lived():
	return render_template("long-lived-3256488.html")

@app.route("/expert-rider")
def Expert_Rider():
	return render_template("expert-rider.html")

@app.route("/animal-allies")
def Animal_Allies():
	return render_template("animal-allies.html")

@app.route("/aquatic-ambusher")
def Aquatic_Ambusher():
	return render_template("aquatic-ambusher.html")

@app.route("/guided-by-the-stars")
def Guided_by_the_Stars():
	return render_template("guided-by-the-stars.html")

@app.route("/read-the-stars")
def Read_the_Stars():
	return render_template("read-the-stars.html")

@app.route("/heir-of-the-saoc")
def Heir_of_the_Saoc():
	return render_template("heir-of-the-saoc.html")

@app.route("/saoc-astrology")
def Saoc_Astrology():
	return render_template("saoc-astrology.html")

@app.route("/swim-speed")
def Swim_Speed():
	return render_template("swim-speed.html")

@app.route("/animal-order-elocutionist")
def Animal_Order_Elocutionist():
	return render_template("animal-order-elocutionist.html")

@app.route("/complications")
def Complications():
	return render_template("complications.html")

@app.route("/beastkin")
def Beastkin():
	return render_template("beastkin.html")

@app.route("/critter-shape")
def Critter_Shape():
	return render_template("critter-shape.html")

@app.route("/lifetime-climber")
def Lifetime_Climber():
	return render_template("lifetime-climber.html")

@app.route("/adept-climber")
def Adept_Climber():
	return render_template("adept-climber.html")

@app.route("/avenge-the-fallen")
def Avenge_the_Fallen():
	return render_template("avenge-the-fallen.html")

@app.route("/cant-fall-here")
def Cant_Fall_Here():
	return render_template("cant-fall-here.html")

@app.route("/call-of-elysium")
def Call_of_Elysium():
	return render_template("call-of-elysium.html")

@app.route("/mindfulness")
def Mindfulness():
	return render_template("mindfulness.html")

@app.route("/we-march-on")
def We_March_On():
	return render_template("we-march-on.html")

@app.route("/handy")
def Handy():
	return render_template("handy.html")

@app.route("/inventive-offensive")
def Inventive_Offensive():
	return render_template("inventive-offensive.html")

@app.route("/natural-charm")
def Natural_Charm():
	return render_template("natural-charm.html")

@app.route("/voice-modulation")
def Voice_Modulation():
	return render_template("voice-modulation.html")

@app.route("/bright-soul")
def Bright_Soul():
	return render_template("bright-soul.html")

@app.route("/chaotic-elemental-resistance")
def Chaotic_Elemental_Resistance():
	return render_template("chaotic-elemental-resistance.html")

@app.route("/elemental-bulwark")
def Elemental_Bulwark():
	return render_template("elemental-bulwark.html")

@app.route("/flame-jump")
def Flame_Jump():
	return render_template("flame-jump.html")

@app.route("/smoke-blending")
def Smoke_Blending():
	return render_template("smoke-blending.html")

@app.route("/invoke-the-elements")
def Invoke_the_Elements():
	return render_template("invoke-the-elements.html")

@app.route("/the-shroud")
def The_Shroud():
	return render_template("the-shroud.html")

@app.route("/tidal-shield")
def Tidal_Shield():
	return render_template("tidal-shield.html")

@app.route("/water-strider")
def Water_Strider():
	return render_template("water-strider.html")

@app.route("/breath-weapon")
def Breath_Weapon():
	return render_template("breath-weapon.html")

@app.route("/elemental-reprisal")
def Elemental_Reprisal():
	return render_template("elemental-reprisal.html")

@app.route("/elemental-assault")
def Elemental_Assault():
	return render_template("elemental-assault.html")

@app.route("/elemental-heart")
def Elemental_Heart():
	return render_template("elemental-heart.html")

@app.route("/guided-strike")
def Guided_Strike():
	return render_template("guided-strike.html")

@app.route("/radiant-burst")
def Radiant_Burst():
	return render_template("radiant-burst.html")

@app.route("/scorching-disarm")
def Scorching_Disarm():
	return render_template("scorching-disarm.html")

@app.route("/torcher")
def Torcher():
	return render_template("torcher.html")

@app.route("/palpable-enmity-6347319")
def Palpable_Enmity():
	return render_template("palpable-enmity-6347319.html")

@app.route("/cloud-gazer")
def Cloud_Gazer():
	return render_template("cloud-gazer.html")

@app.route("/street-dwellers")
def Street_Dwellers():
	return render_template("street-dwellers.html")

@app.route("/body-storage")
def Body_Storage():
	return render_template("body-storage.html")

@app.route("/hazard-expertise")
def Hazard_Expertise():
	return render_template("hazard-expertise.html")

@app.route("/wary-skulker")
def Wary_Skulker():
	return render_template("wary-skulker.html")

@app.route("/between-the-plates")
def Between_the_Plates():
	return render_template("between-the-plates.html")

@app.route("/cause-hesitation")
def Cause_Hesitation():
	return render_template("cause-hesitation.html")

@app.route("/cling")
def Cling():
	return render_template("cling.html")

@app.route("/cornered-fury")
def Cornered_Fury():
	return render_template("cornered-fury.html")

@app.route("/dashing-snatch")
def Dashing_Snatch():
	return render_template("dashing-snatch.html")

@app.route("/empathetic-plea")
def Empathetic_Plea():
	return render_template("empathetic-plea.html")

@app.route("/graceful-dance")
def Graceful_Dance():
	return render_template("graceful-dance.html")

@app.route("/grasping-reach")
def Grasping_Reach():
	return render_template("grasping-reach.html")

@app.route("/saving-throw-feats")
def Saving_Throw_Feats():
	return render_template("saving-throw-feats.html")

@app.route("/lifebloods-call")
def Lifebloods_Call():
	return render_template("lifebloods-call.html")

@app.route("/olethross-decree")
def Olethross_Decree():
	return render_template("olethross-decree.html")

@app.route("/tactical-reposition")
def Tactical_Reposition():
	return render_template("tactical-reposition.html")

@app.route("/sudden-hop")
def Sudden_Hop():
	return render_template("sudden-hop.html")

@app.route("/terrain-advantage")
def Terrain_Advantage():
	return render_template("terrain-advantage.html")

@app.route("/to-the-last")
def To_The_Last():
	return render_template("to-the-last.html")

@app.route("/cat-nap")
def Cat_Nap():
	return render_template("cat-nap.html")

@app.route("/ferocity")
def Ferocity():
	return render_template("ferocity.html")

@app.route("/robust-vitality")
def Robust_Vitality():
	return render_template("robust-vitality.html")

@app.route("/healing-factor")
def Healing_Factor():
	return render_template("healing-factor.html")

@app.route("/stoutness")
def Stoutness():
	return render_template("stoutness.html")

@app.route("/mystical-mending")
def Mystical_Mending():
	return render_template("mystical-mending.html")

@app.route("/nine-lives")
def Nine_Lives():
	return render_template("nine-lives.html")

@app.route("/spell-devourer")
def Spell_Devourer():
	return render_template("spell-devourer.html")

@app.route("/victorious-vigor")
def Victorious_Vigor():
	return render_template("victorious-vigor.html")

@app.route("/blessed-blood")
def Blessed_Blood():
	return render_template("blessed-blood.html")

@app.route("/magical-strikes")
def Magical_Strikes():
	return render_template("magical-strikes.html")

@app.route("/fiendish-strikes")
def Fiendish_Strikes():
	return render_template("fiendish-strikes.html")

@app.route("/enforced-order")
def Enforced_Order():
	return render_template("enforced-order.html")

@app.route("/celestial-strikes")
def Celestial_Strikes():
	return render_template("celestial-strikes.html")

@app.route("/halo")
def Halo():
	return render_template("halo.html")

@app.route("/radiate-glory")
def Radiate_Glory():
	return render_template("radiate-glory.html")

@app.route("/intimidating-mein")
def Intimidating_Mein():
	return render_template("intimidating-mein.html")

@app.route("/remorseless-lash")
def Remorseless_Lash():
	return render_template("remorseless-lash.html")

@app.route("/cultural-expertise")
def Cultural_Expertise():
	return render_template("cultural-expertise.html")

@app.route("/dynamic-skill")
def Dynamic_Skill():
	return render_template("dynamic-skill.html")

@app.route("/theoretical-acumen")
def Theoretical_Acumen():
	return render_template("theoretical-acumen.html")

@app.route("/clever-improvisor")
def Clever_Improvisor():
	return render_template("clever-improvisor.html")

@app.route("/chance-death")
def Chance_Death():
	return render_template("chance-death.html")

@app.route("/eat-fortune")
def Eat_Fortune():
	return render_template("eat-fortune.html")

@app.route("/impose-order")
def Impose_Order():
	return render_template("impose-order.html")

@app.route("/extremely-lucky")
def Extremely_Lucky():
	return render_template("extremely-lucky.html")

@app.route("/tradition-countermeasures")
def Tradition_Countermeasures():
	return render_template("tradition-countermeasures.html")

@app.route("/bouncy")
def Bouncy():
	return render_template("bouncy.html")

@app.route("/powerful-leaps")
def Powerful_Leaps():
	return render_template("powerful-leaps.html")

@app.route("/rock-and-roll")
def Rock_and_Roll():
	return render_template("rock-and-roll.html")

@app.route("/sure-feet")
def Sure_Feet():
	return render_template("sure-feet.html")

@app.route("/tumbler")
def Tumbler():
	return render_template("tumbler.html")

@app.route("/mutate-weapon")
def Mutate_Weapon():
	return render_template("mutate-weapon.html")

@app.route("/coating-of-slime")
def Coating_of_Slime():
	return render_template("coating-of-slime.html")

@app.route("/natural-weapon-cunning")
def Natural_Weapon_Cunning():
	return render_template("natural-weapon-cunning.html")

@app.route("/venom")
def Venom():
	return render_template("venom.html")

@app.route("/bite-attack")
def Bite_Attack():
	return render_template("bite-attack.html")

@app.route("/persistent-wounds")
def Persistent_Wounds():
	return render_template("persistent-wounds.html")

@app.route("/iron-fists")
def Iron_Fists():
	return render_template("iron-fists.html")

@app.route("/easy-dry")
def Easy_Dry():
	return render_template("easy-dry.html")

@app.route("/claws")
def Claws():
	return render_template("claws.html")

@app.route("/scooper")
def Scooper():
	return render_template("scooper.html")

@app.route("/observant")
def Observant():
	return render_template("observant.html")

@app.route("/aloofness")
def Aloofness():
	return render_template("aloofness.html")

@app.route("/ward-against-corruption")
def Ward_Against_Corruption():
	return render_template("ward-against-corruption.html")

@app.route("/grim-insight")
def Grim_Insight():
	return render_template("grim-insight.html")

@app.route("/evade-doom")
def Evade_Doom():
	return render_template("evade-doom.html")

@app.route("/stubborn-persistence")
def Stubborn_Persistence():
	return render_template("stubborn-persistence.html")

@app.route("/resilient-body")
def Resilient_Body():
	return render_template("resilient-body.html")

@app.route("/resist-persistent-damage")
def Resist_Persistent_Damage():
	return render_template("resist-persistent-damage.html")

@app.route("/common-resistance")
def Common_Resistance():
	return render_template("common-resistance.html")

@app.route("/uncommon-resistance")
def Uncommon_Resistance():
	return render_template("uncommon-resistance.html")

@app.route("/stone-bones")
def Stone_Bones():
	return render_template("stone-bones.html")

@app.route("/dragonscaled")
def Dragonscaled():
	return render_template("dragonscaled.html")

@app.route("/flexible-morality")
def Flexible_Morality():
	return render_template("flexible-morality.html")

@app.route("/blunt-snout")
def Blunt_Snout():
	return render_template("blunt-snout.html")

@app.route("/deaths-drums")
def Deaths_Drums():
	return render_template("deaths-drums.html")

@app.route("/child-of-light")
def Child_of_Light():
	return render_template("child-of-light.html")

@app.route("/death-warden")
def Death_Warden():
	return render_template("death-warden.html")

@app.route("/gutsy")
def Gutsy():
	return render_template("gutsy.html")

@app.route("/haughty-obstinacy")
def Haughty_Obstinacy():
	return render_template("haughty-obstinacy.html")

@app.route("/jinxed-5569781")
def Jinxed():
	return render_template("jinxed-5569781.html")

@app.route("/know-oneself")
def Know_Oneself():
	return render_template("know-oneself.html")

@app.route("/lab-rat")
def Lab_Rat():
	return render_template("lab-rat.html")

@app.route("/dreamer")
def Dreamer():
	return render_template("dreamer.html")

@app.route("/plumekin")
def Plumekin():
	return render_template("plumekin.html")

@app.route("/tide-hardened")
def Tide_Hardened():
	return render_template("tide-hardened.html")

@app.route("/augment-senses")
def Augment_Senses():
	return render_template("augment-senses.html")

@app.route("/bloodhound")
def Bloodhound():
	return render_template("bloodhound.html")

@app.route("/darkvision")
def Darkvision():
	return render_template("darkvision.html")

@app.route("/shadowsight")
def Shadowsight():
	return render_template("shadowsight.html")

@app.route("/whisper-kind")
def Whisper_kind():
	return render_template("whisper-kind.html")

@app.route("/spotting-as-one")
def Spotting_as_one():
	return render_template("spotting-as-one.html")

@app.route("/slip-into-the-shadow")
def Slip_Into_the_Shadow():
	return render_template("slip-into-the-shadow.html")

@app.route("/unexpected-shift")
def Unexpected_Shift():
	return render_template("unexpected-shift.html")

@app.route("/close-quarters")
def Close_Quarters():
	return render_template("close-quarters.html")

@app.route("/scamper-underfoot")
def Scamper_Underfoot():
	return render_template("scamper-underfoot.html")

@app.route("/dance-underfoot")
def Dance_Underfoot():
	return render_template("dance-underfoot.html")

@app.route("/tiny")
def Tiny():
	return render_template("tiny.html")

@app.route("/shifting-colors")
def Shifting_Colors():
	return render_template("shifting-colors.html")

@app.route("/folksy-patter")
def Folksy_Patter():
	return render_template("folksy-patter.html")

@app.route("/project-persona")
def Project_Persona():
	return render_template("project-persona.html")

@app.route("/surge")
def Surge():
	return render_template("surge.html")

@app.route("/photosynthesis")
def Photosynthesis():
	return render_template("photosynthesis.html")

@app.route("/distracting-song")
def Distracting_Song():
	return render_template("distracting-song.html")

@app.route("/catchy-tune")
def Catchy_Tune():
	return render_template("catchy-tune.html")

@app.route("/lightning-tongue")
def Lightning_Tongue():
	return render_template("lightning-tongue.html")

@app.route("/useful-bonus-appendage")
def Useful_Bonus_Appendage():
	return render_template("useful-bonus-appendage.html")

@app.route("/warmask")
def Warmask():
	return render_template("warmask.html")

@app.route("/ancestral-shieldbearer")
def Ancestral_Shieldbearer():
	return render_template("ancestral-shieldbearer.html")

@app.route("/clan-dagger")
def Clan_Dagger():
	return render_template("clan-dagger.html")

@app.route("/improvisational-warrior")
def Improvisational_Warrior():
	return render_template("improvisational-warrior.html")

@app.route("/leech-clipper")
def Leech_Clipper():
	return render_template("leech-clipper.html")

@app.route("/wings")
def Wings():
	return render_template("wings.html")

@app.route("/bomb-maker")
def Bomb_Maker():
	return render_template("bomb-maker.html")

@app.route("/splash-control")
def Splash_Control():
	return render_template("splash-control.html")

@app.route("/debilitating-bomb")
def Debilitating_Bomb():
	return render_template("debilitating-bomb.html")

@app.route("/far-lobber")
def Far_Lobber():
	return render_template("far-lobber.html")

@app.route("/artokuss-fire")
def Artokuss_Fire():
	return render_template("artokuss-fire.html")

@app.route("/combine-elixers")
def Combine_Elixers():
	return render_template("combine-elixers.html")

@app.route("/alchemical-healer")
def Alchemical_Healer():
	return render_template("alchemical-healer.html")

@app.route("/merciful-elixir")
def Merciful_Elixir():
	return render_template("merciful-elixir.html")

@app.route("/mutagenic-discovery")
def Mutagenic_Discovery():
	return render_template("mutagenic-discovery.html")

@app.route("/mutagenist")
def Mutagenist():
	return render_template("mutagenist.html")

@app.route("/chemical-contagion")
def Chemical_Contagion():
	return render_template("chemical-contagion.html")

@app.route("/poison-weapon")
def Poison_Weapon():
	return render_template("poison-weapon.html")

@app.route("/tenacious-toxins")
def Tenacious_Toxins():
	return render_template("tenacious-toxins.html")

@app.route("/toxicologist")
def Toxicologist():
	return render_template("toxicologist.html")

@app.route("/braggart-7341319")
def Braggart():
	return render_template("braggart-7341319.html")

@app.route("/inspired-methodology")
def Inspired_Methodology():
	return render_template("inspired-methodology.html")

@app.route("/upstage")
def Upstage():
	return render_template("upstage.html")

@app.route("/group-infiltration")
def Group_Infiltration():
	return render_template("group-infiltration.html")

@app.route("/liberator")
def Liberator():
	return render_template("liberator.html")

@app.route("/immediate-aid")
def Immediate_Aid():
	return render_template("immediate-aid.html")

@app.route("/cut-the-bonds")
def Cut_the_Bonds():
	return render_template("cut-the-bonds.html")

@app.route("/marshals-aura")
def Marshals_Aura():
	return render_template("marshals-aura.html")

@app.route("/cadence-call")
def Cadence_Call():
	return render_template("cadence-call.html")

@app.route("/steel-yourself")
def Steel_Yourself():
	return render_template("steel-yourself.html")

@app.route("/eidetic-memorization")
def Eidetic_Memorization():
	return render_template("eidetic-memorization.html")

@app.route("/efficient-rituals")
def Efficient_Rituals():
	return render_template("efficient-rituals.html")

@app.route("/charmed-life")
def Charmed_Life():
	return render_template("charmed-life.html")

@app.route("/quick-warning")
def Quick_Warning():
	return render_template("quick-warning.html")

@app.route("/deft-cooperation")
def Deft_Cooperation():
	return render_template("deft-cooperation.html")

@app.route("/focus-ally")
def Focus_Ally():
	return render_template("focus-ally.html")

@app.route("/watch-and-learn")
def Watch_and_Learn():
	return render_template("watch-and-learn.html")

@app.route("/absorb-spell")
def Absorb_Spell():
	return render_template("absorb-spell.html")

@app.route("/clever-counterspell")
def Clever_Counterspell():
	return render_template("clever-counterspell.html")

@app.route("/reflect-spell")
def Reflect_Spell():
	return render_template("reflect-spell.html")

@app.route("/physical-evolution")
def Physical_Evolution():
	return render_template("physical-evolution.html")

@app.route("/counterspell")
def Counterspell():
	return render_template("counterspell.html")

@app.route("/second-chance-enchantment")
def Second_Chance_Enchantment():
	return render_template("second-chance-enchantment.html")

@app.route("/enhanced-familiar")
def Enhanced_Familiar():
	return render_template("enhanced-familiar.html")

@app.route("/sneak-attack")
def Sneak_Attack():
	return render_template("sneak-attack.html")

@app.route("/warrior-tactic-feats")
def Warrior_Tactic_Feats():
	return render_template("warrior-tactic-feats.html")

@app.route("/impossible-striker")
def Impossible_Striker():
	return render_template("impossible-striker.html")

@app.route("/sly-striker")
def Sly_Striker():
	return render_template("sly-striker.html")

@app.route("/twist-the-knife")
def Twist_the_Knife():
	return render_template("twist-the-knife.html")

@app.route("/formation-training")
def Formation_Training():
	return render_template("formation-training.html")

@app.route("/legendary-performer")
def Legendary_Performer():
	return render_template("legendary-performer.html")

@app.route("/craft")
def Craft():
	return render_template("craft.html")

@app.route("/magic-item-rules")
def Magic_Item_Rules():
	return render_template("magic-item-rules.html")

@app.route("/sacrifice-armor")
def Sacrifice_Armor():
	return render_template("sacrifice-armor.html")

@app.route("/mark-for-death")
def Mark_For_Death():
	return render_template("mark-for-death.html")

@app.route("/second-skin")
def Second_Skin():
	return render_template("second-skin.html")

@app.route("/agile-maneuvers")
def Agile_Maneuvers():
	return render_template("agile-maneuvers.html")

@app.route("/barreling-charge")
def Barreling_Charge():
	return render_template("barreling-charge.html")

@app.route("/cleave")
def Cleave():
	return render_template("cleave.html")

@app.route("/dragging-strike")
def Dragging_Strike():
	return render_template("dragging-strike.html")

@app.route("/flat-footed")
def Flat_Footed():
	return render_template("flat-footed.html")

@app.route("/flanking")
def Flanking():
	return render_template("flanking.html")

@app.route("/grapple")
def Grapple():
	return render_template("grapple.html")

@app.route("/disarm")
def Disarm():
	return render_template("disarm.html")

@app.route("/trip")
def Trip():
	return render_template("trip.html")

@app.route("/shove")
def Shove():
	return render_template("shove.html")

@app.route("/mixed-maneuver")
def Mixed_Maneuver():
	return render_template("mixed-maneuver.html")

@app.route("/unbalancing-sweep")
def Unbalancing_Sweep():
	return render_template("unbalancing-sweep.html")

@app.route("/combat-flexibility")
def Combat_Flexibility():
	return render_template("combat-flexibility.html")

@app.route("/distracting-feint")
def Distracting_Feint():
	return render_template("distracting-feint.html")

@app.route("/thrash")
def Thrash():
	return render_template("thrash.html")

@app.route("/shatter-defenses")
def Shatter_Defenses():
	return render_template("shatter-defenses.html")

@app.route("/power-attack")
def Power_Attack():
	return render_template("power-attack.html")

@app.route("/attack-of-opportunity")
def Attack_of_Opportunity():
	return render_template("attack-of-opportunity.html")

@app.route("/deflect-arrow")
def Deflect_Arrow():
	return render_template("deflect-arrow.html")

@app.route("/opportune-riposte")
def Opportune_Riposte():
	return render_template("opportune-riposte.html")

@app.route("/preparation")
def Preparation():
	return render_template("preparation.html")

@app.route("/red-mantis-assassin")
def Red_Mantis_Assassin():
	return render_template("red-mantis-assassin.html")

@app.route("/knockback")
def Knockback():
	return render_template("knockback.html")

@app.route("/boasters-challenge")
def Boasters_Challenge():
	return render_template("boasters-challenge.html")

@app.route("/pin-to-the-spot")
def Pin_to_the_Spot():
	return render_template("pin-to-the-spot.html")

@app.route("/nimble-dodge")
def Nimble_Dodge():
	return render_template("nimble-dodge.html")

@app.route("/stance-savant")
def Stance_Savant():
	return render_template("stance-savant.html")

@app.route("/shoulder-catastrophe")
def Shoulder_Catastrophe():
	return render_template("shoulder-catastrophe.html")

@app.route("/knockdown")
def Knockdown():
	return render_template("knockdown.html")

@app.route("/warrior-general-feats")
def Warrior_General_Feats():
	return render_template("warrior-general-feats.html")

@app.route("/devise-a-strategem")
def Devise_a_Strategem():
	return render_template("devise-a-strategem.html")

@app.route("/accompany")
def Accompany():
	return render_template("accompany.html")

@app.route("/learning-epiphanies-and-experience-points")
def Learning_Epiphanies_and_Experience_Points():
	return render_template("learning-epiphanies-and-experience-points.html")

@app.route("/wound-thresholds-and-healing")
def Wound_Thresholds_and_Healing():
	return render_template("wound-thresholds-and-healing.html")

@app.route("/silencing-strike")
def Silencing_Strike():
	return render_template("silencing-strike.html")

@app.route("/divine-spells")
def Divine_Spells():
	return render_template("divine-spells.html")

@app.route("/greater-flurry")
def Greater_Flurry():
	return render_template("greater-flurry.html")

@app.route("/lava-soul")
def Lava_Soul():
	return render_template("lava-soul.html")

@app.route("/inveigle")
def Inveigle():
	return render_template("inveigle.html")

@app.route("/marked")
def Marked():
	return render_template("marked.html")

@app.route("/shattering-strike")
def Shattering_Strike():
	return render_template("shattering-strike.html")

@app.route("/elixir-of-life")
def Elixir_of_Life():
	return render_template("elixir-of-life.html")

@app.route("/alchemical-elixirs")
def Alchemical_Elixirs():
	return render_template("alchemical-elixirs.html")

@app.route("/lunacy")
def Lunacy():
	return render_template("lunacy.html")

@app.route("/hymn-of-healing")
def Hymn_of_Healing():
	return render_template("hymn-of-healing.html")

@app.route("/house-of-imaginary-walls")
def House_of_Imaginary_Walls():
	return render_template("house-of-imaginary-walls.html")

@app.route("/make-an-impression")
def Make_an_Impression():
	return render_template("make-an-impression.html")

@app.route("/diplomacy-chr")
def Diplomacy__CHR_():
	return render_template("diplomacy-chr.html")

@app.route("/intimidation-chr")
def Intimidation__CHR_():
	return render_template("intimidation-chr.html")

@app.route("/deception-chr")
def Deception__CHR_():
	return render_template("deception-chr.html")

@app.route("/magic-domain-mystic-beacon")
def Magic_Domain__Mystic_Beacon():
	return render_template("magic-domain-mystic-beacon.html")

@app.route("/dhampire")
def Dhampire():
	return render_template("dhampire.html")

@app.route("/regenerate")
def Regenerate():
	return render_template("regenerate.html")

@app.route("/advanced-alchemy")
def Advanced_Alchemy():
	return render_template("advanced-alchemy.html")

@app.route("/alchemist")
def Alchemist():
	return render_template("alchemist.html")

@app.route("/quick-alchemy")
def Quick_Alchemy():
	return render_template("quick-alchemy.html")

@app.route("/professional-feats")
def Professional_Feats():
	return render_template("professional-feats.html")

@app.route("/disturbing-defense")
def Disturbing_Defense():
	return render_template("disturbing-defense.html")

@app.route("/peculiar-anatomy")
def Peculiar_Anatomy():
	return render_template("peculiar-anatomy.html")

@app.route("/uncanny-suction")
def Uncanny_Suction():
	return render_template("uncanny-suction.html")

@app.route("/scroll-savant")
def Scroll_Savant():
	return render_template("scroll-savant.html")

@app.route("/new-cantrips")
def New_Cantrips():
	return render_template("new-cantrips.html")

@app.route("/equipment-list")
def Equipment_List():
	return render_template("equipment-list.html")

@app.route("/character-creation-guide")
def CHARACTER_CREATION_GUIDE():
	return render_template("character-creation-guide.html")

@app.route("/aapoph-serpentfolk")
def Aapoph_Serpentfolk():
	return render_template("aapoph-serpentfolk.html")

@app.route("/ankhrav")
def Ankhrav():
	return render_template("ankhrav.html")

@app.route("/simple-dcs-by-tier")
def Simple_DCs_by_Tier():
	return render_template("simple-dcs-by-tier.html")

@app.route("/dance-of-intercession")
def Dance_of_Intercession():
	return render_template("dance-of-intercession.html")

@app.route("/soothe")
def Soothe():
	return render_template("soothe.html")

@app.route("/incredible-companion")
def Incredible_Companion():
	return render_template("incredible-companion.html")

@app.route("/spellcasting")
def Spellcasting():
	return render_template("spellcasting.html")

@app.route("/necrophidius")
def Necrophidius():
	return render_template("necrophidius.html")

@app.route("/animated-statue")
def Animated_Statue():
	return render_template("animated-statue.html")

@app.route("/soulbound-doll")
def Soulbound_Doll():
	return render_template("soulbound-doll.html")

@app.route("/dig-widget")
def Dig_Widget():
	return render_template("dig-widget.html")

@app.route("/terra-cotta-soldier")
def Terra_Cotta_Soldier():
	return render_template("terra-cotta-soldier.html")

@app.route("/scarecrow-5701577")
def Scarecrow():
	return render_template("scarecrow-5701577.html")

@app.route("/giant-animated-statue")
def Giant_Animated_Statue():
	return render_template("giant-animated-statue.html")

@app.route("/levaloch")
def Levaloch():
	return render_template("levaloch.html")

@app.route("/tupilaq")
def Tupilaq():
	return render_template("tupilaq.html")

@app.route("/animated-furnace")
def Animated_Furnace():
	return render_template("animated-furnace.html")

@app.route("/swordkeeper")
def Swordkeeper():
	return render_template("swordkeeper.html")

@app.route("/spiral-centurian")
def Spiral_Centurian():
	return render_template("spiral-centurian.html")

@app.route("/frost-drake")
def Frost_Drake():
	return render_template("frost-drake.html")

@app.route("/desert-drake")
def Desert_Drake():
	return render_template("desert-drake.html")

@app.route("/young-copper-dragon")
def Young_Copper_Dragon():
	return render_template("young-copper-dragon.html")

@app.route("/young-red-dragon")
def Young_Red_Dragon():
	return render_template("young-red-dragon.html")

@app.route("/young-blue-dragon")
def Young_Blue_Dragon():
	return render_template("young-blue-dragon.html")

@app.route("/summon-animal")
def Summon_Animal():
	return render_template("summon-animal.html")

@app.route("/reincarnate")
def Reincarnate():
	return render_template("reincarnate.html")

@app.route("/skeleton-archer")
def Skeleton_Archer():
	return render_template("skeleton-archer.html")

@app.route("/drain-bonded-item")
def Drain_Bonded_Item():
	return render_template("drain-bonded-item.html")

@app.route("/soul-domain-eject-soul")
def Soul_Domain__Eject_Soul():
	return render_template("soul-domain-eject-soul.html")

@app.route("/mature-animal-companion")
def Mature_Animal_Companion():
	return render_template("mature-animal-companion.html")

@app.route("/perception")
def Perception():
	return render_template("perception.html")

@app.route("/athletics-v2")
def Athletics__v2_():
	return render_template("athletics-v2.html")

@app.route("/might-v2")
def Might__v2_():
	return render_template("might-v2.html")

@app.route("/coordination-v2")
def Coordination__V2_():
	return render_template("coordination-v2.html")

@app.route("/reconstruct-the-scene-3367166")
def Reconstruct_the_Scene():
	return render_template("reconstruct-the-scene-3367166.html")

@app.route("/discover-motivations")
def Discover_Motivations():
	return render_template("discover-motivations.html")

@app.route("/empathy-v2")
def Empathy__V2_():
	return render_template("empathy-v2.html")

@app.route("/the-quality-spectrum")
def The_Quality_Spectrum():
	return render_template("the-quality-spectrum.html")

@app.route("/perform")
def Perform():
	return render_template("perform.html")

@app.route("/create-artwork")
def Create_Artwork():
	return render_template("create-artwork.html")

@app.route("/the-rock")
def The_Rock():
	return render_template("the-rock.html")

@app.route("/alchemy-abilities")
def Alchemy_Abilities():
	return render_template("alchemy-abilities.html")

@app.route("/monster-npc-rules")
def Monster___NPC_Rules():
	return render_template("monster-npc-rules.html")

@app.route("/magic-and-spellcasting")
def Magic_and_Spellcasting():
	return render_template("magic-and-spellcasting.html")

@app.route("/social-interaction")
def Social_Interaction():
	return render_template("social-interaction.html")

@app.route("/armor-and-weapon-design")
def Armor_and_Weapon_Design():
	return render_template("armor-and-weapon-design.html")

@app.route("/tiefling-fighter")
def Tiefling_Fighter():
	return render_template("tiefling-fighter.html")

@app.route("/alchemy")
def Alchemy():
	return render_template("alchemy.html")

@app.route("/dwarf-rogue")
def Dwarf_Rogue():
	return render_template("dwarf-rogue.html")

@app.route("/persuade")
def Persuade():
	return render_template("persuade.html")

@app.route("/rogue-abilities")
def Rogue_Abilities():
	return render_template("rogue-abilities.html")

@app.route("/halfling-wizard")
def Halfling_Wizard():
	return render_template("halfling-wizard.html")

@app.route("/range-duration-and-area")
def Range_Duration_and_Area():
	return render_template("range-duration-and-area.html")

@app.route("/boosts")
def Boosts():
	return render_template("boosts.html")

@app.route("/enhanced-activity-use")
def Enhanced_Activity_Use():
	return render_template("enhanced-activity-use.html")

@app.route("/action-savers")
def Action_Savers():
	return render_template("action-savers.html")

@app.route("/special-defenses")
def Special_Defenses():
	return render_template("special-defenses.html")

@app.route("/limits")
def Limits():
	return render_template("limits.html")

@app.route("/the-situational-limit")
def The_Situational_Limit():
	return render_template("the-situational-limit.html")

@app.route("/special-attack")
def Special_Attack():
	return render_template("special-attack.html")

@app.route("/defense-checks-and-condition-resistance")
def Defense_Checks_and_Condition_Resistance():
	return render_template("defense-checks-and-condition-resistance.html")

@app.route("/healing-and-dying")
def Healing_and_Dying():
	return render_template("healing-and-dying.html")

@app.route("/other-combat-benefits")
def Other_Combat_Benefits():
	return render_template("other-combat-benefits.html")

@app.route("/movement-7447550")
def Movement():
	return render_template("movement-7447550.html")

@app.route("/senses-and-perception")
def Senses_and_Perception():
	return render_template("senses-and-perception.html")

@app.route("/exploration-4164893")
def Exploration():
	return render_template("exploration-4164893.html")

@app.route("/investigation-and-information")
def Investigation_and_Information():
	return render_template("investigation-and-information.html")

@app.route("/teamwork")
def Teamwork():
	return render_template("teamwork.html")

@app.route("/communication")
def Communication():
	return render_template("communication.html")

@app.route("/survival")
def Survival():
	return render_template("survival.html")

@app.route("/spellcasting-abilities")
def Spellcasting_Abilities():
	return render_template("spellcasting-abilities.html")

@app.route("/community-and-society")
def Community_and_Society():
	return render_template("community-and-society.html")

@app.route("/equipment")
def Equipment():
	return render_template("equipment.html")

@app.route("/creating-abilities")
def Creating_Abilities():
	return render_template("creating-abilities.html")

@app.route("/clandestine-and-rogue")
def Clandestine_and_Rogue():
	return render_template("clandestine-and-rogue.html")

@app.route("/skills")
def Skills():
	return render_template("skills.html")

@app.route("/stealth-and-hiding")
def Stealth_and_Hiding():
	return render_template("stealth-and-hiding.html")

@app.route("/traps-and-hazards")
def Traps_and_Hazards():
	return render_template("traps-and-hazards.html")

@app.route("/alter-material")
def Alter_Material():
	return render_template("alter-material.html")

@app.route("/creation-9164590")
def Creation():
	return render_template("creation-9164590.html")

@app.route("/destroy-material")
def Destroy_Material():
	return render_template("destroy-material.html")

@app.route("/environmental-control")
def Environmental_Control():
	return render_template("environmental-control.html")

@app.route("/illusions")
def Illusions():
	return render_template("illusions.html")

@app.route("/meta-abilities")
def Meta_Abilities():
	return render_template("meta-abilities.html")

@app.route("/minions")
def Minions():
	return render_template("minions.html")

@app.route("/animal-friends-and-mounts")
def Animal_Friends_and_Mounts():
	return render_template("animal-friends-and-mounts.html")

@app.route("/shapeshifting")
def Shapeshifting():
	return render_template("shapeshifting.html")

@app.route("/size")
def Size():
	return render_template("size.html")

@app.route("/arrange-a-meeting")
def Arrange_a_Meeting():
	return render_template("arrange-a-meeting.html")

@app.route("/administration")
def Administration():
	return render_template("administration.html")

@app.route("/navigate-unsecured-system")
def Navigate_Unsecured_System():
	return render_template("navigate-unsecured-system.html")

@app.route("/create-electronic-forgery")
def Create_Electronic_Forgery():
	return render_template("create-electronic-forgery.html")

@app.route("/infiltrate-secure-system")
def Infiltrate_Secure_System():
	return render_template("infiltrate-secure-system.html")

@app.route("/avoid-system-detection")
def Avoid_System_Detection():
	return render_template("avoid-system-detection.html")

@app.route("/bypass-countermeasures")
def Bypass_Countermeasures():
	return render_template("bypass-countermeasures.html")

@app.route("/computers")
def Computers():
	return render_template("computers.html")

@app.route("/culture")
def Culture():
	return render_template("culture.html")

@app.route("/configure-explosives")
def Configure_Explosives():
	return render_template("configure-explosives.html")

@app.route("/assess-structures")
def Assess_Structures():
	return render_template("assess-structures.html")

@app.route("/disable-device")
def Disable_Device():
	return render_template("disable-device.html")

@app.route("/identify-technology")
def Identify_Technology():
	return render_template("identify-technology.html")

@app.route("/identify-magic")
def Identify_Magic():
	return render_template("identify-magic.html")

@app.route("/repair")
def Repair():
	return render_template("repair.html")

@app.route("/jury-rig")
def Jury_Rig():
	return render_template("jury-rig.html")

@app.route("/engineering")
def Engineering():
	return render_template("engineering.html")

@app.route("/arcana")
def Arcana():
	return render_template("arcana.html")

@app.route("/connect-the-dots-4949769")
def Connect_the_Dots():
	return render_template("connect-the-dots-4949769.html")

@app.route("/examine-clue")
def Examine_Clue():
	return render_template("examine-clue.html")

@app.route("/investigation-v2")
def Investigation__V2_():
	return render_template("investigation-v2.html")

@app.route("/life-sciences")
def Life_Sciences():
	return render_template("life-sciences.html")

@app.route("/physical-sciences")
def Physical_Sciences():
	return render_template("physical-sciences.html")

@app.route("/piloting")
def Piloting():
	return render_template("piloting.html")

@app.route("/streetwise-6073864")
def Streetwise():
	return render_template("streetwise-6073864.html")

@app.route("/v2-character-creation")
def V2_Character_Creation():
	return render_template("v2-character-creation.html")

@app.route("/animal-companions")
def Animal_Companions():
	return render_template("animal-companions.html")

@app.route("/rallying-cry")
def Rallying_Cry():
	return render_template("rallying-cry.html")

@app.route("/persistent-alchemy")
def Persistent_Alchemy():
	return render_template("persistent-alchemy.html")

@app.route("/extend-elixir")
def Extend_Elixir():
	return render_template("extend-elixir.html")

@app.route("/administer-first-aid-8413834")
def Administer_First_Aid():
	return render_template("administer-first-aid-8413834.html")

@app.route("/alchemist-class-feats")
def Alchemist_Class_Feats():
	return render_template("alchemist-class-feats.html")

@app.route("/reckless-abandon")
def Reckless_Abandon():
	return render_template("reckless-abandon.html")

@app.route("/all-ancestry-feats")
def All_Ancestry_Feats():
	return render_template("all-ancestry-feats.html")

@app.route("/word-of-recall")
def Word_of_Recall():
	return render_template("word-of-recall.html")

@app.route("/selective-energy")
def Selective_Energy():
	return render_template("selective-energy.html")

@app.route("/spellcaster-feats")
def Spellcaster_Feats():
	return render_template("spellcaster-feats.html")

@app.route("/breath-of-life")
def Breath_of_Life():
	return render_template("breath-of-life.html")

@app.route("/sacred-defense")
def Sacred_Defense():
	return render_template("sacred-defense.html")

