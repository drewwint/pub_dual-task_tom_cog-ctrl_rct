/***************************** 
 * Full_Dual-Task_Ctrl3 Test *
 *****************************/


// store info about the experiment session:
let expName = 'full_dual-task_ctrl3';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'Phone number last five*': '',
    'Email*': '',
};

// Start code blocks for 'Before Experiment'
// Run 'Before Experiment' code from prac_ssst_iti_draw
msg = "do!";

// Run 'Before Experiment' code from prac_tom_code
msg = "do!";

// Run 'Before Experiment' code from code
msg = "do!";

// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([(- 1.0), (- 1.0), (- 1.0)]),
  units: 'height',
  waitBlanking: true
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); }, flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(welcomeRoutineBegin());
flowScheduler.add(welcomeRoutineEachFrame());
flowScheduler.add(welcomeRoutineEnd());
flowScheduler.add(ssst_prac_instRoutineBegin());
flowScheduler.add(ssst_prac_instRoutineEachFrame());
flowScheduler.add(ssst_prac_instRoutineEnd());
const prac_ssstLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_ssstLoopBegin(prac_ssstLoopScheduler));
flowScheduler.add(prac_ssstLoopScheduler);
flowScheduler.add(prac_ssstLoopEnd);
flowScheduler.add(prac_tom_instRoutineBegin());
flowScheduler.add(prac_tom_instRoutineEachFrame());
flowScheduler.add(prac_tom_instRoutineEnd());
const prac_tomLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_tomLoopBegin(prac_tomLoopScheduler));
flowScheduler.add(prac_tomLoopScheduler);
flowScheduler.add(prac_tomLoopEnd);
flowScheduler.add(prac_dual_instRoutineBegin());
flowScheduler.add(prac_dual_instRoutineEachFrame());
flowScheduler.add(prac_dual_instRoutineEnd());
const prac_dualLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(prac_dualLoopBegin(prac_dualLoopScheduler));
flowScheduler.add(prac_dualLoopScheduler);
flowScheduler.add(prac_dualLoopEnd);
flowScheduler.add(real_task_instRoutineBegin());
flowScheduler.add(real_task_instRoutineEachFrame());
flowScheduler.add(real_task_instRoutineEnd());
const tom_blockLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(tom_blockLoopBegin(tom_blockLoopScheduler));
flowScheduler.add(tom_blockLoopScheduler);
flowScheduler.add(tom_blockLoopEnd);
flowScheduler.add(restRoutineBegin());
flowScheduler.add(restRoutineEachFrame());
flowScheduler.add(restRoutineEnd());
const dual_blockLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(dual_blockLoopBegin(dual_blockLoopScheduler));
flowScheduler.add(dual_blockLoopScheduler);
flowScheduler.add(dual_blockLoopEnd);
flowScheduler.add(outroRoutineBegin());
flowScheduler.add(outroRoutineEachFrame());
flowScheduler.add(outroRoutineEnd());
flowScheduler.add(quitPsychoJS, '', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, '', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    {'name': 'stimuli/PC10_2_Fixed.png', 'path': 'stimuli/PC10_2_Fixed.png'},
    {'name': 'stimuli/CT6_dec.png', 'path': 'stimuli/CT6_dec.png'},
    {'name': 'stimuli/CT1_3_Fixed.png', 'path': 'stimuli/CT1_3_Fixed.png'},
    {'name': 'stimuli/ssst_ignore.png', 'path': 'stimuli/ssst_ignore.png'},
    {'name': 'stimuli/PC7_2_Fixed.png', 'path': 'stimuli/PC7_2_Fixed.png'},
    {'name': 'practice_stimuli/CT_example_2.png', 'path': 'practice_stimuli/CT_example_2.png'},
    {'name': 'stimuli/CT5_1_Fixed.png', 'path': 'stimuli/CT5_1_Fixed.png'},
    {'name': 'stimuli/AT3_dec.png', 'path': 'stimuli/AT3_dec.png'},
    {'name': 'stimuli/CT6_1_Fixed.png', 'path': 'stimuli/CT6_1_Fixed.png'},
    {'name': 'stimuli/AT7_2_Fixed.png', 'path': 'stimuli/AT7_2_Fixed.png'},
    {'name': 'stimuli/CT1_1_Fixed.png', 'path': 'stimuli/CT1_1_Fixed.png'},
    {'name': 'stimuli/CT10_dec.png', 'path': 'stimuli/CT10_dec.png'},
    {'name': 'stimuli/AT6_3_Fixed.png', 'path': 'stimuli/AT6_3_Fixed.png'},
    {'name': 'stimuli/PC10_dec.png', 'path': 'stimuli/PC10_dec.png'},
    {'name': 'stimuli/AT7_dec.png', 'path': 'stimuli/AT7_dec.png'},
    {'name': 'stimuli/PC9_3_Fixed.png', 'path': 'stimuli/PC9_3_Fixed.png'},
    {'name': 'stimuli/AT4_1_Fixed.png', 'path': 'stimuli/AT4_1_Fixed.png'},
    {'name': 'stimuli/CT7_2_Fixed.png', 'path': 'stimuli/CT7_2_Fixed.png'},
    {'name': 'stimuli/AT2_2_Fixed.png', 'path': 'stimuli/AT2_2_Fixed.png'},
    {'name': 'stimuli/AT3_1_Fixed.png', 'path': 'stimuli/AT3_1_Fixed.png'},
    {'name': 'stimuli/PC6_2_Fixed.png', 'path': 'stimuli/PC6_2_Fixed.png'},
    {'name': 'stimuli/PC6_dec.png', 'path': 'stimuli/PC6_dec.png'},
    {'name': 'stimuli/PC6_3_Fixed.png', 'path': 'stimuli/PC6_3_Fixed.png'},
    {'name': 'stimuli/AT1_3_Fixed.png', 'path': 'stimuli/AT1_3_Fixed.png'},
    {'name': 'stimuli/AT5_dec.png', 'path': 'stimuli/AT5_dec.png'},
    {'name': 'stimuli/PC4_2_Fixed.png', 'path': 'stimuli/PC4_2_Fixed.png'},
    {'name': 'stimuli/PC2_3_Fixed.png', 'path': 'stimuli/PC2_3_Fixed.png'},
    {'name': 'stimuli/ssst_go_arrow.png', 'path': 'stimuli/ssst_go_arrow.png'},
    {'name': 'stimuli/AT2_3_Fixed.png', 'path': 'stimuli/AT2_3_Fixed.png'},
    {'name': 'stimuli/CT2_2_Fixed.png', 'path': 'stimuli/CT2_2_Fixed.png'},
    {'name': 'stimuli/PC3_3_Fixed.png', 'path': 'stimuli/PC3_3_Fixed.png'},
    {'name': 'stimuli/CT7_dec.png', 'path': 'stimuli/CT7_dec.png'},
    {'name': 'stimuli/PC5_2_Fixed.png', 'path': 'stimuli/PC5_2_Fixed.png'},
    {'name': 'stimuli/PC8_dec.png', 'path': 'stimuli/PC8_dec.png'},
    {'name': 'stimuli/AT10_1_Fixed.png', 'path': 'stimuli/AT10_1_Fixed.png'},
    {'name': 'stimuli/PC10_3_Fixed.png', 'path': 'stimuli/PC10_3_Fixed.png'},
    {'name': 'stimuli/CT8_dec.png', 'path': 'stimuli/CT8_dec.png'},
    {'name': 'stimuli/PC8_3_Fixed.png', 'path': 'stimuli/PC8_3_Fixed.png'},
    {'name': 'stimuli/AT1_1_Fixed.png', 'path': 'stimuli/AT1_1_Fixed.png'},
    {'name': 'stimuli/AT7_1_Fixed.png', 'path': 'stimuli/AT7_1_Fixed.png'},
    {'name': 'practice_stimuli/PC_example_2.png', 'path': 'practice_stimuli/PC_example_2.png'},
    {'name': 'stimuli/CT6_2_Fixed.png', 'path': 'stimuli/CT6_2_Fixed.png'},
    {'name': 'stimuli/AT4_2_Fixed.png', 'path': 'stimuli/AT4_2_Fixed.png'},
    {'name': 'stimuli/AT8_dec.png', 'path': 'stimuli/AT8_dec.png'},
    {'name': 'stimuli/PC2_2_Fixed.png', 'path': 'stimuli/PC2_2_Fixed.png'},
    {'name': 'stimuli/AT9_2_Fixed.png', 'path': 'stimuli/AT9_2_Fixed.png'},
    {'name': 'stimuli/CT3_2_Fixed.png', 'path': 'stimuli/CT3_2_Fixed.png'},
    {'name': 'stimuli/CT2_3_Fixed.png', 'path': 'stimuli/CT2_3_Fixed.png'},
    {'name': 'practice_stimuli/AT_example_1.png', 'path': 'practice_stimuli/AT_example_1.png'},
    {'name': 'stimuli/CT2_1_Fixed.png', 'path': 'stimuli/CT2_1_Fixed.png'},
    {'name': 'stimuli/AT8_2_Fixed.png', 'path': 'stimuli/AT8_2_Fixed.png'},
    {'name': 'stimuli/CT9_1_Fixed.png', 'path': 'stimuli/CT9_1_Fixed.png'},
    {'name': 'stimuli/PC3_dec.png', 'path': 'stimuli/PC3_dec.png'},
    {'name': 'stimuli/AT10_2_Fixed.png', 'path': 'stimuli/AT10_2_Fixed.png'},
    {'name': 'stimuli/AT3_3_Fixed.png', 'path': 'stimuli/AT3_3_Fixed.png'},
    {'name': 'conditions/tom_cond.xlsx', 'path': 'conditions/tom_cond.xlsx'},
    {'name': 'stimuli/PC6_1_Fixed.png', 'path': 'stimuli/PC6_1_Fixed.png'},
    {'name': 'stimuli/PC1_1_Fixed.png', 'path': 'stimuli/PC1_1_Fixed.png'},
    {'name': 'stimuli/AT5_1_Fixed.png', 'path': 'stimuli/AT5_1_Fixed.png'},
    {'name': 'stimuli/CT4_3_Fixed.png', 'path': 'stimuli/CT4_3_Fixed.png'},
    {'name': 'stimuli/PC5_3_Fixed.png', 'path': 'stimuli/PC5_3_Fixed.png'},
    {'name': 'stimuli/CT3_3_Fixed.png', 'path': 'stimuli/CT3_3_Fixed.png'},
    {'name': 'stimuli/CT4_1_Fixed.png', 'path': 'stimuli/CT4_1_Fixed.png'},
    {'name': 'stimuli/CT8_2_Fixed.png', 'path': 'stimuli/CT8_2_Fixed.png'},
    {'name': 'stimuli/CT1_dec.png', 'path': 'stimuli/CT1_dec.png'},
    {'name': 'stimuli/CT5_3_Fixed.png', 'path': 'stimuli/CT5_3_Fixed.png'},
    {'name': 'stimuli/AT1_dec.png', 'path': 'stimuli/AT1_dec.png'},
    {'name': 'practice_stimuli/PC_example_3.png', 'path': 'practice_stimuli/PC_example_3.png'},
    {'name': 'practice_stimuli/AT_example_dec.png', 'path': 'practice_stimuli/AT_example_dec.png'},
    {'name': 'stimuli/AT6_1_Fixed.png', 'path': 'stimuli/AT6_1_Fixed.png'},
    {'name': 'stimuli/AT4_dec.png', 'path': 'stimuli/AT4_dec.png'},
    {'name': 'stimuli/CT5_2_Fixed.png', 'path': 'stimuli/CT5_2_Fixed.png'},
    {'name': 'stimuli/AT2_1_Fixed.png', 'path': 'stimuli/AT2_1_Fixed.png'},
    {'name': 'stimuli/AT3_2_Fixed.png', 'path': 'stimuli/AT3_2_Fixed.png'},
    {'name': 'stimuli/AT8_3_Fixed.png', 'path': 'stimuli/AT8_3_Fixed.png'},
    {'name': 'stimuli/PC5_1_Fixed.png', 'path': 'stimuli/PC5_1_Fixed.png'},
    {'name': 'practice_stimuli/AT_example_3.png', 'path': 'practice_stimuli/AT_example_3.png'},
    {'name': 'stimuli/PC1_3_Fixed.png', 'path': 'stimuli/PC1_3_Fixed.png'},
    {'name': 'stimuli/AT9_3_Fixed.png', 'path': 'stimuli/AT9_3_Fixed.png'},
    {'name': 'practice_stimuli/inst_tom.png', 'path': 'practice_stimuli/inst_tom.png'},
    {'name': 'stimuli/PC5_dec.png', 'path': 'stimuli/PC5_dec.png'},
    {'name': 'stimuli/AT8_1_Fixed.png', 'path': 'stimuli/AT8_1_Fixed.png'},
    {'name': 'stimuli/AT1_2_Fixed.png', 'path': 'stimuli/AT1_2_Fixed.png'},
    {'name': 'practice_stimuli/PC_example_dec.png', 'path': 'practice_stimuli/PC_example_dec.png'},
    {'name': 'practice_stimuli/CT_example_dec.png', 'path': 'practice_stimuli/CT_example_dec.png'},
    {'name': 'stimuli/CT8_3_Fixed.png', 'path': 'stimuli/CT8_3_Fixed.png'},
    {'name': 'stimuli/PC7_1_Fixed.png', 'path': 'stimuli/PC7_1_Fixed.png'},
    {'name': 'stimuli/CT8_1_Fixed.png', 'path': 'stimuli/CT8_1_Fixed.png'},
    {'name': 'stimuli/AT5_3_Fixed.png', 'path': 'stimuli/AT5_3_Fixed.png'},
    {'name': 'stimuli/PC4_1_Fixed.png', 'path': 'stimuli/PC4_1_Fixed.png'},
    {'name': 'stimuli/CT10_2_Fixed.png', 'path': 'stimuli/CT10_2_Fixed.png'},
    {'name': 'conditions/prac_tom_cond.xlsx', 'path': 'conditions/prac_tom_cond.xlsx'},
    {'name': 'stimuli/PC9_2_Fixed.png', 'path': 'stimuli/PC9_2_Fixed.png'},
    {'name': 'practice_stimuli/CT_example_3.png', 'path': 'practice_stimuli/CT_example_3.png'},
    {'name': 'stimuli/AT10_3_Fixed.png', 'path': 'stimuli/AT10_3_Fixed.png'},
    {'name': 'stimuli/PC4_3_Fixed.png', 'path': 'stimuli/PC4_3_Fixed.png'},
    {'name': 'stimuli/CT6_3_Fixed.png', 'path': 'stimuli/CT6_3_Fixed.png'},
    {'name': 'stimuli/AT7_3_Fixed.png', 'path': 'stimuli/AT7_3_Fixed.png'},
    {'name': 'stimuli/PC4_dec.png', 'path': 'stimuli/PC4_dec.png'},
    {'name': 'stimuli/CT3_1_Fixed.png', 'path': 'stimuli/CT3_1_Fixed.png'},
    {'name': 'stimuli/PC2_dec.png', 'path': 'stimuli/PC2_dec.png'},
    {'name': 'stimuli/PC7_3_Fixed.png', 'path': 'stimuli/PC7_3_Fixed.png'},
    {'name': 'stimuli/CT7_3_Fixed.png', 'path': 'stimuli/CT7_3_Fixed.png'},
    {'name': 'stimuli/AT2_dec.png', 'path': 'stimuli/AT2_dec.png'},
    {'name': 'stimuli/CT7_1_Fixed.png', 'path': 'stimuli/CT7_1_Fixed.png'},
    {'name': 'stimuli/CT9_2_Fixed.png', 'path': 'stimuli/CT9_2_Fixed.png'},
    {'name': 'stimuli/AT5_2_Fixed.png', 'path': 'stimuli/AT5_2_Fixed.png'},
    {'name': 'stimuli/AT9_1_Fixed.png', 'path': 'stimuli/AT9_1_Fixed.png'},
    {'name': 'stimuli/PC1_dec.png', 'path': 'stimuli/PC1_dec.png'},
    {'name': 'practice_stimuli/inst_ssst_ctrl.png', 'path': 'practice_stimuli/inst_ssst_ctrl.png'},
    {'name': 'stimuli/ssst_cross.png', 'path': 'stimuli/ssst_cross.png'},
    {'name': 'practice_stimuli/CT_example_1.png', 'path': 'practice_stimuli/CT_example_1.png'},
    {'name': 'stimuli/AT6_2_Fixed.png', 'path': 'stimuli/AT6_2_Fixed.png'},
    {'name': 'stimuli/PC8_1_Fixed.png', 'path': 'stimuli/PC8_1_Fixed.png'},
    {'name': 'stimuli/CT9_3_Fixed.png', 'path': 'stimuli/CT9_3_Fixed.png'},
    {'name': 'stimuli/CT4_dec.png', 'path': 'stimuli/CT4_dec.png'},
    {'name': 'stimuli/CT9_dec.png', 'path': 'stimuli/CT9_dec.png'},
    {'name': 'practice_stimuli/PC_example_1.png', 'path': 'practice_stimuli/PC_example_1.png'},
    {'name': 'stimuli/AT6_dec.png', 'path': 'stimuli/AT6_dec.png'},
    {'name': 'stimuli/CT5_dec.png', 'path': 'stimuli/CT5_dec.png'},
    {'name': 'stimuli/CT4_2_Fixed.png', 'path': 'stimuli/CT4_2_Fixed.png'},
    {'name': 'conditions/prac_dual_tom_cond.xlsx', 'path': 'conditions/prac_dual_tom_cond.xlsx'},
    {'name': 'stimuli/CT1_2_Fixed.png', 'path': 'stimuli/CT1_2_Fixed.png'},
    {'name': 'stimuli/CT10_1_Fixed.png', 'path': 'stimuli/CT10_1_Fixed.png'},
    {'name': 'practice_stimuli/inst_dual-task_ctrl.png', 'path': 'practice_stimuli/inst_dual-task_ctrl.png'},
    {'name': 'stimuli/PC2_1_Fixed.png', 'path': 'stimuli/PC2_1_Fixed.png'},
    {'name': 'stimuli/AT10_dec.png', 'path': 'stimuli/AT10_dec.png'},
    {'name': 'conditions/ssst_go_stop.xlsx', 'path': 'conditions/ssst_go_stop.xlsx'},
    {'name': 'stimuli/AT4_3_Fixed.png', 'path': 'stimuli/AT4_3_Fixed.png'},
    {'name': 'stimuli/PC3_2_Fixed.png', 'path': 'stimuli/PC3_2_Fixed.png'},
    {'name': 'stimuli/AT9_dec.png', 'path': 'stimuli/AT9_dec.png'},
    {'name': 'stimuli/PC1_2_Fixed.png', 'path': 'stimuli/PC1_2_Fixed.png'},
    {'name': 'stimuli/PC9_dec.png', 'path': 'stimuli/PC9_dec.png'},
    {'name': 'stimuli/CT3_dec.png', 'path': 'stimuli/CT3_dec.png'},
    {'name': 'stimuli/PC10_1_Fixed.png', 'path': 'stimuli/PC10_1_Fixed.png'},
    {'name': 'stimuli/PC8_2_Fixed.png', 'path': 'stimuli/PC8_2_Fixed.png'},
    {'name': 'stimuli/CT2_dec.png', 'path': 'stimuli/CT2_dec.png'},
    {'name': 'stimuli/CT10_3_Fixed.png', 'path': 'stimuli/CT10_3_Fixed.png'},
    {'name': 'stimuli/PC7_dec.png', 'path': 'stimuli/PC7_dec.png'},
    {'name': 'stimuli/PC9_1_Fixed.png', 'path': 'stimuli/PC9_1_Fixed.png'},
    {'name': 'stimuli/ssst_stop.png', 'path': 'stimuli/ssst_stop.png'},
    {'name': 'practice_stimuli/AT_example_2.png', 'path': 'practice_stimuli/AT_example_2.png'},
    {'name': 'stimuli/PC3_1_Fixed.png', 'path': 'stimuli/PC3_1_Fixed.png'}
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.EXP);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2022.2.4';
  expInfo['OS'] = window.navigator.platform;

  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);

  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  psychoJS.setRedirectUrls(('https://cualienartifactstask.azurewebsites.net?ID=' + expInfo['participant']), '');

  return Scheduler.Event.NEXT;
}


