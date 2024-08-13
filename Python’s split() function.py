# Tokenization using Python’s split() function
text = """This tool is in an a beta stage. Alexa developers can use Get Metrics API to seamlessly 
analyze metrics. It also supports custom skill models, prebuilt Flash Briefing models, and the Smart 
Home Skill API. You can use this tool for creation of monitors, alarms, and dashboards that spotlight 
changes. The release of these three tools will enable developers to create visually rich skills for 
Alexa devices with screens. Amazon describes these tools as the collection of tech and tools for 
creating visually rich and interactive voice experiences.""" 
# Tokenization using split() with improved handling of periods within sentences 
sentences = text.split(". ")  # Split on periods followed by a space 
for sentence in sentences: 
# Optionally, remove leading/trailing whitespace (customizable) 
    sentence = sentence.strip() 
    print(sentence)