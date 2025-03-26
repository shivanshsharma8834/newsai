import ast
import json

def json_convert(data):
    try:
        return json.loads(data.split("json\n", 1)[1])
    except json.JSONDecodeError:
        return ast.literal_eval(data.split("json\n", 1)[1])

data = '''json\n{\n \"title\": \"Record payout for world's longest-serving death row inmate\",\n \"author\": \"Kelly Ng, BBC News\",\n \"publish_date\": \"1 day ago\",\n \"summary\": \"Iwao Hakamata, an 89-year-old Japanese man, has been awarded 217 million yen in compensation after being acquitted of murder last year, following nearly 50 years on death row. Hakamata was found guilty in 1968 of killing his boss and his family, but his lawyers argued that the evidence was planted and that he had suffered 'extremely severe' mental and physical pain during his detention. The payout is the largest-ever in a criminal case in Japan, according to local media, and highlights concerns about the country's justice system, including forced confessions and lengthy retrial proceedings.\",\n \"key_points\": [\n \"Iwao Hakamata spent nearly 50 years on death row before being acquitted\",\n \"He was awarded 217 million yen in compensation, the largest-ever payout in a Japanese criminal case\",\n \"Hakamata's case raises questions about Japan's justice system, including forced confessions and lengthy retrial proceedings\",\n \"He was granted a retrial in 2014, but it took until last year for the retrial to begin\",\n \"Hakamata's sister, Hideko, fought for decades to clear his name\"\n ],\n \"keywords\": [\n \"Iwao Hakamata\",\n \"death row\",\n \"Japan\",\n \"justice system\",\n \"compensation\",\n \"acquittal\",\n \"retrial\",\n \"forced confessions\"\n ]\n}\n'''

print(type(json_convert(data)))