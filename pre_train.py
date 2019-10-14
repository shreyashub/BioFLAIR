from flair.data import Dictionary
from flair.models import LanguageModel
from flair.trainers.language_model_trainer import LanguageModelTrainer, TextCorpus
from flair.embeddings import FlairEmbeddings
dictionary: Dictionary = Dictionary.load('chars')
#dictionary: Dictionary = language_model.dictionary
language_model = FlairEmbeddings('pubmed-forward').lm
# get your corpus, process forward and at the character level
is_forward_lm=True

corpus = TextCorpus('/content/corpus',
                    dictionary,
                    is_forward_lm,
                    character_level=True)

trainer = LanguageModelTrainer(language_model, corpus)

trainer.train('/content/language_model',
              sequence_length=10,
              mini_batch_size=10,
              max_epochs=10)

