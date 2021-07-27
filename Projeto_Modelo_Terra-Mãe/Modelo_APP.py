import pandas as pd
import numpy as np
import streamlit as st
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

#

#Criação de Dataset para a revista Terra-Mãe


programa=np.repeat(['Infraestrutura (pg 148)','Desenvolvimento Rural (pg 106 e pg 144)'
           ,'Cultura (pg 188-189)','Ciência e Tecnologia(pg 96)'
          ,'Recursos Hídricos (pg 118)',
          'Meio Ambiente e Sustentabilidade (pg 140)',
          'Desenvolvimento Produtivo (pg 132)',
          'Gestão Governamental (pg 234)'],[16,12,9,4,11,2,3,2])


data = {'Programa':  programa,
        'Evento':np.array(['Entrega de Rodovias e Estradas',
                   'BA-148 (Irecê - Ibititá - Barra dos Mendes)',
                   'BA-210 (Curaçá - BR-116)',
                   'BA-438 (Itaguaçu da Bahia - Entroncamento BA-052)',
                   'BA-504 (Itanagra - Linha Verde)',
                   'BA-290 (Itanhém - Entroncamento Vila Rezende)',
                   'BA-270 (Maiquinique - Povoado de Mangerona)',
                   'BA-263 (Licínio de Almeida -Urandi)',
                   'BA-140 e BA-160',
                   'BA-223 entre o entroncamento da BR-110 (Sátiro Dias)',
                   'BA-131, Senhor do Bonfim - Saúde - Caem - BR-324',
                   'BA-001 Duplicação (Ponte Ilhéus- Pontal)',
                   'Redução de distâncias (Construção ou Recuperação de Pontes)',
                   'Obras de construção ou recuperação de pontes concluídas-2020',
                   'Obras de construção ou recuperação de pontes EM ANDAMENTO-2020',
                   'Ponte Salvador-Itaparica (p. 158-159)',
                   'Positividade pós pandemia (crescimento)',
                   'Agricultura Familiar',
                   'Da Caatinga para o mercado europeu',
                   'Coopercuc (Cooperativa de Agropecuária Familiar de Canudos, Uauá e Curaçá)',
                   'Coopercaju (Cooperativa da Cajucultura Familiar do Nordeste da Bahia)',
                   'Coopfesba (Cooperativa da Agricultura Familiar e Economia Solidária da Bacia do Rio Salgado e Adjacências)',
                   'Coopessba (Cooperativa de Serviços Sustentáveis da Bahia)',
                   'Cooperleite (Cooperativa de Produtores de Leite do Oeste da Bahia)',
                   'Ampliação da assistência técnica e extensão rural (Ater).',
                   'Parques eólicos.',
                   'Feiras Livres Readequadas Covid-19.',
                   'Feiras Livres Readequadas Covid-19. (Investimentos SDR)',
                   'Situação pandemia:',
                   'Protocolo De Prevenção a Covid-19 do sistema estadual de bibliotecas',
                   'Premiações',
                   'Programa Aldir Blanc Bahia',
                   'Recursos da Aldir Blanc Bahia',
                   'Bate-papos sobre as culturas populares e identitárias (Virtual)',
                   'Teatro Castro Alves (Digital)',
                   'Obras e Reformas',
                   'Arquivo Público do Estado da Bahia',
                   'Telecoronavírus',
                   'Rede de Coworkings',
                   'Internet',
                   'Espaço Colaborar',
                   'Obras Estruturantes',
                   'Mais Conclusões de obras',
                   'Aquífero de Tucano',
                   'Barragem do Catolé',
                   'Barragem de Baraúnas',
                   'Segurança de Barragens',
                   'Investimentos da Embasa',
                   'Investimentos da CERB',
                   'Esgotamento Sanitário.',
                   'Esgotamento Sanitário (Mais Informações)',
                   'Obras em andamento',
                   'Preservação e outros',
                   'Projetos sociais',
                   'Informações',
                   'Energias Renováveis',
                   'Destaques',
                   'Contas',
                   'Pandemia']),
        'Descrição':np.array(['De 2019 até o momento já são cerca de 2400 km de rodovias com obras concluídas e/ou em andamento incluindo o Programa de Manutenção das Estradas Baianas (Premar). Dentre os trechos entregues recentemente em 2020 destacam-se a BA-148, BA-210 e a BA-438 (p. 150)',
'Foram recuperados 58 km da BA-148 bem no trecho da BA-432. Além de beneficiar 250 mil habitantes a obra vai facilitar o escoamento da produção do agronegócio, principal atividade na região. (p. 151)',
'92 km de recuperação da BA-210, que liga Curaçá até a BR-116, foram concluídos no município do vale São Francisco. A obra está beneficiando 70 mil moradores de Abaré, Chorrochó e Rodelas, junto com Curaçá, e contempla o escoamento da produção de grãos e do sisal, a agricultura, pecuária e o turismo na região. (p. 151)',
'Pavimentação dos 5,8 km da rodovia BA-438 que liga Itaguaçu da Bahia ao entroncamento da BA-052. O serviço beneficiou 33 mil moradores das cidades de Itaguaçu da Bahia e Central. (p. 151)',
'BA-504 Itanagra ao entroncamento da BA-099. A obra nos 20 km da rodovia está em execução. A construção da nova via vai encurtar a distância dos municípios da região de Alagoinhas com a Linha Verde no Litoral Norte Baiano. Previsão de entrega sendo Maio de 2021. (p. 152) ',
'Implantação em pelo menos 20 km da BA-290, entre Itanhém e o acesso a Vila Rezende em andamento no Extremo Sul Baiano. Previsão de Conclusão Junho de 2021. A via irá facilitar a ligação entre os estados de Minas Gerais e a Bahia e contribuirá no escoamento da produção agropecuária da região. (p. 152)',
'22 km  da BA-270, de Maiquinique até o Povoado de Mangerona, passarão por restauração. Trará um benefício para 130 mil habitantes do Centro-Sul Baiano e também o escoamento da produção agrícola e pecuária da região. (p. 152)',
'20,8 km da BA-263 estão sendo implantados entre Licínio de Almeida e Urandi, reduzirão o tempo de deslocamento entre os municípios para cerca de 30 minutos. A rodovia facilita o transporte de moradores de Licínio de Almeida,Caculé, Mortugaba, Jacaraci e Condeúba que viajam em direção a Guanambi e ao estado de Minas Gerais. Previsão de entrega em Abril de 2021. (p. 152)',
'Serviços de recuperação e manutenção pelo Premar do Entroncamento da BA-148: BR-242 (Boninal) - Piatã - Abaíra - Rio de Contas e BA-160: Ibotirama - Bom Jesus da Lapa. No total são 332,47 km que têm previsão de conclusão em março de 2022. (p. 152)',
'A BA-233, do entrocamento da BR-110 até Sátiro Dias, será restaurada. A obra será feita em 39,6 km da rodovia na região do Litoral Norte e Agreste Baiano. A recuperação da rodovia vai facilitar a ligação entre os municípios de Sátiro Dias e Inhambupe e irá beneficiar o escoamento da produção agrícola local. (p. 152)',
'A BA-131 que liga Senhor do Bonfim até a BR-324 terá os 97 km de extensão da rodovia no Centro-Norte Baiano recuperados. Os serviços na via atenderão 210 mil moradores dos municípios de Antônio Gonçalves, Pindobaçu e Jacobina, junto com Senhor do Bonfim, Saúde e Caém . (p. 153)',
'Como continuidade da ponte Ilhéus Pontal está sendo feita a duplicação da BA-001, do aeroporto de Ilhéus até o entroncamento da BR-251. Os serviços em 2,7 km de extensão se encontram com 56% de execução. Previsão de conclusão Março de 2021. A duplicação também inclui a presença de uma ciclovia (p. 154)',
'O governo da Bahia já construiu ou recuperou 7 pontes em 2020. (p. 153)',
'Ponte Ilhéus-Pontal (A ponte tem 533 m de extensão e um sistema viário com acessos ao porto de malhado, ao distrito industrial e ao futuro porto sul. A obra também inclui uma área voltada para o lazer. Investimento de cerca de 100 milhões (p. 154)); Recuperação de Ponte sobre o Rio Japara Grande, trecho Prado-Cumuruxatiba; Pontes sobre os rios Sauípe (66,60 m) e Juerana (22,60 m), trecho de Itanagra, entroncamento da BA-099 (Linha Verde); Ponte sobre o Rio Angelim - Potiraguá; Construção de Ponte sobre o Rio Grande; Rio Buranhém - Guaratinga. (p. 153)',
'Ponte sobre o Rio São Francisco (Barra - Xique-Xique) (Está em andamento com 41% de execução juntos os dois municípios reúnem aproximadamente 100 mil baianos - investimento de 133 milhões (p. 154)); Ponte sobre o Rio Itapicuru (Olindina - Itapicuru) (Uma das principais integrações com o estado de Sergipe, o equipamento que faz a ligação da BR-110 está passando por recuperação (p. 157)); Ponte sobre o Rio Verde (Mascote); Pontes do Cavaco e de Itachama (Amargosa - Brejões).(p. 153)',
'Em  2020 foi publicada a homologação do consórcio responsável pela construção e operação da ponte Salvador-Itaparica. O contrato definitivo foi assinado em 12 de novembro de 2020 pelo Governo do Estado e pelo Consórcio Chinês. A ponte terá 12,4 km com acessos em Salvador por túneis e viadutos, e em Vera Cruz, com ligação a BA-001. O investimento será de 5,4 bilhões de reais e o aporte do estado será de 1,5 bilhão de reais. O projeto irá melhorar a mobilidade entre a capital, RMS e outras regiões do estado. Não será mais necessário realizar o contorno de 100 km pela BR-101 para acessar a capital baiana. Cerca de 250 municípios serão beneficiados com essa redução. A estimativa é que sejam gerados sete mil empregos durante a construção do equipamento e cerca de 100 mil postos de trabalho em 30 anos.',
'De acordo com a SEI o setor teve um crescimento de 7,5% no primeiro semestre de 2020 em comparação com o mesmo período no ano passado. A participação do agronegócio no PIB da Bahia saltou para 24%. A Bahia lidera o ranking do Nordeste em relação ao Valor Bruto da Produção Agropecuária (VPB) com previsão de movimentar cerca de 36 bilhões de reais, apresentando alta de 8,3% em relação a 2019, ano em que o VBP do estado ficou em 33 bilhões.  (p. 147)',
'Por meio da SDR(Secretaria de Desenvolvimento Rural) foram investidos desde 2015 cerca de 1,6 bilhão de reais. Somente em 2020 cerca de 120 milhões de reais foram aplicados em ações voltadas para o fortalecimento da base de produção, acesso à terra e à tecnologia, com infraestrutura, agroindustrialização, acesso a mercados e assistência técnica e extensão rural  (p. 108)',
'A Cooperativa de Agropecuária Familiar de Canudos, Uauá e Curaçá (Coopercuc) está exportando produtos como barrinhas de doce, geleia de umbu, para países como Alemanha e França. A Coopercuc é apoiada pelo governo estadual por meio dos projetos Bahia produtiva e pró-semiárido, da companhia de desenvolvimento e ação regional (CAR/SDR). Estão sendo investidos 5,8 milhões de reais para o acesso ao novo mercado, aquisições de novos equipamentos e certificações como a de produtos veganos.   (p. 109)',
'Foi construída uma unidade agroindustrial polivalente para o beneficiamento de frutas da agricultura familiar na região semiárida baiana, aumentando a produção de 200 para 800 toneladas por ano.  (p. 109)',
'A Coopercaju está sendo beneficiada com o investimento de 2,3 milhões de reais do governo do estado, por meio do Bahia Produtiva. Os recursos são aplicados na aquisição de equipamentos e máquinas para qualificar e aumentar a produção, e no desenvolvimento de rótulos e embalagens para os produtos. (p. 110)',
'Na Coopfesba foram aplicados recursos de 3 milhões de reais por meio do Bahia Produtiva, para melhoria da qualidade do cacau nas propriedades, em equipamentos para o processo de beneficiamento e ampliação da produção e em estratégias de mercado, entre outras opções (p. 111).',
'De acordo com a Diretora da Coopessba, Carine Assunção, as vendas cresceram cerca de 30%, mesmo em pandemia, estão sendo investidos cerca de 2,5 milhões de reais, que incluem ações como ampliação da capacidade produtiva e desenvolvimento de nova marca e embalagens. (p. 112).',
'No Oeste Baiano a Cooperleite recebeu em agosto equipamentos para potencializar a atividade leiteira na região num total de 2,2 milhões de reais de investimentos. A cooperativa assinou convênio com CAR/SDR no valor de 2,3 milhões, para construção do maior laticínio da agricultura familiar na região, que deve gerar emprego e renda para 186 famílias agricultoras. A expectativa é dobrar a produção anual da Cooperleite que atualmente é de nove milhões de litros de leite. (p. 113).',
'Em 2020 foram assinados a partir do projeto Mais Ater, contratos com nove consórcios públicos da Bahia. A ação vai possibilitar o apoio para custeio com realização de atividades voltadas para a prestação do serviço de Ater de 12 mil famílias. Atualmente mais de 80 mil famílias agricultoras Baianas recebem o benefício de Ater por meio de uma das suas 3 modalidades. (p. 114).',
'Outra ação importante da SDR é a regularização fundiária das áreas de parques eólicos do Estado da Bahia, com garantia de segurança jurídica a partir da publicação da Instrução Normativa 001/2020. Já foram cadastrados 1400 imóveis e emitidos aproximadamente 900 títulos de terra. A estimativa é que com o novo modelo de corredores de vento sejam regularizados aproximadamente 1,2 milhão de hectares e aproximadamente 6 mil imóveis incluindo áreas individuais e áreas coletivas ocupadas por povos e comunidades tradicionais. (p. 115).',
'O governo lançou a campanha Viva Feira e Feira Segura, com o objetivo de apoiar os municípios a adequarem as feiras livres, orgânicas, agroecológicas e mercados municipais às normas de saúde recomendadas para o enfrentamento da covid-19.  A iniciativa já apoiou a reorganização das feiras livres de mais de 100 municípios baianos e vai chegar a 200, pela SDR estão sendo entregues 4 mil barracas e 20 mil kits feirantes, contendo máscaras de proteção, gorro, avental, frasco de álcool em gel e folheto que explica a ação e os cuidados que os feirantes devem ter. No município de Camamu, a feira foi beneficiada com 50 barracas de feira livre, e todos os equipamentos necessários na prevenção a Covid-19, em Santo Antônio de Jesus, no Recôncavo Baiano, a feira livre também recebeu investimentos onde 100 feirantes foram capacitados pelo FAEB/senar e a CAR/SDR entregou 100 barracas e 100 kits de proteção individual. (p. 116).',
'Nos últimos 5 anos foram investidos pela SDR/CAR mais de R$ 9 Milhões na aquisição de 12.260 barracas de feira livre padronizadas e investidos 41,2 milhões na construção e reforma de 54 mercados municipais, somente em 2020 os investimentos foram em 29 mercados municipais. O mercado Municipal da cidade de Santa Inês já está funcionando em pleno vapor. O investimento total, de R$ 506,4 mil, foi aplicado na melhoria de condições de infraestrutura para comercialização da produção e higienização do local, oferecendo condições sanitárias adequadas aos consumidores e para cerca de 300 comerciantes. (p. 117)',
'Foi garantido pelo Governo do Estado que os processos iniciados antes da pandemia não interrompessem a continuidade. A Secult prosseguiu com a seleção de propostas em 19 segmentos culturais, por meio dos editais setoriais 2019. Com um investimento de R$ 14 milhões do Fundo de Cultura do Estado da Bahia (FCBA), 162 proponentes com propostas pré-selecionadas nos certames estão realizando os ajustes no plano de execução, por conta da pandemia da Covid-19. Mais de 56,2% dos projetos selecionados foram do interior do estado, contemplando mais de 90% dos territórios culturais baianos. (p. 190)',
'O Protocolo de  prevenção a Covid-19 do sistema estadual de bibliotecas é referência Nacional e serviu como guia para o Ministério da Cidadania. (p. 196)',
'Puderam concorrer propostas dentro da Fundação Cultural do Estado da Bahia, na oitava edição do calendário das Artes. Foram premiadas 29 propostas por macroterritório da Bahia. Das 200 propostas selecionadas, 32 foram de Salvador, e as demais dos territórios de identidade. Cada proposta teve uma premiação de R$ 2500. (p. 191).',
'Após aprovação do plano de ação da Secult-BA, foram repassados na ordem de R$ 110 para a execução das ações emergenciais de apoio ao setor cultural. No dia 21 de Setembro de 2020, via Decreto Estadual número 20.005, foi criado o Programa Aldir Blanc Bahia (PABB), que regulamentou a LAB (Lei Aldir Blanc) em âmbito local. A Secult em parceria com a Secretaria Estadual do Trabalho, Emprego, Renda e Esporte lançou o cadastro estadual dos trabalhadores da cultura. (p. 192)',
'Os recursos federais do Programa Aldir Blanc Bahia foram aplicados em chamadas públicas, coordenadas pela Secult e suas vinculadas. Foram publicados 8 editais , divididos entre chamadas públicas e premiações, que totalizavam mais de R$ 50,7 milhões em recursos a serem investidos em propostas culturais da Bahia. (p. 192)',
'As culturas populares, cujas manifestações tradicionalmente ocorrem em comunidades espalhadas pelos territórios de identidade, as culturas de gênero e dos povos tradicionais, se reuniram no cenário digital. (p. 192).',
'O TCA precisou se manter fechado ao público, seus corpos técnicos e artísticos mantiveram-se em atividade, reinventando-se. Alguns projetos como o Domingo no TCA, Conversas Plugadas, Terça da Música e os cursos de iniciação musical do TCA foram transferidos para a internet. Os colaboradores habilitados em costura do Centro Técnico do TCA, habituados em seu cotidiano à confecção de figurinos e adereços, dedicaram-se a produzir máscaras de tecido para distribuição gratuita. Os profissionais trabalharam remotamente e foram distribuídas mais de 3,5 mil máscaras. A Orquestra Sinfônica da Bahia (Osba) lançou em março o OSBAflix, extensa programação digital. (p. 193)',
'Com entrega prevista para o primeiro semestre de 2021 as obras de restauração da Biblioteca Anísio Teixeira (BAT), em Salvador, da Biblioteca Juracy Magalhães Júnior (BJMJR/ITA) de Itaparica seguem a todo o vapor. As duas unidades da (FPC/Secult/BA) receberam um investimento de R$ 13,5 milhões para intervenções nas instalações físicas com recursos oriundos do Fundo de Defesa dos Direitos Difusos (FDDD) do Ministério da Justiça. As reformas estão sob coordenação do Instituto do Patrimônio Histórico e Artístico Nacional (IPHAN) prevendo a implantação de sistema de climatização, instalações elétricas e hidráulicas para o combate de incêndio, construção de novas edificações e áreas técnicas e administrativas. Obras de restauração no imóvel onde será a nova BAT, na avenida sete de setembro, estão na fase de implantação das estruturas metálicas de cerca de R$ 7,5 milhões, além do desenvolvimento de algumas instalações complementares, há também a reforma da biblioteca em Itaparica na ordem de R$ 5,5 milhões. (p. 194)',
'Proporcionada por um investimento de R$ 3 milhões, obtidos pela FPC/Secultba junto ao antigo ministério da cultura, a reforma é uma reivindicação da sociedade e nessa terceira etapa realizou restauração e reforma da edificação. (p. 195)',
'Por meio da SECTI (Secretaria de Ciência, Tecnologia e Inovação), com os objetivos de Monitorar o Coronavírus e esclarecer dúvidas em caso de infecção, as ferramentas Tele-Coronavírus e Monitora Covid-19 auxiliaram a população Baiana. Pelo Disque 155 mais de 110 mil pessoas foram atendidas (p. 97)',
'A Bahia está construindo a maior rede de Coworkings públicos do Brasil, com a entrega de unidades do espaço para colaborar em diversos territórios de identidade. (p. 98).',
'Levar internet em alta velocidade para beneficiar estudantes, professores e pesquisadores da Bahia é uma das missões da SECTI (Secretaria de Ciência, Tecnologia e Inovação) em parceria com a Rede Nacional de Ensino e Pesquisa ao implantar uma infovia para educação, pesquisa e inovação em diversas regiões do estado. A UNEB em Paulo Afonso foi uma das primeiras a receber o sinal de internet, que é 20 vezes mais rápido que o anterior. (p. 98)',
'O lançamento do Espaço Colaborar marca a requalificação dos antigos Centros Digitais de Cidadania (CDC) que chegarão a 24 cidades na primeira etapa e mais 17 na segunda. O espaço conta com ferramentas para o trabalho presencial e remoto, como computadores, mobílias de escritório, internet de qualidade, etc. (p. 98)',
'Sem prejuízo nas obras em andamento, dentre as principais intervenções concluídas em agosto a SIHS (Secretaria de Infraestrutura Hídrica e Saneamento) entregou à população do município de Camaçari as obras de ampliação do Sistema de Abastecimento de Água (SAA) Machadinho Norte, com investimento de mais de R$ 42 milhões a obra vai beneficiar mais de 80 mil habitantes das localidades. Foi concluído o Sistema Integrado de Abastecimento de Água (SIAA) Salvador onde foram investidos um total de R$ 9,6 milhões beneficiando cerca de 180 mil habitantes (p. 120-121).',
'Foi concluído também em 2020 a ampliação do SIAA Feira de Santana - 1a Etapa Sistema Produtor/Adutor, com um investimento de R$ 13 milhões que vai beneficiar 598.406 mil habitantes, e a ampliação do SIAA de Itaberaba, no  qual foram investidos quase 11 milhões levando água tratada para mais de 160 mil baianos, também está em andamento a obra do Sistema Adutor Ponto Novo x Pedras Altas, com investimento previsto de R$ 33 milhões, para beneficiar cerca de 195 mil habitantes em 22 municípios. (p. 121)',
'Foi construído em 2020 o sistema Araci Norte/ Tucano com um investimento de R$ 58 milhões, beneficiando cerca de 34,4 mil baianos de 77 localidades dos municípios de Araci e Tucano. Está em fase final a construção do Sistema Integrado de Abastecimento de Água Tucano Noroeste, beneficiando 58 mil pessoas. Com investimento estimado de 93 milhões de reais, a previsão de conclusão é fevereiro de 2021. (p. 121)',
'A obra irá beneficiar cerca de 350 mil habitantes com investimento de R$ 166 milhões, recursos provenientes do Governo Federal e da Embasa. A previsão de entrega é abril de 2022. (p. 122)',
'A obra irá beneficiar cerca de 65 mil habitantes com investimento de  R$ 92,6 milhões, sendo 64,5 milhões de recursos provenientes do Governo Federal e 28,1 milhões do Governo Estadual. (p. 122).',
'A Bahia possui cerca de 330 barragens cadastradas pelo instituto do meio ambiente e recursos Hídricos (Inema), na Bahia 89 barragens se enquadram na Política Nacional de Segurança de Barragens (PNSB), do total 37 são de domínio Federal (23 Dnocs e 14 Codevasf), 52 de domínio estadual, sendo 27 da Embasa e 25 da Cerb, ambas empresas vinculadas à SIHS. (p. 123)',
'Entre 2015 e 2019 a Embasa investiu  R$ 10.420.057,42 em diversas intervenções para manutenção das condições de segurança dos barramentos, incluido projetos e obras de recuperação de barramentos, estudos requeridos por lei como revisão periódica e Planos de Ação emergencial e a implementação do sistema de alerta da barragem de Pituaçu. Os investimentos adicionais previstos até 2023 em ações voltadas a segurança das barragens e atendimento dos requisitos legais estarão na ordem de R$ 25 milhões. Foi concluído em 2020 o plano de Segurança da Barragem do Cobre. Estão contratados e em andamento em 2020 com previsão de conclusão para 2021, os planos das Barragens de Água Fria I, Água Fria II, Aipim, Aracatu, Brumado, Cachoeira Grande, Crisciuma, Cristalândia, Iguape, Itapicuruzinho, Piau, Prata, Riacho de Santana, Rio da Dona, Saloméa/Floresta Azul Serra Preta e Tapera. (p. 123-124).',
'Pela CERB foram contratados em 2019, os planos das barragens do Apertado, França, Gasparino e Pedras Altas que estão em andamento com investimento previsto de R$ 1,49 milhão e previsão de conclusão em 2021. Outros 5 planos estão com processos de licitação previstos para lançamento ainda este ano, com investimento de R$ 3,48 milhões. (p. 124).',
'Dentre as principais obras, o governo do Estado entregou em agosto para a população do município de Baixa Grande as obras de implantação do novo sistema de Esgotamento Sanitário. Com investimentos de R$ 16,8 milhões, com recursos do PAC II e recursos próprios da Embasa, beneficiando 16.482 habitantes da sede do município. (p. 124-125)',
'Pela CERB foram contratados em 2019, os planos das barragens do Apertado, França, Gasparino e Pedras Altas que estão em andamento com investimento previsto de R$ 1,49 milhão e previsão de conclusão em 2021. Outros 5 planos estão com processos de licitação previstos para lançamento ainda este ano, com investimento de R$ 3,48 milhões. A SIHS em agosto também entregou a primeira etapa das obras de ampliação do Sistema de Esgotamento Sanitário Ilhéus/Pontal, com investimento de R$ 53,8 milhões, para início de execução da segunda etapa a ordem de serviço foi emitida e o investimento será de R$ 18 milhões, esse sistema de Esgotamento tem investimento total cerca de R$ 71,7 milhões, beneficiando cerca de mais de 65 mil pessoas. Outra obra concluída em Setembro de 2020 é a Ampliação do Sistema de Esgotamento Sanitário do município de Itaberaba, com investimento de R$ 57.096.697 para beneficiar cerca de 75 mil habitantes. Concluída também em Setembro, a implantação do sistema de esgotamento sanitário do município de Ipirá vai beneficiar 28,2 mil pessoas com a obra do sistema que teve investimento de R$ 39,6 milhões. (p. 124-125).',
'Em 2020, até Setembro foram concluídos sistemas de abastecimento de água em 22 localidades da região das Centrais de Seabra e Jacobina, beneficiando 11 mil pessoas com investimento de R$ 14 milhões. Em 2020 foram construídos 349 módulos sanitários domiciliares (MSD), beneficiando 1,18 mil pessoas, investimento da ordem de R$ 2,08 milhões. (p. 125).',
'São mais de 5 mil produtos de origem florestal produzidos na Bahia, a Bahia possui 700 mil hectares de plantações florestais e as empresas vinculadas à Associação Baiana das Empresas de Base Florestal (ABAF) reúnem mais de 500 mil hectares com ecossistemas florestais nativos (p. 142-143).',
'A Bracell Bahia desenvolve projetos sociais com foco em educação, empoderamento e bem-estar, que beneficiam diretamente 64 mil pessoas das comunidades do entorno de suas operações. A unidade industrial fica no polo de Camaçari e a base florestal está em 35 municípios do estado nas regiões do litoral norte e agreste. (p. 143)',
'SDE (Secretaria de Desenvolvimento Econômico) fez um balanço positivo dos números alcançados em 2020. De Janeiro a Setembro foram assinados 46 protocolos de intenções com previsão de gerar 3,6 mil empregos diretos com investimentos privados de 3,7 bilhões de reais. A perspectiva é que a Bahia encerre 2020 com 32 novos empreendimentos abertos, movimentando um total de 5,2 bilhões de reais em investimentos privados e geração de 2,2 mil postos de trabalho. No período de Janeiro a Agosto de 2020, 12 novos projetos industriais já entraram em operação, totalizando cerca de R$ 2,5 bilhões investidos e 119 mil empregos. (p. 133).',
'O setor de renováveis soma o maior montante investido até Setembro deste ano, cerca de R$ 2,4 bilhões e será responsável pela maior fatia de investimentos até o final do ano, R$ 2,7 bilhões até dezembro, a perspectiva é que sejam inauguradas 20 novas indústrias com investimento de R$ 2,9 bilhões. (p. 134).',
'O segmento de couro e calçados também merece destaque. Serão inauguradas 3 unidades fabris, sendo uma delas de tratamento de couro com investimento total de R$ 17 milhões e geração de 530 novos postos de trabalho. O setor de Informática e Eletrônicos vai ganhar duas importantes fábricas de componentes com investimentos de R$ 11 milhões e geração de 476 novos empregos. (p. 134)',
'O governo teve as contas relativas ao ano de 2019 aprovadas pelo tribunal de contas (TCE), por 5 votos a 1, em sessão ordinária realizada em agosto. (p. 236).',
'No segundo trimestre de 2020, o estado sofreu uma perda de receitas brutas estimada em R$ 1,5 bilhão em comparação ao ano passado, e a previsão de perda para o exercício alcança a expressiva soma de R$ 3 bilhões. (p. 237).',]),
        }

df = pd.DataFrame (data, columns = ['Programa','Evento','Descrição'])

################################################################################################



#Parte Inicial

st.markdown("# Aplicativo Modelo da Revista Terra Mãe: Guerra A Bahia Contra O Coronavírus")

st.markdown("Aplicativo com Informações resumidas por programa da DPE da Revista Terra Mãe")

#Image.open(r'C:\Users\atsilva\Desktop\logo_seplan.png').convert('RGB').save('new.jpeg')

img=Image.open(r'C:\Users\lmorais\Desktop\logo_seplan.jpg')

st.image(img,width=674)



#Parte Final


st.sidebar.markdown("[Fonte de Dados](https://issuu.com/abahiamudoupramim/docs/revsta_terra_mae_2020_web)")
st.sidebar.info("[Seplan](http://www.seplan.ba.gov.br/)")
st.sidebar.info("Projeto feito por [Lucas Rabelo](https://github.com/marreapato) ")
st.sidebar.text("Feito com Streamlit - Python")