var welcomeClock;
var text;
var welcome_adv;
var ssst_prac_instClock;
var ssst_inst1;
var ssst_inst2;
var ssst_inst3;
var ssst_inst5;
var ssst_inst6;
var key_resp;
var prac_ssst_trialClock;
var ssd_prac;
var stepsize;
var minval;
var maxval;
var prac_ssst_go;
var prac_ssst_stop;
var prac_ssst_resp;
var prac_ssst_itiClock;
var prac_ssst_iti_cross;
var prac_tom_instClock;
var tom_inst1;
var tom_inst1_2;
var tom_inst1_3;
var tom_inst2;
var tom_inst3;
var tom_inst4;
var tom_inst5;
var tom_inst_resp;
var prac_tom_trialClock;
var prac_tom1;
var prac_tom2;
var prac_tom3;
var prac_tom_dec;
var prac_tom_resp;
var prac_tom_itiClock;
var prac_tom_fb;
var prac_dual_instClock;
var dual_inst1;
var dual_inst2;
var dual_inst3;
var dual_inst4;
var dial_inst5;
var dual_inst_resp;
var prac_dual_tom1Clock;
var prac_d_tom1;
var prac_dual_tom2Clock;
var prac_d_tom2;
var prac_dual_tom3Clock;
var prac_d_tom3;
var prac_dual_tom_decClock;
var prac_d_tom_choice;
var prac_d_tom_resp;
var prac_d_tom_itiClock;
var prac_d_tom_fb;
var real_task_instClock;
var trial_inst;
var trial_inst2;
var trial_start;
var tom_introClock;
var tom_task;
var tom_int_resp;
var tom_single_trialClock;
var tom_s_1;
var tom_s_2;
var tom_s_3;
var tom_s_dec;
var tom_s_resp;
var ITI_2000Clock;
var tom_iti;
var restClock;
var rest_15;
var rest_15_2;
var rest_resp;
var dual_introClock;
var dual_task_intro;
var dual_task_intro_resp;
var dual_itiClock;
var dual_iti_cross;
var ssst_itiClock;
var ssst_iti_cross;
var stop_sigClock;
var ssd;
var ssst_go;
var ssst_stop;
var ssst_resp;
var tom_dual_1Clock;
var tom_d_1;
var tom_dual_2Clock;
var tom_d_2;
var tom_dual_3Clock;
var tom_d_3;
var tom_dual_decClock;
var tom_choice;
var tom_d_resp;
var outroClock;
var outro_text;
var outro_text2;
var outro_resp;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "welcome"
  welcomeClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: 'Welcome!\n\nHere you will play two games. But first, we will practice these games.\n\nDuring the practice you will recieve feedback on your responses but you will not during the actual game. \n\nAfter you complete the practices and tasks you will be given a link to complete the final part of the study.\n\nTo continue press SPACEBAR.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  welcome_adv = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ssst_prac_inst"
  ssst_prac_instClock = new util.Clock();
  ssst_inst1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssst_inst1',
    text: 'Shapes game practice\n\nIn this game, you will respond as fast as you can to a downward arrow by pressing the SPACEBAR with your RIGHT THUMB.\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  ssst_inst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssst_inst2',
    text: 'As soon as you see a downward arrow press the SPACEBAR as fast as you can!',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  ssst_inst3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssst_inst3',
    text: 'Other shapes may appear around the arrow - but do not pay attention to these only press the SPACEBAR as fast as you see a downward arrow',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  ssst_inst5 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ssst_inst5', units : undefined, 
    image : 'practice_stimuli/inst_ssst_ctrl.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  ssst_inst6 = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssst_inst6',
    text: 'Remember to respond as fast as you can!\n\nShapes game practice will start in 10 seconds or press SPACEBAR to start. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  key_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_ssst_trial"
  prac_ssst_trialClock = new util.Clock();
  // Run 'Begin Experiment' code from prac_ssst_staircase
  ssd_prac = 0.15;
  stepsize = 0.05;
  minval = 0.05;
  maxval = 1.05;
  
  prac_ssst_go = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_ssst_go', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  prac_ssst_stop = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_ssst_stop', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  prac_ssst_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_ssst_iti"
  prac_ssst_itiClock = new util.Clock();
  prac_ssst_iti_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_ssst_iti_cross',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "prac_tom_inst"
  prac_tom_instClock = new util.Clock();
  tom_inst1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst1',
    text: 'Cartoon game practice\n\nHere you will see three cartoon story scenes and it is up to you to decide the ending of these stories. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  tom_inst1_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst1_2',
    text: 'To solve these stories, you will have to try to take the perspective of the characters to decide the most possible ending. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  tom_inst1_3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst1_3',
    text: 'There are no wrong or right solutions. We are interested in your thoughts on how the story might end, considering the characters’ feelings and thoughts.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  tom_inst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst2',
    text: 'Your choices will be labeled 1, 2, and 3 and you will select your option by pressing 1, 2, or 3 at the top of your keyboard with your left hand. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -3.0 
  });
  
  tom_inst3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst3',
    text: 'DO NOT use numbers on the right of your keyboard ONLY USE the numbers at the top of your keyboard. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  tom_inst4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_inst4', units : undefined, 
    image : 'practice_stimuli/inst_tom.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -5.0 
  });
  tom_inst5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_inst5',
    text: 'Cartoon game practice will start in 10 seconds or press SPACEBAR',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -6.0 
  });
  
  tom_inst_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_tom_trial"
  prac_tom_trialClock = new util.Clock();
  prac_tom1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_tom1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  prac_tom2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_tom2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  prac_tom3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_tom3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  prac_tom_dec = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_tom_dec', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  prac_tom_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_tom_iti"
  prac_tom_itiClock = new util.Clock();
  prac_tom_fb = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_tom_fb',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "prac_dual_inst"
  prac_dual_instClock = new util.Clock();
  dual_inst1 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dual_inst1',
    text: 'Combined Game Practice\n\nHere you will be asked to play both games at the same time',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  dual_inst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dual_inst2',
    text: 'You will use the same buttons as the prior games, but you will use all of them in this combined game.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  dual_inst3 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dual_inst3',
    text: 'Please place your both of your hands on the left and right sides of the keyboard to play the combined game.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -2.0 
  });
  
  dual_inst4 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'dual_inst4', units : undefined, 
    image : 'practice_stimuli/inst_dual-task_ctrl.png', mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  dial_inst5 = new visual.TextStim({
    win: psychoJS.window,
    name: 'dial_inst5',
    text: 'Combined game practice will start in 10 seconds or press SPACEBAR. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -4.0 
  });
  
  dual_inst_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_dual_tom1"
  prac_dual_tom1Clock = new util.Clock();
  prac_d_tom1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_d_tom1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "prac_dual_tom2"
  prac_dual_tom2Clock = new util.Clock();
  prac_d_tom2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_d_tom2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "prac_dual_tom3"
  prac_dual_tom3Clock = new util.Clock();
  prac_d_tom3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_d_tom3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "prac_dual_tom_dec"
  prac_dual_tom_decClock = new util.Clock();
  prac_d_tom_choice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'prac_d_tom_choice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  prac_d_tom_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "prac_d_tom_iti"
  prac_d_tom_itiClock = new util.Clock();
  prac_d_tom_fb = new visual.TextStim({
    win: psychoJS.window,
    name: 'prac_d_tom_fb',
    text: '',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "real_task_inst"
  real_task_instClock = new util.Clock();
  trial_inst = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_inst',
    text: 'Rest for 15 seconds - we will start the study next. \n\nPlease place you left and right hands on the keyboard as instructred. \n\nRemember, if you respond to > 90% of the trials you will recieve an additional 10 dollars, so respond as quickly and as accurately as you can.\n\nYou will no longer recieve feedback about your response.\n\n\n\n',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  trial_inst2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'trial_inst2',
    text: 'Press SPACEBAR to start to start the task',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  trial_start = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "tom_intro"
  tom_introClock = new util.Clock();
  tom_task = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_task',
    text: 'Now you will play the cartoon game.\n\npress SPACEBAR',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  tom_int_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "tom_single_trial"
  tom_single_trialClock = new util.Clock();
  tom_s_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_s_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  tom_s_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_s_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  tom_s_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_s_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  tom_s_dec = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_s_dec', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -3.0 
  });
  tom_s_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI_2000"
  ITI_2000Clock = new util.Clock();
  tom_iti = new visual.TextStim({
    win: psychoJS.window,
    name: 'tom_iti',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "rest"
  restClock = new util.Clock();
  rest_15 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_15',
    text: 'Take a 15 second break before the next task.',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  rest_15_2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'rest_15_2',
    text: 'Press SPACEBAR to continue. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  rest_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "dual_intro"
  dual_introClock = new util.Clock();
  dual_task_intro = new visual.TextStim({
    win: psychoJS.window,
    name: 'dual_task_intro',
    text: 'Now you will play the combination game.\n\nRemember to respond as fast as you can!\n\npress SPACEBAR',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  dual_task_intro_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "dual_iti"
  dual_itiClock = new util.Clock();
  dual_iti_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'dual_iti_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "ssst_iti"
  ssst_itiClock = new util.Clock();
  ssst_iti_cross = new visual.TextStim({
    win: psychoJS.window,
    name: 'ssst_iti_cross',
    text: '+',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  // Initialize components for Routine "stop_sig"
  stop_sigClock = new util.Clock();
  // Run 'Begin Experiment' code from ssst_staircase
  ssd = 0.15;
  stepsize = 0.05;
  minval = 0.05;
  maxval = 1.05;
  
  ssst_go = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ssst_go', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -1.0 
  });
  ssst_stop = new visual.ImageStim({
    win : psychoJS.window,
    name : 'ssst_stop', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [0.5, 0.5],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : -2.0 
  });
  ssst_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "tom_dual_1"
  tom_dual_1Clock = new util.Clock();
  tom_d_1 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_d_1', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "tom_dual_2"
  tom_dual_2Clock = new util.Clock();
  tom_d_2 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_d_2', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "tom_dual_3"
  tom_dual_3Clock = new util.Clock();
  tom_d_3 = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_d_3', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  // Initialize components for Routine "tom_dual_dec"
  tom_dual_decClock = new util.Clock();
  tom_choice = new visual.ImageStim({
    win : psychoJS.window,
    name : 'tom_choice', units : undefined, 
    image : undefined, mask : undefined,
    ori : 0.0, pos : [0, 0], size : [1, 1],
    color : new util.Color([1,1,1]), opacity : undefined,
    flipHoriz : false, flipVert : false,
    texRes : 128.0, interpolate : true, depth : 0.0 
  });
  tom_d_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "outro"
  outroClock = new util.Clock();
  outro_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'outro_text',
    text: 'Contrats on completing the first portion of the study! \n\nAfter leaving the next page you will be asked to press ok with your mouse which will immediately take you to the next portion of the study.\n\nRemember the last 5 digits of your phone number and the email you registered with so that you can enter the next part of the study. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  outro_text2 = new visual.TextStim({
    win: psychoJS.window,
    name: 'outro_text2',
    text: 'Again you will need the last 5 digits of your phone number and the email you registered with so to enter the next part of the study. \n\nPress SPACEBAR to go to end this part the study and wait until a box appears that asks you to click ok with your mouse. ',
    font: 'Open Sans',
    units: undefined, 
    pos: [0, 0], height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: -1.0 
  });
  
  outro_resp = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var _welcome_adv_allKeys;
var welcomeComponents;
function welcomeRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'welcome' ---
    t = 0;
    welcomeClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    welcome_adv.keys = undefined;
    welcome_adv.rt = undefined;
    _welcome_adv_allKeys = [];
    // keep track of which components have finished
    welcomeComponents = [];
    welcomeComponents.push(text);
    welcomeComponents.push(welcome_adv);
    
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function welcomeRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'welcome' ---
    // get current time
    t = welcomeClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }

    
    // *welcome_adv* updates
    if (t >= 1 && welcome_adv.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      welcome_adv.tStart = t;  // (not accounting for frame time here)
      welcome_adv.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { welcome_adv.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { welcome_adv.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { welcome_adv.clearEvents(); });
    }

    if (welcome_adv.status === PsychoJS.Status.STARTED) {
      let theseKeys = welcome_adv.getKeys({keyList: ['space'], waitRelease: false});
      _welcome_adv_allKeys = _welcome_adv_allKeys.concat(theseKeys);
      if (_welcome_adv_allKeys.length > 0) {
        welcome_adv.keys = _welcome_adv_allKeys[_welcome_adv_allKeys.length - 1].name;  // just the last key pressed
        welcome_adv.rt = _welcome_adv_allKeys[_welcome_adv_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    welcomeComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function welcomeRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'welcome' ---
    welcomeComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(welcome_adv.corr, level);
    }
    psychoJS.experiment.addData('welcome_adv.keys', welcome_adv.keys);
    if (typeof welcome_adv.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('welcome_adv.rt', welcome_adv.rt);
        routineTimer.reset();
        }
    
    welcome_adv.stop();
    // the Routine "welcome" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _key_resp_allKeys;
var ssst_prac_instComponents;
function ssst_prac_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ssst_prac_inst' ---
    t = 0;
    ssst_prac_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(47.000000);
    // update component parameters for each repeat
    key_resp.keys = undefined;
    key_resp.rt = undefined;
    _key_resp_allKeys = [];
    // keep track of which components have finished
    ssst_prac_instComponents = [];
    ssst_prac_instComponents.push(ssst_inst1);
    ssst_prac_instComponents.push(ssst_inst2);
    ssst_prac_instComponents.push(ssst_inst3);
    ssst_prac_instComponents.push(ssst_inst5);
    ssst_prac_instComponents.push(ssst_inst6);
    ssst_prac_instComponents.push(key_resp);
    
    ssst_prac_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ssst_prac_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ssst_prac_inst' ---
    // get current time
    t = ssst_prac_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ssst_inst1* updates
    if (t >= 0.0 && ssst_inst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_inst1.tStart = t;  // (not accounting for frame time here)
      ssst_inst1.frameNStart = frameN;  // exact frame index
      
      ssst_inst1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 9 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_inst1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_inst1.setAutoDraw(false);
    }
    
    // *ssst_inst2* updates
    if (t >= 9 && ssst_inst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_inst2.tStart = t;  // (not accounting for frame time here)
      ssst_inst2.frameNStart = frameN;  // exact frame index
      
      ssst_inst2.setAutoDraw(true);
    }

    frameRemains = 9 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_inst2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_inst2.setAutoDraw(false);
    }
    
    // *ssst_inst3* updates
    if (t >= 16 && ssst_inst3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_inst3.tStart = t;  // (not accounting for frame time here)
      ssst_inst3.frameNStart = frameN;  // exact frame index
      
      ssst_inst3.setAutoDraw(true);
    }

    frameRemains = 16 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_inst3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_inst3.setAutoDraw(false);
    }
    
    // *ssst_inst5* updates
    if (t >= 23 && ssst_inst5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_inst5.tStart = t;  // (not accounting for frame time here)
      ssst_inst5.frameNStart = frameN;  // exact frame index
      
      ssst_inst5.setAutoDraw(true);
    }

    frameRemains = 23 + 14 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_inst5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_inst5.setAutoDraw(false);
    }
    
    // *ssst_inst6* updates
    if (t >= 37 && ssst_inst6.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_inst6.tStart = t;  // (not accounting for frame time here)
      ssst_inst6.frameNStart = frameN;  // exact frame index
      
      ssst_inst6.setAutoDraw(true);
    }

    frameRemains = 37 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_inst6.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_inst6.setAutoDraw(false);
    }
    
    // *key_resp* updates
    if (t >= 37 && key_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_resp.tStart = t;  // (not accounting for frame time here)
      key_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_resp.clearEvents(); });
    }

    frameRemains = 37 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (key_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      key_resp.status = PsychoJS.Status.FINISHED;
  }

    if (key_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_resp.getKeys({keyList: ['space'], waitRelease: false});
      _key_resp_allKeys = _key_resp_allKeys.concat(theseKeys);
      if (_key_resp_allKeys.length > 0) {
        key_resp.keys = _key_resp_allKeys[_key_resp_allKeys.length - 1].name;  // just the last key pressed
        key_resp.rt = _key_resp_allKeys[_key_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ssst_prac_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ssst_prac_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ssst_prac_inst' ---
    ssst_prac_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_resp.corr, level);
    }
    psychoJS.experiment.addData('key_resp.keys', key_resp.keys);
    if (typeof key_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_resp.rt', key_resp.rt);
        routineTimer.reset();
        }
    
    key_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_ssst;
function prac_ssstLoopBegin(prac_ssstLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_ssst = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 3, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'prac_ssst'
    });
    psychoJS.experiment.addLoop(prac_ssst); // add the loop to the experiment
    currentLoop = prac_ssst;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_ssst.forEach(function() {
      snapshot = prac_ssst.getSnapshot();
    
      prac_ssstLoopScheduler.add(importConditions(snapshot));
      prac_ssstLoopScheduler.add(prac_ssst_trialRoutineBegin(snapshot));
      prac_ssstLoopScheduler.add(prac_ssst_trialRoutineEachFrame());
      prac_ssstLoopScheduler.add(prac_ssst_trialRoutineEnd(snapshot));
      prac_ssstLoopScheduler.add(prac_ssst_itiRoutineBegin(snapshot));
      prac_ssstLoopScheduler.add(prac_ssst_itiRoutineEachFrame());
      prac_ssstLoopScheduler.add(prac_ssst_itiRoutineEnd(snapshot));
      prac_ssstLoopScheduler.add(prac_ssstLoopEndIteration(prac_ssstLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_ssstLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_ssst);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_ssstLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_tom;
function prac_tomLoopBegin(prac_tomLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_tom = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/prac_tom_cond.xlsx',
      seed: undefined, name: 'prac_tom'
    });
    psychoJS.experiment.addLoop(prac_tom); // add the loop to the experiment
    currentLoop = prac_tom;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_tom.forEach(function() {
      snapshot = prac_tom.getSnapshot();
    
      prac_tomLoopScheduler.add(importConditions(snapshot));
      prac_tomLoopScheduler.add(prac_tom_trialRoutineBegin(snapshot));
      prac_tomLoopScheduler.add(prac_tom_trialRoutineEachFrame());
      prac_tomLoopScheduler.add(prac_tom_trialRoutineEnd(snapshot));
      prac_tomLoopScheduler.add(prac_tom_itiRoutineBegin(snapshot));
      prac_tomLoopScheduler.add(prac_tom_itiRoutineEachFrame());
      prac_tomLoopScheduler.add(prac_tom_itiRoutineEnd(snapshot));
      prac_tomLoopScheduler.add(prac_tomLoopEndIteration(prac_tomLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_tomLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_tom);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_tomLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_dual;
function prac_dualLoopBegin(prac_dualLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_dual = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/prac_dual_tom_cond.xlsx',
      seed: undefined, name: 'prac_dual'
    });
    psychoJS.experiment.addLoop(prac_dual); // add the loop to the experiment
    currentLoop = prac_dual;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_dual.forEach(function() {
      snapshot = prac_dual.getSnapshot();
    
      prac_dualLoopScheduler.add(importConditions(snapshot));
      const prac_dual_ssst1LoopScheduler = new Scheduler(psychoJS);
      prac_dualLoopScheduler.add(prac_dual_ssst1LoopBegin(prac_dual_ssst1LoopScheduler, snapshot));
      prac_dualLoopScheduler.add(prac_dual_ssst1LoopScheduler);
      prac_dualLoopScheduler.add(prac_dual_ssst1LoopEnd);
      prac_dualLoopScheduler.add(prac_dual_tom1RoutineBegin(snapshot));
      prac_dualLoopScheduler.add(prac_dual_tom1RoutineEachFrame());
      prac_dualLoopScheduler.add(prac_dual_tom1RoutineEnd(snapshot));
      const prac_dual_ssst2LoopScheduler = new Scheduler(psychoJS);
      prac_dualLoopScheduler.add(prac_dual_ssst2LoopBegin(prac_dual_ssst2LoopScheduler, snapshot));
      prac_dualLoopScheduler.add(prac_dual_ssst2LoopScheduler);
      prac_dualLoopScheduler.add(prac_dual_ssst2LoopEnd);
      prac_dualLoopScheduler.add(prac_dual_tom2RoutineBegin(snapshot));
      prac_dualLoopScheduler.add(prac_dual_tom2RoutineEachFrame());
      prac_dualLoopScheduler.add(prac_dual_tom2RoutineEnd(snapshot));
      const prac_dual_ssst3LoopScheduler = new Scheduler(psychoJS);
      prac_dualLoopScheduler.add(prac_dual_ssst3LoopBegin(prac_dual_ssst3LoopScheduler, snapshot));
      prac_dualLoopScheduler.add(prac_dual_ssst3LoopScheduler);
      prac_dualLoopScheduler.add(prac_dual_ssst3LoopEnd);
      prac_dualLoopScheduler.add(prac_dual_tom3RoutineBegin(snapshot));
      prac_dualLoopScheduler.add(prac_dual_tom3RoutineEachFrame());
      prac_dualLoopScheduler.add(prac_dual_tom3RoutineEnd(snapshot));
      prac_dualLoopScheduler.add(prac_dual_tom_decRoutineBegin(snapshot));
      prac_dualLoopScheduler.add(prac_dual_tom_decRoutineEachFrame());
      prac_dualLoopScheduler.add(prac_dual_tom_decRoutineEnd(snapshot));
      prac_dualLoopScheduler.add(prac_d_tom_itiRoutineBegin(snapshot));
      prac_dualLoopScheduler.add(prac_d_tom_itiRoutineEachFrame());
      prac_dualLoopScheduler.add(prac_d_tom_itiRoutineEnd(snapshot));
      prac_dualLoopScheduler.add(prac_dualLoopEndIteration(prac_dualLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var prac_dual_ssst1;
function prac_dual_ssst1LoopBegin(prac_dual_ssst1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_dual_ssst1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'prac_dual_ssst1'
    });
    psychoJS.experiment.addLoop(prac_dual_ssst1); // add the loop to the experiment
    currentLoop = prac_dual_ssst1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_dual_ssst1.forEach(function() {
      snapshot = prac_dual_ssst1.getSnapshot();
    
      prac_dual_ssst1LoopScheduler.add(importConditions(snapshot));
      prac_dual_ssst1LoopScheduler.add(prac_ssst_trialRoutineBegin(snapshot));
      prac_dual_ssst1LoopScheduler.add(prac_ssst_trialRoutineEachFrame());
      prac_dual_ssst1LoopScheduler.add(prac_ssst_trialRoutineEnd(snapshot));
      prac_dual_ssst1LoopScheduler.add(prac_ssst_itiRoutineBegin(snapshot));
      prac_dual_ssst1LoopScheduler.add(prac_ssst_itiRoutineEachFrame());
      prac_dual_ssst1LoopScheduler.add(prac_ssst_itiRoutineEnd(snapshot));
      prac_dual_ssst1LoopScheduler.add(prac_dual_ssst1LoopEndIteration(prac_dual_ssst1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_dual_ssst1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_dual_ssst1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_dual_ssst1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_dual_ssst2;
function prac_dual_ssst2LoopBegin(prac_dual_ssst2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_dual_ssst2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'prac_dual_ssst2'
    });
    psychoJS.experiment.addLoop(prac_dual_ssst2); // add the loop to the experiment
    currentLoop = prac_dual_ssst2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_dual_ssst2.forEach(function() {
      snapshot = prac_dual_ssst2.getSnapshot();
    
      prac_dual_ssst2LoopScheduler.add(importConditions(snapshot));
      prac_dual_ssst2LoopScheduler.add(prac_ssst_trialRoutineBegin(snapshot));
      prac_dual_ssst2LoopScheduler.add(prac_ssst_trialRoutineEachFrame());
      prac_dual_ssst2LoopScheduler.add(prac_ssst_trialRoutineEnd(snapshot));
      prac_dual_ssst2LoopScheduler.add(prac_ssst_itiRoutineBegin(snapshot));
      prac_dual_ssst2LoopScheduler.add(prac_ssst_itiRoutineEachFrame());
      prac_dual_ssst2LoopScheduler.add(prac_ssst_itiRoutineEnd(snapshot));
      prac_dual_ssst2LoopScheduler.add(prac_dual_ssst2LoopEndIteration(prac_dual_ssst2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_dual_ssst2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_dual_ssst2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_dual_ssst2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var prac_dual_ssst3;
function prac_dual_ssst3LoopBegin(prac_dual_ssst3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    prac_dual_ssst3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'prac_dual_ssst3'
    });
    psychoJS.experiment.addLoop(prac_dual_ssst3); // add the loop to the experiment
    currentLoop = prac_dual_ssst3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    prac_dual_ssst3.forEach(function() {
      snapshot = prac_dual_ssst3.getSnapshot();
    
      prac_dual_ssst3LoopScheduler.add(importConditions(snapshot));
      prac_dual_ssst3LoopScheduler.add(prac_ssst_trialRoutineBegin(snapshot));
      prac_dual_ssst3LoopScheduler.add(prac_ssst_trialRoutineEachFrame());
      prac_dual_ssst3LoopScheduler.add(prac_ssst_trialRoutineEnd(snapshot));
      prac_dual_ssst3LoopScheduler.add(prac_ssst_itiRoutineBegin(snapshot));
      prac_dual_ssst3LoopScheduler.add(prac_ssst_itiRoutineEachFrame());
      prac_dual_ssst3LoopScheduler.add(prac_ssst_itiRoutineEnd(snapshot));
      prac_dual_ssst3LoopScheduler.add(prac_dual_ssst3LoopEndIteration(prac_dual_ssst3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function prac_dual_ssst3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_dual_ssst3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_dual_ssst3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function prac_dualLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(prac_dual);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function prac_dualLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var tom_block;
function tom_blockLoopBegin(tom_blockLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    tom_block = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'tom_block'
    });
    psychoJS.experiment.addLoop(tom_block); // add the loop to the experiment
    currentLoop = tom_block;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    tom_block.forEach(function() {
      snapshot = tom_block.getSnapshot();
    
      tom_blockLoopScheduler.add(importConditions(snapshot));
      tom_blockLoopScheduler.add(tom_introRoutineBegin(snapshot));
      tom_blockLoopScheduler.add(tom_introRoutineEachFrame());
      tom_blockLoopScheduler.add(tom_introRoutineEnd(snapshot));
      const tom_singleLoopScheduler = new Scheduler(psychoJS);
      tom_blockLoopScheduler.add(tom_singleLoopBegin(tom_singleLoopScheduler, snapshot));
      tom_blockLoopScheduler.add(tom_singleLoopScheduler);
      tom_blockLoopScheduler.add(tom_singleLoopEnd);
      tom_blockLoopScheduler.add(tom_blockLoopEndIteration(tom_blockLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var tom_single;
function tom_singleLoopBegin(tom_singleLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    tom_single = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/tom_cond.xlsx',
      seed: undefined, name: 'tom_single'
    });
    psychoJS.experiment.addLoop(tom_single); // add the loop to the experiment
    currentLoop = tom_single;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    tom_single.forEach(function() {
      snapshot = tom_single.getSnapshot();
    
      tom_singleLoopScheduler.add(importConditions(snapshot));
      tom_singleLoopScheduler.add(tom_single_trialRoutineBegin(snapshot));
      tom_singleLoopScheduler.add(tom_single_trialRoutineEachFrame());
      tom_singleLoopScheduler.add(tom_single_trialRoutineEnd(snapshot));
      tom_singleLoopScheduler.add(ITI_2000RoutineBegin(snapshot));
      tom_singleLoopScheduler.add(ITI_2000RoutineEachFrame());
      tom_singleLoopScheduler.add(ITI_2000RoutineEnd(snapshot));
      tom_singleLoopScheduler.add(tom_singleLoopEndIteration(tom_singleLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function tom_singleLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(tom_single);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function tom_singleLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function tom_blockLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(tom_block);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function tom_blockLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var dual_block;
function dual_blockLoopBegin(dual_blockLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    dual_block = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: undefined,
      seed: undefined, name: 'dual_block'
    });
    psychoJS.experiment.addLoop(dual_block); // add the loop to the experiment
    currentLoop = dual_block;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    dual_block.forEach(function() {
      snapshot = dual_block.getSnapshot();
    
      dual_blockLoopScheduler.add(importConditions(snapshot));
      dual_blockLoopScheduler.add(dual_introRoutineBegin(snapshot));
      dual_blockLoopScheduler.add(dual_introRoutineEachFrame());
      dual_blockLoopScheduler.add(dual_introRoutineEnd(snapshot));
      const dual_taskLoopScheduler = new Scheduler(psychoJS);
      dual_blockLoopScheduler.add(dual_taskLoopBegin(dual_taskLoopScheduler, snapshot));
      dual_blockLoopScheduler.add(dual_taskLoopScheduler);
      dual_blockLoopScheduler.add(dual_taskLoopEnd);
      dual_blockLoopScheduler.add(dual_blockLoopEndIteration(dual_blockLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var dual_task;
function dual_taskLoopBegin(dual_taskLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    dual_task = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/tom_cond.xlsx',
      seed: undefined, name: 'dual_task'
    });
    psychoJS.experiment.addLoop(dual_task); // add the loop to the experiment
    currentLoop = dual_task;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    dual_task.forEach(function() {
      snapshot = dual_task.getSnapshot();
    
      dual_taskLoopScheduler.add(importConditions(snapshot));
      dual_taskLoopScheduler.add(dual_itiRoutineBegin(snapshot));
      dual_taskLoopScheduler.add(dual_itiRoutineEachFrame());
      dual_taskLoopScheduler.add(dual_itiRoutineEnd(snapshot));
      const ssst_loop1LoopScheduler = new Scheduler(psychoJS);
      dual_taskLoopScheduler.add(ssst_loop1LoopBegin(ssst_loop1LoopScheduler, snapshot));
      dual_taskLoopScheduler.add(ssst_loop1LoopScheduler);
      dual_taskLoopScheduler.add(ssst_loop1LoopEnd);
      dual_taskLoopScheduler.add(tom_dual_1RoutineBegin(snapshot));
      dual_taskLoopScheduler.add(tom_dual_1RoutineEachFrame());
      dual_taskLoopScheduler.add(tom_dual_1RoutineEnd(snapshot));
      const ssst_loop2LoopScheduler = new Scheduler(psychoJS);
      dual_taskLoopScheduler.add(ssst_loop2LoopBegin(ssst_loop2LoopScheduler, snapshot));
      dual_taskLoopScheduler.add(ssst_loop2LoopScheduler);
      dual_taskLoopScheduler.add(ssst_loop2LoopEnd);
      dual_taskLoopScheduler.add(tom_dual_2RoutineBegin(snapshot));
      dual_taskLoopScheduler.add(tom_dual_2RoutineEachFrame());
      dual_taskLoopScheduler.add(tom_dual_2RoutineEnd(snapshot));
      const ssst_loop3LoopScheduler = new Scheduler(psychoJS);
      dual_taskLoopScheduler.add(ssst_loop3LoopBegin(ssst_loop3LoopScheduler, snapshot));
      dual_taskLoopScheduler.add(ssst_loop3LoopScheduler);
      dual_taskLoopScheduler.add(ssst_loop3LoopEnd);
      dual_taskLoopScheduler.add(tom_dual_3RoutineBegin(snapshot));
      dual_taskLoopScheduler.add(tom_dual_3RoutineEachFrame());
      dual_taskLoopScheduler.add(tom_dual_3RoutineEnd(snapshot));
      dual_taskLoopScheduler.add(tom_dual_decRoutineBegin(snapshot));
      dual_taskLoopScheduler.add(tom_dual_decRoutineEachFrame());
      dual_taskLoopScheduler.add(tom_dual_decRoutineEnd(snapshot));
      dual_taskLoopScheduler.add(dual_taskLoopEndIteration(dual_taskLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


var ssst_loop1;
function ssst_loop1LoopBegin(ssst_loop1LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ssst_loop1 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'ssst_loop1'
    });
    psychoJS.experiment.addLoop(ssst_loop1); // add the loop to the experiment
    currentLoop = ssst_loop1;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    ssst_loop1.forEach(function() {
      snapshot = ssst_loop1.getSnapshot();
    
      ssst_loop1LoopScheduler.add(importConditions(snapshot));
      ssst_loop1LoopScheduler.add(ssst_itiRoutineBegin(snapshot));
      ssst_loop1LoopScheduler.add(ssst_itiRoutineEachFrame());
      ssst_loop1LoopScheduler.add(ssst_itiRoutineEnd(snapshot));
      ssst_loop1LoopScheduler.add(stop_sigRoutineBegin(snapshot));
      ssst_loop1LoopScheduler.add(stop_sigRoutineEachFrame());
      ssst_loop1LoopScheduler.add(stop_sigRoutineEnd(snapshot));
      ssst_loop1LoopScheduler.add(ssst_loop1LoopEndIteration(ssst_loop1LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function ssst_loop1LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ssst_loop1);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ssst_loop1LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ssst_loop2;
function ssst_loop2LoopBegin(ssst_loop2LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ssst_loop2 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'ssst_loop2'
    });
    psychoJS.experiment.addLoop(ssst_loop2); // add the loop to the experiment
    currentLoop = ssst_loop2;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    ssst_loop2.forEach(function() {
      snapshot = ssst_loop2.getSnapshot();
    
      ssst_loop2LoopScheduler.add(importConditions(snapshot));
      ssst_loop2LoopScheduler.add(ssst_itiRoutineBegin(snapshot));
      ssst_loop2LoopScheduler.add(ssst_itiRoutineEachFrame());
      ssst_loop2LoopScheduler.add(ssst_itiRoutineEnd(snapshot));
      ssst_loop2LoopScheduler.add(stop_sigRoutineBegin(snapshot));
      ssst_loop2LoopScheduler.add(stop_sigRoutineEachFrame());
      ssst_loop2LoopScheduler.add(stop_sigRoutineEnd(snapshot));
      ssst_loop2LoopScheduler.add(ssst_loop2LoopEndIteration(ssst_loop2LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function ssst_loop2LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ssst_loop2);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ssst_loop2LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ssst_loop3;
function ssst_loop3LoopBegin(ssst_loop3LoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    ssst_loop3 = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/ssst_go_stop.xlsx',
      seed: undefined, name: 'ssst_loop3'
    });
    psychoJS.experiment.addLoop(ssst_loop3); // add the loop to the experiment
    currentLoop = ssst_loop3;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    ssst_loop3.forEach(function() {
      snapshot = ssst_loop3.getSnapshot();
    
      ssst_loop3LoopScheduler.add(importConditions(snapshot));
      ssst_loop3LoopScheduler.add(ssst_itiRoutineBegin(snapshot));
      ssst_loop3LoopScheduler.add(ssst_itiRoutineEachFrame());
      ssst_loop3LoopScheduler.add(ssst_itiRoutineEnd(snapshot));
      ssst_loop3LoopScheduler.add(stop_sigRoutineBegin(snapshot));
      ssst_loop3LoopScheduler.add(stop_sigRoutineEachFrame());
      ssst_loop3LoopScheduler.add(stop_sigRoutineEnd(snapshot));
      ssst_loop3LoopScheduler.add(ssst_loop3LoopEndIteration(ssst_loop3LoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function ssst_loop3LoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(ssst_loop3);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function ssst_loop3LoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function dual_taskLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(dual_task);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function dual_taskLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


async function dual_blockLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(dual_block);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function dual_blockLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var _prac_ssst_resp_allKeys;
var prac_ssst_trialComponents;
function prac_ssst_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_ssst_trial' ---
    t = 0;
    prac_ssst_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    prac_ssst_go.setImage(go_img);
    prac_ssst_stop.setImage(st_img);
    prac_ssst_resp.keys = undefined;
    prac_ssst_resp.rt = undefined;
    _prac_ssst_resp_allKeys = [];
    // keep track of which components have finished
    prac_ssst_trialComponents = [];
    prac_ssst_trialComponents.push(prac_ssst_go);
    prac_ssst_trialComponents.push(prac_ssst_stop);
    prac_ssst_trialComponents.push(prac_ssst_resp);
    
    prac_ssst_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_ssst_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_ssst_trial' ---
    // get current time
    t = prac_ssst_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_ssst_go* updates
    if (t >= 0 && prac_ssst_go.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_ssst_go.tStart = t;  // (not accounting for frame time here)
      prac_ssst_go.frameNStart = frameN;  // exact frame index
      
      prac_ssst_go.setAutoDraw(true);
    }

    frameRemains = 0 + ssd - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_ssst_go.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_ssst_go.setAutoDraw(false);
    }
    
    // *prac_ssst_stop* updates
    if (t >= (ssd - 1e-05) && prac_ssst_stop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_ssst_stop.tStart = t;  // (not accounting for frame time here)
      prac_ssst_stop.frameNStart = frameN;  // exact frame index
      
      prac_ssst_stop.setAutoDraw(true);
    }

    frameRemains = (ssd - 1e-05) + (1.25 - ssd) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_ssst_stop.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_ssst_stop.setAutoDraw(false);
    }
    
    // *prac_ssst_resp* updates
    if (t >= 0.0 && prac_ssst_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_ssst_resp.tStart = t;  // (not accounting for frame time here)
      prac_ssst_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_ssst_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_ssst_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_ssst_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_ssst_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_ssst_resp.status = PsychoJS.Status.FINISHED;
  }

    if (prac_ssst_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_ssst_resp.getKeys({keyList: ['space'], waitRelease: false});
      _prac_ssst_resp_allKeys = _prac_ssst_resp_allKeys.concat(theseKeys);
      if (_prac_ssst_resp_allKeys.length > 0) {
        prac_ssst_resp.keys = _prac_ssst_resp_allKeys[_prac_ssst_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_ssst_resp.rt = _prac_ssst_resp_allKeys[_prac_ssst_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_ssst_resp.keys == corr_resp) {
            prac_ssst_resp.corr = 1;
        } else {
            prac_ssst_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_ssst_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_ssst_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_ssst_trial' ---
    prac_ssst_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from prac_ssst_staircase
    psychoJS.experiment.addData("trial_type", trial_type);
    psychoJS.experiment.addData("ssd_prac", ssd_prac);
    psychoJS.experiment.addData("prac_ssst_resp", prac_ssst_resp.keys);
    if ((trial_type === "stop")) {
        if ((prac_ssst_resp.corr === 1)) {
            ssd_prac += stepsize;
        } else {
            ssd_prac -= stepsize;
        }
        if ((ssd_prac < minval)) {
            ssd_prac = minval;
        }
        if ((ssd_prac > maxval)) {
            ssd_prac = maxval;
        }
    }
    
    // was no response the correct answer?!
    if (prac_ssst_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp)) {
         prac_ssst_resp.corr = 1;  // correct non-response
      } else {
         prac_ssst_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(prac_ssst_resp.corr, level);
    }
    psychoJS.experiment.addData('prac_ssst_resp.keys', prac_ssst_resp.keys);
    psychoJS.experiment.addData('prac_ssst_resp.corr', prac_ssst_resp.corr);
    if (typeof prac_ssst_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_ssst_resp.rt', prac_ssst_resp.rt);
        routineTimer.reset();
        }
    
    prac_ssst_resp.stop();
    // the Routine "prac_ssst_trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var msg;
var color;
var prac_ssst_itiComponents;
function prac_ssst_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_ssst_iti' ---
    t = 0;
    prac_ssst_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from prac_ssst_iti_draw
    if (prac_ssst_resp.corr) {
        msg = "Correct!";
        color = "green";
    } else {
        msg = "Oops! That was wrong - SPACEBAR as soon as you see a downward arrow";
        color = "red";
    }
    
    prac_ssst_iti_cross.setColor(new util.Color(color));
    prac_ssst_iti_cross.setText(msg);
    // keep track of which components have finished
    prac_ssst_itiComponents = [];
    prac_ssst_itiComponents.push(prac_ssst_iti_cross);
    
    prac_ssst_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_ssst_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_ssst_iti' ---
    // get current time
    t = prac_ssst_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_ssst_iti_cross* updates
    if (t >= 0.0 && prac_ssst_iti_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_ssst_iti_cross.tStart = t;  // (not accounting for frame time here)
      prac_ssst_iti_cross.frameNStart = frameN;  // exact frame index
      
      prac_ssst_iti_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_ssst_iti_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_ssst_iti_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_ssst_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_ssst_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_ssst_iti' ---
    prac_ssst_itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _tom_inst_resp_allKeys;
var prac_tom_instComponents;
function prac_tom_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_tom_inst' ---
    t = 0;
    prac_tom_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(55.000000);
    // update component parameters for each repeat
    tom_inst_resp.keys = undefined;
    tom_inst_resp.rt = undefined;
    _tom_inst_resp_allKeys = [];
    // keep track of which components have finished
    prac_tom_instComponents = [];
    prac_tom_instComponents.push(tom_inst1);
    prac_tom_instComponents.push(tom_inst1_2);
    prac_tom_instComponents.push(tom_inst1_3);
    prac_tom_instComponents.push(tom_inst2);
    prac_tom_instComponents.push(tom_inst3);
    prac_tom_instComponents.push(tom_inst4);
    prac_tom_instComponents.push(tom_inst5);
    prac_tom_instComponents.push(tom_inst_resp);
    
    prac_tom_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_tom_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_tom_inst' ---
    // get current time
    t = prac_tom_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_inst1* updates
    if (t >= 0.0 && tom_inst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst1.tStart = t;  // (not accounting for frame time here)
      tom_inst1.frameNStart = frameN;  // exact frame index
      
      tom_inst1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst1.setAutoDraw(false);
    }
    
    // *tom_inst1_2* updates
    if (t >= 7 && tom_inst1_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst1_2.tStart = t;  // (not accounting for frame time here)
      tom_inst1_2.frameNStart = frameN;  // exact frame index
      
      tom_inst1_2.setAutoDraw(true);
    }

    frameRemains = 7 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst1_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst1_2.setAutoDraw(false);
    }
    
    // *tom_inst1_3* updates
    if (t >= 14 && tom_inst1_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst1_3.tStart = t;  // (not accounting for frame time here)
      tom_inst1_3.frameNStart = frameN;  // exact frame index
      
      tom_inst1_3.setAutoDraw(true);
    }

    frameRemains = 14 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst1_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst1_3.setAutoDraw(false);
    }
    
    // *tom_inst2* updates
    if (t >= 21 && tom_inst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst2.tStart = t;  // (not accounting for frame time here)
      tom_inst2.frameNStart = frameN;  // exact frame index
      
      tom_inst2.setAutoDraw(true);
    }

    frameRemains = 21 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst2.setAutoDraw(false);
    }
    
    // *tom_inst3* updates
    if (t >= 28 && tom_inst3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst3.tStart = t;  // (not accounting for frame time here)
      tom_inst3.frameNStart = frameN;  // exact frame index
      
      tom_inst3.setAutoDraw(true);
    }

    frameRemains = 28 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst3.setAutoDraw(false);
    }
    
    // *tom_inst4* updates
    if (t >= 35 && tom_inst4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst4.tStart = t;  // (not accounting for frame time here)
      tom_inst4.frameNStart = frameN;  // exact frame index
      
      tom_inst4.setAutoDraw(true);
    }

    frameRemains = 35 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst4.setAutoDraw(false);
    }
    
    // *tom_inst5* updates
    if (t >= 45 && tom_inst5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst5.tStart = t;  // (not accounting for frame time here)
      tom_inst5.frameNStart = frameN;  // exact frame index
      
      tom_inst5.setAutoDraw(true);
    }

    frameRemains = 45 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst5.setAutoDraw(false);
    }
    
    // *tom_inst_resp* updates
    if (t >= 45 && tom_inst_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_inst_resp.tStart = t;  // (not accounting for frame time here)
      tom_inst_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { tom_inst_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { tom_inst_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { tom_inst_resp.clearEvents(); });
    }

    frameRemains = 45 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_inst_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_inst_resp.status = PsychoJS.Status.FINISHED;
  }

    if (tom_inst_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = tom_inst_resp.getKeys({keyList: ['space'], waitRelease: false});
      _tom_inst_resp_allKeys = _tom_inst_resp_allKeys.concat(theseKeys);
      if (_tom_inst_resp_allKeys.length > 0) {
        tom_inst_resp.keys = _tom_inst_resp_allKeys[_tom_inst_resp_allKeys.length - 1].name;  // just the last key pressed
        tom_inst_resp.rt = _tom_inst_resp_allKeys[_tom_inst_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_tom_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_tom_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_tom_inst' ---
    prac_tom_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(tom_inst_resp.corr, level);
    }
    psychoJS.experiment.addData('tom_inst_resp.keys', tom_inst_resp.keys);
    if (typeof tom_inst_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('tom_inst_resp.rt', tom_inst_resp.rt);
        routineTimer.reset();
        }
    
    tom_inst_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _prac_tom_resp_allKeys;
var prac_tom_trialComponents;
function prac_tom_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_tom_trial' ---
    t = 0;
    prac_tom_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(11.500000);
    // update component parameters for each repeat
    prac_tom1.setImage(prac_img1);
    prac_tom2.setImage(prac_img2);
    prac_tom3.setImage(prac_img3);
    prac_tom_dec.setImage(prac_dec_img);
    prac_tom_resp.keys = undefined;
    prac_tom_resp.rt = undefined;
    _prac_tom_resp_allKeys = [];
    // keep track of which components have finished
    prac_tom_trialComponents = [];
    prac_tom_trialComponents.push(prac_tom1);
    prac_tom_trialComponents.push(prac_tom2);
    prac_tom_trialComponents.push(prac_tom3);
    prac_tom_trialComponents.push(prac_tom_dec);
    prac_tom_trialComponents.push(prac_tom_resp);
    
    prac_tom_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_tom_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_tom_trial' ---
    // get current time
    t = prac_tom_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_tom1* updates
    if (t >= 0 && prac_tom1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom1.tStart = t;  // (not accounting for frame time here)
      prac_tom1.frameNStart = frameN;  // exact frame index
      
      prac_tom1.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom1.setAutoDraw(false);
    }
    
    // *prac_tom2* updates
    if (t >= 1.5 && prac_tom2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom2.tStart = t;  // (not accounting for frame time here)
      prac_tom2.frameNStart = frameN;  // exact frame index
      
      prac_tom2.setAutoDraw(true);
    }

    frameRemains = 1.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom2.setAutoDraw(false);
    }
    
    // *prac_tom3* updates
    if (t >= 3 && prac_tom3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom3.tStart = t;  // (not accounting for frame time here)
      prac_tom3.frameNStart = frameN;  // exact frame index
      
      prac_tom3.setAutoDraw(true);
    }

    frameRemains = 3 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom3.setAutoDraw(false);
    }
    
    // *prac_tom_dec* updates
    if (t >= 4.5 && prac_tom_dec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom_dec.tStart = t;  // (not accounting for frame time here)
      prac_tom_dec.frameNStart = frameN;  // exact frame index
      
      prac_tom_dec.setAutoDraw(true);
    }

    frameRemains = 4.5 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom_dec.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom_dec.setAutoDraw(false);
    }
    
    // *prac_tom_resp* updates
    if (t >= 4.5 && prac_tom_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom_resp.tStart = t;  // (not accounting for frame time here)
      prac_tom_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_tom_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_tom_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_tom_resp.clearEvents(); });
    }

    frameRemains = 4.5 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom_resp.status = PsychoJS.Status.FINISHED;
  }

    if (prac_tom_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_tom_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _prac_tom_resp_allKeys = _prac_tom_resp_allKeys.concat(theseKeys);
      if (_prac_tom_resp_allKeys.length > 0) {
        prac_tom_resp.keys = _prac_tom_resp_allKeys[_prac_tom_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_tom_resp.rt = _prac_tom_resp_allKeys[_prac_tom_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_tom_resp.keys == corr_resp_tom_prac) {
            prac_tom_resp.corr = 1;
        } else {
            prac_tom_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_tom_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_tom_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_tom_trial' ---
    prac_tom_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (prac_tom_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp_tom_prac)) {
         prac_tom_resp.corr = 1;  // correct non-response
      } else {
         prac_tom_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(prac_tom_resp.corr, level);
    }
    psychoJS.experiment.addData('prac_tom_resp.keys', prac_tom_resp.keys);
    psychoJS.experiment.addData('prac_tom_resp.corr', prac_tom_resp.corr);
    if (typeof prac_tom_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_tom_resp.rt', prac_tom_resp.rt);
        routineTimer.reset();
        }
    
    prac_tom_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_tom_itiComponents;
function prac_tom_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_tom_iti' ---
    t = 0;
    prac_tom_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from prac_tom_code
    if ((! prac_tom_resp.keys)) {
        msg = "Failed to respond";
        color = "red";
    } else {
        msg = `Your reaction time was ${Math.round(prac_tom_resp.rt, 3)}`;
        color = "white";
    }
    
    prac_tom_fb.setColor(new util.Color(color));
    prac_tom_fb.setText(msg);
    // keep track of which components have finished
    prac_tom_itiComponents = [];
    prac_tom_itiComponents.push(prac_tom_fb);
    
    prac_tom_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_tom_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_tom_iti' ---
    // get current time
    t = prac_tom_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_tom_fb* updates
    if (t >= 0.0 && prac_tom_fb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_tom_fb.tStart = t;  // (not accounting for frame time here)
      prac_tom_fb.frameNStart = frameN;  // exact frame index
      
      prac_tom_fb.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_tom_fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_tom_fb.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_tom_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_tom_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_tom_iti' ---
    prac_tom_itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _dual_inst_resp_allKeys;
var prac_dual_instComponents;
function prac_dual_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_dual_inst' ---
    t = 0;
    prac_dual_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(39.000000);
    // update component parameters for each repeat
    dual_inst_resp.keys = undefined;
    dual_inst_resp.rt = undefined;
    _dual_inst_resp_allKeys = [];
    // keep track of which components have finished
    prac_dual_instComponents = [];
    prac_dual_instComponents.push(dual_inst1);
    prac_dual_instComponents.push(dual_inst2);
    prac_dual_instComponents.push(dual_inst3);
    prac_dual_instComponents.push(dual_inst4);
    prac_dual_instComponents.push(dial_inst5);
    prac_dual_instComponents.push(dual_inst_resp);
    
    prac_dual_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_dual_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_dual_inst' ---
    // get current time
    t = prac_dual_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dual_inst1* updates
    if (t >= 0.0 && dual_inst1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_inst1.tStart = t;  // (not accounting for frame time here)
      dual_inst1.frameNStart = frameN;  // exact frame index
      
      dual_inst1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_inst1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_inst1.setAutoDraw(false);
    }
    
    // *dual_inst2* updates
    if (t >= 7 && dual_inst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_inst2.tStart = t;  // (not accounting for frame time here)
      dual_inst2.frameNStart = frameN;  // exact frame index
      
      dual_inst2.setAutoDraw(true);
    }

    frameRemains = 7 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_inst2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_inst2.setAutoDraw(false);
    }
    
    // *dual_inst3* updates
    if (t >= 14 && dual_inst3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_inst3.tStart = t;  // (not accounting for frame time here)
      dual_inst3.frameNStart = frameN;  // exact frame index
      
      dual_inst3.setAutoDraw(true);
    }

    frameRemains = 14 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_inst3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_inst3.setAutoDraw(false);
    }
    
    // *dual_inst4* updates
    if (t >= 21 && dual_inst4.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_inst4.tStart = t;  // (not accounting for frame time here)
      dual_inst4.frameNStart = frameN;  // exact frame index
      
      dual_inst4.setAutoDraw(true);
    }

    frameRemains = 21 + 10 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_inst4.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_inst4.setAutoDraw(false);
    }
    
    // *dial_inst5* updates
    if (t >= 31 && dial_inst5.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dial_inst5.tStart = t;  // (not accounting for frame time here)
      dial_inst5.frameNStart = frameN;  // exact frame index
      
      dial_inst5.setAutoDraw(true);
    }

    frameRemains = 31 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dial_inst5.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dial_inst5.setAutoDraw(false);
    }
    
    // *dual_inst_resp* updates
    if (t >= 31 && dual_inst_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_inst_resp.tStart = t;  // (not accounting for frame time here)
      dual_inst_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dual_inst_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dual_inst_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dual_inst_resp.clearEvents(); });
    }

    frameRemains = 31 + 8 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_inst_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_inst_resp.status = PsychoJS.Status.FINISHED;
  }

    if (dual_inst_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = dual_inst_resp.getKeys({keyList: ['space'], waitRelease: false});
      _dual_inst_resp_allKeys = _dual_inst_resp_allKeys.concat(theseKeys);
      if (_dual_inst_resp_allKeys.length > 0) {
        dual_inst_resp.keys = _dual_inst_resp_allKeys[_dual_inst_resp_allKeys.length - 1].name;  // just the last key pressed
        dual_inst_resp.rt = _dual_inst_resp_allKeys[_dual_inst_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_dual_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_dual_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_dual_inst' ---
    prac_dual_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(dual_inst_resp.corr, level);
    }
    psychoJS.experiment.addData('dual_inst_resp.keys', dual_inst_resp.keys);
    if (typeof dual_inst_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dual_inst_resp.rt', dual_inst_resp.rt);
        routineTimer.reset();
        }
    
    dual_inst_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_dual_tom1Components;
function prac_dual_tom1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_dual_tom1' ---
    t = 0;
    prac_dual_tom1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    prac_d_tom1.setImage(prac_img1);
    // keep track of which components have finished
    prac_dual_tom1Components = [];
    prac_dual_tom1Components.push(prac_d_tom1);
    
    prac_dual_tom1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_dual_tom1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_dual_tom1' ---
    // get current time
    t = prac_dual_tom1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_d_tom1* updates
    if (t >= 0 && prac_d_tom1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom1.tStart = t;  // (not accounting for frame time here)
      prac_d_tom1.frameNStart = frameN;  // exact frame index
      
      prac_d_tom1.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_dual_tom1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_dual_tom1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_dual_tom1' ---
    prac_dual_tom1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_dual_tom2Components;
function prac_dual_tom2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_dual_tom2' ---
    t = 0;
    prac_dual_tom2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    prac_d_tom2.setImage(prac_img2);
    // keep track of which components have finished
    prac_dual_tom2Components = [];
    prac_dual_tom2Components.push(prac_d_tom2);
    
    prac_dual_tom2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_dual_tom2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_dual_tom2' ---
    // get current time
    t = prac_dual_tom2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_d_tom2* updates
    if (t >= 0 && prac_d_tom2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom2.tStart = t;  // (not accounting for frame time here)
      prac_d_tom2.frameNStart = frameN;  // exact frame index
      
      prac_d_tom2.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_dual_tom2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_dual_tom2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_dual_tom2' ---
    prac_dual_tom2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_dual_tom3Components;
function prac_dual_tom3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_dual_tom3' ---
    t = 0;
    prac_dual_tom3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    prac_d_tom3.setImage(prac_img3);
    // keep track of which components have finished
    prac_dual_tom3Components = [];
    prac_dual_tom3Components.push(prac_d_tom3);
    
    prac_dual_tom3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_dual_tom3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_dual_tom3' ---
    // get current time
    t = prac_dual_tom3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_d_tom3* updates
    if (t >= 0 && prac_d_tom3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom3.tStart = t;  // (not accounting for frame time here)
      prac_d_tom3.frameNStart = frameN;  // exact frame index
      
      prac_d_tom3.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_dual_tom3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_dual_tom3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_dual_tom3' ---
    prac_dual_tom3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _prac_d_tom_resp_allKeys;
var prac_dual_tom_decComponents;
function prac_dual_tom_decRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_dual_tom_dec' ---
    t = 0;
    prac_dual_tom_decClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    prac_d_tom_choice.setImage(prac_dec_img);
    prac_d_tom_resp.keys = undefined;
    prac_d_tom_resp.rt = undefined;
    _prac_d_tom_resp_allKeys = [];
    // keep track of which components have finished
    prac_dual_tom_decComponents = [];
    prac_dual_tom_decComponents.push(prac_d_tom_choice);
    prac_dual_tom_decComponents.push(prac_d_tom_resp);
    
    prac_dual_tom_decComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_dual_tom_decRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_dual_tom_dec' ---
    // get current time
    t = prac_dual_tom_decClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_d_tom_choice* updates
    if (t >= 0 && prac_d_tom_choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom_choice.tStart = t;  // (not accounting for frame time here)
      prac_d_tom_choice.frameNStart = frameN;  // exact frame index
      
      prac_d_tom_choice.setAutoDraw(true);
    }

    frameRemains = 0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom_choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom_choice.setAutoDraw(false);
    }
    
    // *prac_d_tom_resp* updates
    if (t >= 0 && prac_d_tom_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom_resp.tStart = t;  // (not accounting for frame time here)
      prac_d_tom_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { prac_d_tom_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { prac_d_tom_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { prac_d_tom_resp.clearEvents(); });
    }

    frameRemains = 0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom_resp.status = PsychoJS.Status.FINISHED;
  }

    if (prac_d_tom_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = prac_d_tom_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _prac_d_tom_resp_allKeys = _prac_d_tom_resp_allKeys.concat(theseKeys);
      if (_prac_d_tom_resp_allKeys.length > 0) {
        prac_d_tom_resp.keys = _prac_d_tom_resp_allKeys[_prac_d_tom_resp_allKeys.length - 1].name;  // just the last key pressed
        prac_d_tom_resp.rt = _prac_d_tom_resp_allKeys[_prac_d_tom_resp_allKeys.length - 1].rt;
        // was this correct?
        if (prac_d_tom_resp.keys == corr_resp_dual_prac) {
            prac_d_tom_resp.corr = 1;
        } else {
            prac_d_tom_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_dual_tom_decComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_dual_tom_decRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_dual_tom_dec' ---
    prac_dual_tom_decComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (prac_d_tom_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp_dual_prac)) {
         prac_d_tom_resp.corr = 1;  // correct non-response
      } else {
         prac_d_tom_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(prac_d_tom_resp.corr, level);
    }
    psychoJS.experiment.addData('prac_d_tom_resp.keys', prac_d_tom_resp.keys);
    psychoJS.experiment.addData('prac_d_tom_resp.corr', prac_d_tom_resp.corr);
    if (typeof prac_d_tom_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('prac_d_tom_resp.rt', prac_d_tom_resp.rt);
        routineTimer.reset();
        }
    
    prac_d_tom_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var prac_d_tom_itiComponents;
function prac_d_tom_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'prac_d_tom_iti' ---
    t = 0;
    prac_d_tom_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // Run 'Begin Routine' code from code
    if ((! prac_d_tom_resp.keys)) {
        msg = "Failed to respond";
    } else {
        msg = `Reaction Time =${Math.round(prac_d_tom_resp.rt, 3)}`;
    }
    
    prac_d_tom_fb.setText(msg);
    // keep track of which components have finished
    prac_d_tom_itiComponents = [];
    prac_d_tom_itiComponents.push(prac_d_tom_fb);
    
    prac_d_tom_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function prac_d_tom_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'prac_d_tom_iti' ---
    // get current time
    t = prac_d_tom_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *prac_d_tom_fb* updates
    if (t >= 0.0 && prac_d_tom_fb.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      prac_d_tom_fb.tStart = t;  // (not accounting for frame time here)
      prac_d_tom_fb.frameNStart = frameN;  // exact frame index
      
      prac_d_tom_fb.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (prac_d_tom_fb.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      prac_d_tom_fb.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    prac_d_tom_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function prac_d_tom_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'prac_d_tom_iti' ---
    prac_d_tom_itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _trial_start_allKeys;
var real_task_instComponents;
function real_task_instRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'real_task_inst' ---
    t = 0;
    real_task_instClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    trial_start.keys = undefined;
    trial_start.rt = undefined;
    _trial_start_allKeys = [];
    // keep track of which components have finished
    real_task_instComponents = [];
    real_task_instComponents.push(trial_inst);
    real_task_instComponents.push(trial_inst2);
    real_task_instComponents.push(trial_start);
    
    real_task_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function real_task_instRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'real_task_inst' ---
    // get current time
    t = real_task_instClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *trial_inst* updates
    if (t >= 0.0 && trial_inst.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_inst.tStart = t;  // (not accounting for frame time here)
      trial_inst.frameNStart = frameN;  // exact frame index
      
      trial_inst.setAutoDraw(true);
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (trial_inst.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      trial_inst.setAutoDraw(false);
    }
    
    // *trial_inst2* updates
    if (t >= 15 && trial_inst2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_inst2.tStart = t;  // (not accounting for frame time here)
      trial_inst2.frameNStart = frameN;  // exact frame index
      
      trial_inst2.setAutoDraw(true);
    }

    
    // *trial_start* updates
    if (t >= 15 && trial_start.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      trial_start.tStart = t;  // (not accounting for frame time here)
      trial_start.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { trial_start.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { trial_start.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { trial_start.clearEvents(); });
    }

    if (trial_start.status === PsychoJS.Status.STARTED) {
      let theseKeys = trial_start.getKeys({keyList: ['space'], waitRelease: false});
      _trial_start_allKeys = _trial_start_allKeys.concat(theseKeys);
      if (_trial_start_allKeys.length > 0) {
        trial_start.keys = _trial_start_allKeys[_trial_start_allKeys.length - 1].name;  // just the last key pressed
        trial_start.rt = _trial_start_allKeys[_trial_start_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    real_task_instComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function real_task_instRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'real_task_inst' ---
    real_task_instComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(trial_start.corr, level);
    }
    psychoJS.experiment.addData('trial_start.keys', trial_start.keys);
    if (typeof trial_start.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('trial_start.rt', trial_start.rt);
        routineTimer.reset();
        }
    
    trial_start.stop();
    // the Routine "real_task_inst" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _tom_int_resp_allKeys;
var tom_introComponents;
function tom_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_intro' ---
    t = 0;
    tom_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    tom_int_resp.keys = undefined;
    tom_int_resp.rt = undefined;
    _tom_int_resp_allKeys = [];
    // keep track of which components have finished
    tom_introComponents = [];
    tom_introComponents.push(tom_task);
    tom_introComponents.push(tom_int_resp);
    
    tom_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_intro' ---
    // get current time
    t = tom_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_task* updates
    if (t >= 0.0 && tom_task.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_task.tStart = t;  // (not accounting for frame time here)
      tom_task.frameNStart = frameN;  // exact frame index
      
      tom_task.setAutoDraw(true);
    }

    
    // *tom_int_resp* updates
    if (t >= 0.0 && tom_int_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_int_resp.tStart = t;  // (not accounting for frame time here)
      tom_int_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { tom_int_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { tom_int_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { tom_int_resp.clearEvents(); });
    }

    if (tom_int_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = tom_int_resp.getKeys({keyList: ['space'], waitRelease: false});
      _tom_int_resp_allKeys = _tom_int_resp_allKeys.concat(theseKeys);
      if (_tom_int_resp_allKeys.length > 0) {
        tom_int_resp.keys = _tom_int_resp_allKeys[_tom_int_resp_allKeys.length - 1].name;  // just the last key pressed
        tom_int_resp.rt = _tom_int_resp_allKeys[_tom_int_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_intro' ---
    tom_introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(tom_int_resp.corr, level);
    }
    psychoJS.experiment.addData('tom_int_resp.keys', tom_int_resp.keys);
    if (typeof tom_int_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('tom_int_resp.rt', tom_int_resp.rt);
        routineTimer.reset();
        }
    
    tom_int_resp.stop();
    // the Routine "tom_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _tom_s_resp_allKeys;
var tom_single_trialComponents;
function tom_single_trialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_single_trial' ---
    t = 0;
    tom_single_trialClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(16.000000);
    // update component parameters for each repeat
    tom_s_1.setImage(tom_img1);
    tom_s_2.setImage(tom_img2);
    tom_s_3.setImage(tom_img3);
    tom_s_dec.setImage(tom_dec_img);
    tom_s_resp.keys = undefined;
    tom_s_resp.rt = undefined;
    _tom_s_resp_allKeys = [];
    // keep track of which components have finished
    tom_single_trialComponents = [];
    tom_single_trialComponents.push(tom_s_1);
    tom_single_trialComponents.push(tom_s_2);
    tom_single_trialComponents.push(tom_s_3);
    tom_single_trialComponents.push(tom_s_dec);
    tom_single_trialComponents.push(tom_s_resp);
    
    tom_single_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_single_trialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_single_trial' ---
    // get current time
    t = tom_single_trialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_s_1* updates
    if (t >= 0 && tom_s_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_s_1.tStart = t;  // (not accounting for frame time here)
      tom_s_1.frameNStart = frameN;  // exact frame index
      
      tom_s_1.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_s_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_s_1.setAutoDraw(false);
    }
    
    // *tom_s_2* updates
    if (t >= 1.5 && tom_s_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_s_2.tStart = t;  // (not accounting for frame time here)
      tom_s_2.frameNStart = frameN;  // exact frame index
      
      tom_s_2.setAutoDraw(true);
    }

    frameRemains = 1.5 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_s_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_s_2.setAutoDraw(false);
    }
    
    // *tom_s_3* updates
    if (t >= 3 && tom_s_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_s_3.tStart = t;  // (not accounting for frame time here)
      tom_s_3.frameNStart = frameN;  // exact frame index
      
      tom_s_3.setAutoDraw(true);
    }

    frameRemains = 3 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_s_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_s_3.setAutoDraw(false);
    }
    
    // *tom_s_dec* updates
    if (t >= 4.5 && tom_s_dec.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_s_dec.tStart = t;  // (not accounting for frame time here)
      tom_s_dec.frameNStart = frameN;  // exact frame index
      
      tom_s_dec.setAutoDraw(true);
    }

    frameRemains = 4.5 + 11.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_s_dec.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_s_dec.setAutoDraw(false);
    }
    
    // *tom_s_resp* updates
    if (t >= 4.5 && tom_s_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_s_resp.tStart = t;  // (not accounting for frame time here)
      tom_s_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { tom_s_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { tom_s_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { tom_s_resp.clearEvents(); });
    }

    frameRemains = 4.5 + 11.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_s_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_s_resp.status = PsychoJS.Status.FINISHED;
  }

    if (tom_s_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = tom_s_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _tom_s_resp_allKeys = _tom_s_resp_allKeys.concat(theseKeys);
      if (_tom_s_resp_allKeys.length > 0) {
        tom_s_resp.keys = _tom_s_resp_allKeys[_tom_s_resp_allKeys.length - 1].name;  // just the last key pressed
        tom_s_resp.rt = _tom_s_resp_allKeys[_tom_s_resp_allKeys.length - 1].rt;
        // was this correct?
        if (tom_s_resp.keys == corr_resp) {
            tom_s_resp.corr = 1;
        } else {
            tom_s_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_single_trialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_single_trialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_single_trial' ---
    tom_single_trialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (tom_s_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp)) {
         tom_s_resp.corr = 1;  // correct non-response
      } else {
         tom_s_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(tom_s_resp.corr, level);
    }
    psychoJS.experiment.addData('tom_s_resp.keys', tom_s_resp.keys);
    psychoJS.experiment.addData('tom_s_resp.corr', tom_s_resp.corr);
    if (typeof tom_s_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('tom_s_resp.rt', tom_s_resp.rt);
        routineTimer.reset();
        }
    
    tom_s_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ITI_2000Components;
function ITI_2000RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI_2000' ---
    t = 0;
    ITI_2000Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(2.000000);
    // update component parameters for each repeat
    // keep track of which components have finished
    ITI_2000Components = [];
    ITI_2000Components.push(tom_iti);
    
    ITI_2000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ITI_2000RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI_2000' ---
    // get current time
    t = ITI_2000Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_iti* updates
    if (t >= 0.0 && tom_iti.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_iti.tStart = t;  // (not accounting for frame time here)
      tom_iti.frameNStart = frameN;  // exact frame index
      
      tom_iti.setAutoDraw(true);
    }

    frameRemains = 0.0 + 2.0 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_iti.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_iti.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ITI_2000Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITI_2000RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI_2000' ---
    ITI_2000Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _rest_resp_allKeys;
var restComponents;
function restRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'rest' ---
    t = 0;
    restClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    rest_resp.keys = undefined;
    rest_resp.rt = undefined;
    _rest_resp_allKeys = [];
    // keep track of which components have finished
    restComponents = [];
    restComponents.push(rest_15);
    restComponents.push(rest_15_2);
    restComponents.push(rest_resp);
    
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function restRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'rest' ---
    // get current time
    t = restClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *rest_15* updates
    if (t >= 0.0 && rest_15.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_15.tStart = t;  // (not accounting for frame time here)
      rest_15.frameNStart = frameN;  // exact frame index
      
      rest_15.setAutoDraw(true);
    }

    frameRemains = 0.0 + 15 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (rest_15.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      rest_15.setAutoDraw(false);
    }
    
    // *rest_15_2* updates
    if (t >= 15 && rest_15_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_15_2.tStart = t;  // (not accounting for frame time here)
      rest_15_2.frameNStart = frameN;  // exact frame index
      
      rest_15_2.setAutoDraw(true);
    }

    
    // *rest_resp* updates
    if (t >= 15 && rest_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      rest_resp.tStart = t;  // (not accounting for frame time here)
      rest_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { rest_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { rest_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { rest_resp.clearEvents(); });
    }

    if (rest_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = rest_resp.getKeys({keyList: ['space'], waitRelease: false});
      _rest_resp_allKeys = _rest_resp_allKeys.concat(theseKeys);
      if (_rest_resp_allKeys.length > 0) {
        rest_resp.keys = _rest_resp_allKeys[_rest_resp_allKeys.length - 1].name;  // just the last key pressed
        rest_resp.rt = _rest_resp_allKeys[_rest_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    restComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function restRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'rest' ---
    restComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(rest_resp.corr, level);
    }
    psychoJS.experiment.addData('rest_resp.keys', rest_resp.keys);
    if (typeof rest_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('rest_resp.rt', rest_resp.rt);
        routineTimer.reset();
        }
    
    rest_resp.stop();
    // the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _dual_task_intro_resp_allKeys;
var dual_introComponents;
function dual_introRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dual_intro' ---
    t = 0;
    dual_introClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    dual_task_intro_resp.keys = undefined;
    dual_task_intro_resp.rt = undefined;
    _dual_task_intro_resp_allKeys = [];
    // keep track of which components have finished
    dual_introComponents = [];
    dual_introComponents.push(dual_task_intro);
    dual_introComponents.push(dual_task_intro_resp);
    
    dual_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function dual_introRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dual_intro' ---
    // get current time
    t = dual_introClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dual_task_intro* updates
    if (t >= 0.0 && dual_task_intro.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_task_intro.tStart = t;  // (not accounting for frame time here)
      dual_task_intro.frameNStart = frameN;  // exact frame index
      
      dual_task_intro.setAutoDraw(true);
    }

    
    // *dual_task_intro_resp* updates
    if (t >= 0.0 && dual_task_intro_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_task_intro_resp.tStart = t;  // (not accounting for frame time here)
      dual_task_intro_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { dual_task_intro_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { dual_task_intro_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { dual_task_intro_resp.clearEvents(); });
    }

    if (dual_task_intro_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = dual_task_intro_resp.getKeys({keyList: ['space'], waitRelease: false});
      _dual_task_intro_resp_allKeys = _dual_task_intro_resp_allKeys.concat(theseKeys);
      if (_dual_task_intro_resp_allKeys.length > 0) {
        dual_task_intro_resp.keys = _dual_task_intro_resp_allKeys[_dual_task_intro_resp_allKeys.length - 1].name;  // just the last key pressed
        dual_task_intro_resp.rt = _dual_task_intro_resp_allKeys[_dual_task_intro_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    dual_introComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function dual_introRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dual_intro' ---
    dual_introComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(dual_task_intro_resp.corr, level);
    }
    psychoJS.experiment.addData('dual_task_intro_resp.keys', dual_task_intro_resp.keys);
    if (typeof dual_task_intro_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('dual_task_intro_resp.rt', dual_task_intro_resp.rt);
        routineTimer.reset();
        }
    
    dual_task_intro_resp.stop();
    // the Routine "dual_intro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var dual_iti;
var dual_itiComponents;
function dual_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'dual_iti' ---
    t = 0;
    dual_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from dual_iti_code
    dual_iti = (2.5 - Math.random());
    
    // keep track of which components have finished
    dual_itiComponents = [];
    dual_itiComponents.push(dual_iti_cross);
    
    dual_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function dual_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'dual_iti' ---
    // get current time
    t = dual_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *dual_iti_cross* updates
    if (t >= 0.0 && dual_iti_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      dual_iti_cross.tStart = t;  // (not accounting for frame time here)
      dual_iti_cross.frameNStart = frameN;  // exact frame index
      
      dual_iti_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + dual_iti - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (dual_iti_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      dual_iti_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    dual_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function dual_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'dual_iti' ---
    dual_itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "dual_iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ITI_value;
var ssst_itiComponents;
function ssst_itiRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ssst_iti' ---
    t = 0;
    ssst_itiClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    // Run 'Begin Routine' code from ssst_iti_draw
    ITI_value = (1.5 - Math.random());
    
    // keep track of which components have finished
    ssst_itiComponents = [];
    ssst_itiComponents.push(ssst_iti_cross);
    
    ssst_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function ssst_itiRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ssst_iti' ---
    // get current time
    t = ssst_itiClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ssst_iti_cross* updates
    if (t >= 0.0 && ssst_iti_cross.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_iti_cross.tStart = t;  // (not accounting for frame time here)
      ssst_iti_cross.frameNStart = frameN;  // exact frame index
      
      ssst_iti_cross.setAutoDraw(true);
    }

    frameRemains = 0.0 + ITI_value - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_iti_cross.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_iti_cross.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ssst_itiComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ssst_itiRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ssst_iti' ---
    ssst_itiComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // the Routine "ssst_iti" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _ssst_resp_allKeys;
var stop_sigComponents;
function stop_sigRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'stop_sig' ---
    t = 0;
    stop_sigClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    ssst_go.setImage(go_img);
    ssst_stop.setImage(st_img);
    ssst_resp.keys = undefined;
    ssst_resp.rt = undefined;
    _ssst_resp_allKeys = [];
    // keep track of which components have finished
    stop_sigComponents = [];
    stop_sigComponents.push(ssst_go);
    stop_sigComponents.push(ssst_stop);
    stop_sigComponents.push(ssst_resp);
    
    stop_sigComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function stop_sigRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'stop_sig' ---
    // get current time
    t = stop_sigClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *ssst_go* updates
    if (t >= 0 && ssst_go.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_go.tStart = t;  // (not accounting for frame time here)
      ssst_go.frameNStart = frameN;  // exact frame index
      
      ssst_go.setAutoDraw(true);
    }

    frameRemains = 0 + ssd - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_go.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_go.setAutoDraw(false);
    }
    
    // *ssst_stop* updates
    if (t >= (ssd - 1e-05) && ssst_stop.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_stop.tStart = t;  // (not accounting for frame time here)
      ssst_stop.frameNStart = frameN;  // exact frame index
      
      ssst_stop.setAutoDraw(true);
    }

    frameRemains = (ssd - 1e-05) + (1.25 - ssd) - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_stop.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_stop.setAutoDraw(false);
    }
    
    // *ssst_resp* updates
    if (t >= 0.0 && ssst_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      ssst_resp.tStart = t;  // (not accounting for frame time here)
      ssst_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { ssst_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { ssst_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { ssst_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 1.25 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (ssst_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      ssst_resp.status = PsychoJS.Status.FINISHED;
  }

    if (ssst_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = ssst_resp.getKeys({keyList: ['space'], waitRelease: false});
      _ssst_resp_allKeys = _ssst_resp_allKeys.concat(theseKeys);
      if (_ssst_resp_allKeys.length > 0) {
        ssst_resp.keys = _ssst_resp_allKeys[_ssst_resp_allKeys.length - 1].name;  // just the last key pressed
        ssst_resp.rt = _ssst_resp_allKeys[_ssst_resp_allKeys.length - 1].rt;
        // was this correct?
        if (ssst_resp.keys == corr_resp) {
            ssst_resp.corr = 1;
        } else {
            ssst_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    stop_sigComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function stop_sigRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'stop_sig' ---
    stop_sigComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Run 'End Routine' code from ssst_staircase
    psychoJS.experiment.addData("trial_type", trial_type);
    psychoJS.experiment.addData("ssd", ssd);
    psychoJS.experiment.addData("ssst_resp", ssst_resp.keys);
    if ((trial_type === "stop")) {
        if ((ssst_resp.corr === 1)) {
            ssd += stepsize;
        } else {
            ssd -= stepsize;
        }
        if ((ssd < minval)) {
            ssd = minval;
        }
        if ((ssd > maxval)) {
            ssd = maxval;
        }
    }
    
    // was no response the correct answer?!
    if (ssst_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp)) {
         ssst_resp.corr = 1;  // correct non-response
      } else {
         ssst_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(ssst_resp.corr, level);
    }
    psychoJS.experiment.addData('ssst_resp.keys', ssst_resp.keys);
    psychoJS.experiment.addData('ssst_resp.corr', ssst_resp.corr);
    if (typeof ssst_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('ssst_resp.rt', ssst_resp.rt);
        routineTimer.reset();
        }
    
    ssst_resp.stop();
    // the Routine "stop_sig" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tom_dual_1Components;
function tom_dual_1RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_dual_1' ---
    t = 0;
    tom_dual_1Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    tom_d_1.setImage(tom_img1);
    // keep track of which components have finished
    tom_dual_1Components = [];
    tom_dual_1Components.push(tom_d_1);
    
    tom_dual_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_dual_1RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_dual_1' ---
    // get current time
    t = tom_dual_1Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_d_1* updates
    if (t >= 0.0 && tom_d_1.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_d_1.tStart = t;  // (not accounting for frame time here)
      tom_d_1.frameNStart = frameN;  // exact frame index
      
      tom_d_1.setAutoDraw(true);
    }

    frameRemains = 0.0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_d_1.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_d_1.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_dual_1Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_dual_1RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_dual_1' ---
    tom_dual_1Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tom_dual_2Components;
function tom_dual_2RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_dual_2' ---
    t = 0;
    tom_dual_2Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    tom_d_2.setImage(tom_img2);
    // keep track of which components have finished
    tom_dual_2Components = [];
    tom_dual_2Components.push(tom_d_2);
    
    tom_dual_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_dual_2RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_dual_2' ---
    // get current time
    t = tom_dual_2Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_d_2* updates
    if (t >= 0 && tom_d_2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_d_2.tStart = t;  // (not accounting for frame time here)
      tom_d_2.frameNStart = frameN;  // exact frame index
      
      tom_d_2.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_d_2.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_d_2.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_dual_2Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_dual_2RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_dual_2' ---
    tom_dual_2Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var tom_dual_3Components;
function tom_dual_3RoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_dual_3' ---
    t = 0;
    tom_dual_3Clock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(1.500000);
    // update component parameters for each repeat
    tom_d_3.setImage(tom_img3);
    // keep track of which components have finished
    tom_dual_3Components = [];
    tom_dual_3Components.push(tom_d_3);
    
    tom_dual_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_dual_3RoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_dual_3' ---
    // get current time
    t = tom_dual_3Clock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_d_3* updates
    if (t >= 0 && tom_d_3.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_d_3.tStart = t;  // (not accounting for frame time here)
      tom_d_3.frameNStart = frameN;  // exact frame index
      
      tom_d_3.setAutoDraw(true);
    }

    frameRemains = 0 + 1.5 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_d_3.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_d_3.setAutoDraw(false);
    }
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_dual_3Components.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_dual_3RoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_dual_3' ---
    tom_dual_3Components.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _tom_d_resp_allKeys;
var tom_dual_decComponents;
function tom_dual_decRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'tom_dual_dec' ---
    t = 0;
    tom_dual_decClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    routineTimer.add(7.000000);
    // update component parameters for each repeat
    tom_choice.setImage(tom_dec_img);
    tom_d_resp.keys = undefined;
    tom_d_resp.rt = undefined;
    _tom_d_resp_allKeys = [];
    // keep track of which components have finished
    tom_dual_decComponents = [];
    tom_dual_decComponents.push(tom_choice);
    tom_dual_decComponents.push(tom_d_resp);
    
    tom_dual_decComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function tom_dual_decRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'tom_dual_dec' ---
    // get current time
    t = tom_dual_decClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *tom_choice* updates
    if (t >= 0.0 && tom_choice.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_choice.tStart = t;  // (not accounting for frame time here)
      tom_choice.frameNStart = frameN;  // exact frame index
      
      tom_choice.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_choice.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_choice.setAutoDraw(false);
    }
    
    // *tom_d_resp* updates
    if (t >= 0.0 && tom_d_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      tom_d_resp.tStart = t;  // (not accounting for frame time here)
      tom_d_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { tom_d_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { tom_d_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { tom_d_resp.clearEvents(); });
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (tom_d_resp.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      tom_d_resp.status = PsychoJS.Status.FINISHED;
  }

    if (tom_d_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = tom_d_resp.getKeys({keyList: ['1', '2', '3'], waitRelease: false});
      _tom_d_resp_allKeys = _tom_d_resp_allKeys.concat(theseKeys);
      if (_tom_d_resp_allKeys.length > 0) {
        tom_d_resp.keys = _tom_d_resp_allKeys[_tom_d_resp_allKeys.length - 1].name;  // just the last key pressed
        tom_d_resp.rt = _tom_d_resp_allKeys[_tom_d_resp_allKeys.length - 1].rt;
        // was this correct?
        if (tom_d_resp.keys == corr_resp_tom) {
            tom_d_resp.corr = 1;
        } else {
            tom_d_resp.corr = 0;
        }
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    tom_dual_decComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function tom_dual_decRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'tom_dual_dec' ---
    tom_dual_decComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // was no response the correct answer?!
    if (tom_d_resp.keys === undefined) {
      if (['None','none',undefined].includes(corr_resp_tom)) {
         tom_d_resp.corr = 1;  // correct non-response
      } else {
         tom_d_resp.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(tom_d_resp.corr, level);
    }
    psychoJS.experiment.addData('tom_d_resp.keys', tom_d_resp.keys);
    psychoJS.experiment.addData('tom_d_resp.corr', tom_d_resp.corr);
    if (typeof tom_d_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('tom_d_resp.rt', tom_d_resp.rt);
        routineTimer.reset();
        }
    
    tom_d_resp.stop();
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var _outro_resp_allKeys;
var outroComponents;
function outroRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'outro' ---
    t = 0;
    outroClock.reset(); // clock
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    // update component parameters for each repeat
    outro_resp.keys = undefined;
    outro_resp.rt = undefined;
    _outro_resp_allKeys = [];
    // keep track of which components have finished
    outroComponents = [];
    outroComponents.push(outro_text);
    outroComponents.push(outro_text2);
    outroComponents.push(outro_resp);
    
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function outroRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'outro' ---
    // get current time
    t = outroClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *outro_text* updates
    if (t >= 0.0 && outro_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outro_text.tStart = t;  // (not accounting for frame time here)
      outro_text.frameNStart = frameN;  // exact frame index
      
      outro_text.setAutoDraw(true);
    }

    frameRemains = 0.0 + 7 - psychoJS.window.monitorFramePeriod * 0.75;  // most of one frame period left
    if (outro_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      outro_text.setAutoDraw(false);
    }
    
    // *outro_text2* updates
    if (t >= 7 && outro_text2.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outro_text2.tStart = t;  // (not accounting for frame time here)
      outro_text2.frameNStart = frameN;  // exact frame index
      
      outro_text2.setAutoDraw(true);
    }

    
    // *outro_resp* updates
    if (t >= 7 && outro_resp.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      outro_resp.tStart = t;  // (not accounting for frame time here)
      outro_resp.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { outro_resp.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { outro_resp.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { outro_resp.clearEvents(); });
    }

    if (outro_resp.status === PsychoJS.Status.STARTED) {
      let theseKeys = outro_resp.getKeys({keyList: ['space'], waitRelease: false});
      _outro_resp_allKeys = _outro_resp_allKeys.concat(theseKeys);
      if (_outro_resp_allKeys.length > 0) {
        outro_resp.keys = _outro_resp_allKeys[_outro_resp_allKeys.length - 1].name;  // just the last key pressed
        outro_resp.rt = _outro_resp_allKeys[_outro_resp_allKeys.length - 1].rt;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    outroComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function outroRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'outro' ---
    outroComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(outro_resp.corr, level);
    }
    psychoJS.experiment.addData('outro_resp.keys', outro_resp.keys);
    if (typeof outro_resp.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('outro_resp.rt', outro_resp.rt);
        routineTimer.reset();
        }
    
    outro_resp.stop();
    // the Routine "outro" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
