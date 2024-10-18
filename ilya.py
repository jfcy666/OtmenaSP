from natasha import Segmenter, MorphVocab, Doc, NewsEmbedding, NewsMorphTagger

def to_dative_case(full_name):
    segmenter = Segmenter()
    embedding = NewsEmbedding()
    morph_tagger = NewsMorphTagger(embedding)
    
    doc = Doc(full_name)
    doc.segment(segmenter)
    doc.tag_morph(morph_tagger)  # Передаем tagger

    dative_parts = []
    
    for token in doc.tokens:
        # Получаем дательный падеж
        dative_form = token.morph.inflect({'datv'})
        if dative_form:
            dative_parts.append(dative_form.word)
        else:
            dative_parts.append(token.text)  # Если не удалось преобразовать, добавляем оригинал

    return ' '.join(dative_parts)

if __name__ == "__main__":
    full_name = input("Введите ФИО в именительном падеже: ")
    dative_name = to_dative_case(full_name)
    print("ФИО в дательном падеже:", dative_name)
