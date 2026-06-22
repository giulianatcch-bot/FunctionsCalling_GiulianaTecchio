### AULAB HACKADEMY - Specializzazione Coding AI

# Applicazione didattica: 
# Chatbot VerdePower Italia

## Competenze Didattiche Acquisibili

Questo progetto offre un'eccellente opportunità per gli studenti di comprendere come diverse tecnologie e concetti si integrano in un'applicazione del mondo reale, combinando aspetti di programmazione tradizionale con moderne tecnologie di AI.


## Descrizione Generale dell'Applicazione

L'applicazione è un chatbot intelligente sviluppato per VerdePower Italia, che implementa un assistente virtuale chiamato Sofia utilizzando le API di OpenAI e il framework Chainlit. Il sistema è progettato per interagire con i clienti, rispondere alle loro domande basandosi su una knowledge base aziendale, e gestire l'invio automatico di email di benvenuto quando i clienti forniscono il loro indirizzo email.

L'architettura dell'applicazione segue i principi della programmazione orientata agli oggetti e utilizza moderne pratiche di sviluppo Python, inclusa la gestione sicura delle configurazioni attraverso variabili d'ambiente.

## Descrizione Dettagliata del Funzionamento

### 1. Struttura dell'Applicazione
L'applicazione è organizzata in tre file principali:
- `__init__.py`: Punto di ingresso dell'applicazione che gestisce l'inizializzazione e il flusso della chat
- `chat_logic.py`: Contiene la logica principale del chatbot
- `create_assistant.py`: Script per la creazione e configurazione dell'assistente OpenAI

### 2. Componenti Chiave

#### Inizializzazione (`__init__.py`)
- Carica le configurazioni da file .env (OPENAI_KEY, RESEND_KEY, ASSISTANT_ID)
- Definisce gli handler per l'avvio della chat e la gestione dei messaggi
- Utilizza il framework Chainlit per l'interfaccia utente

#### Logica di Chat (`chat_logic.py`)
- Classe `ChatLogic`: Gestisce l'interazione con le API OpenAI
- Gestione dei thread di conversazione
- Processamento dei messaggi
- Invio delle email attraverso il servizio Resend
- Gestione delle chiamate a funzioni dell'assistente

#### Creazione Assistente (`create_assistant.py`)
- Configura l'assistente Sofia con le sue capacità
- Imposta gli strumenti disponibili (invio email e ricerca nei file)
- Gestisce il caricamento della knowledge base aziendale
- Configura il vector store per la ricerca semantica




