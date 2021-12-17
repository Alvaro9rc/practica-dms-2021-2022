#!/usr/bin/env python3

from dms2122backend.data.config.backendconfiguration import BackendConfiguration
from dms2122backend.data.db.schema import Schema
from dms2122backend.service.questionservices import QuestionServices
from dms2122backend.service.answerservices import AnswersServices

cfg: BackendConfiguration = BackendConfiguration()
cfg.load_from_file(cfg.default_config_file())
db: Schema = Schema(cfg)

QuestionServices.create_question('Question 1','Who discovered America?','Pedro Picapiedra','Christopher Columbus','Cristiano Ronaldo',2,2.0,0.15,db)
QuestionServices.create_question('Question 2','When did Spain won the world cup?','2010','2011','2030',1,2.0,0.15,db)
QuestionServices.create_question('Question 3','Who is older?','Lebron James','The Pope Francis','Queen Elizabeth II',3,2.0,0.15,db)
QuestionServices.create_question('Question 4','Who won the 2021 F1 world championship?','Max Verstappen','Lewis Hamilton','Michael Schumacher',1,2.0,0.15,db)
QuestionServices.create_question('Question 5','How many bones are in the human body?','10','500','206',3,2.0,0.15,db)
QuestionServices.create_question('Question 6','Is programming boring?','Yes','No','I´d rather not answer',2,2.0,0.15,db)
QuestionServices.create_question('Question 7','Who sings poker face?','Lady Gaga','Paquirrin','David Bustamante',1,2.0,0.15,db)