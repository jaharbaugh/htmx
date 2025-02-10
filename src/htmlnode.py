class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children if children is not None else []
        self.props = props if props is not None else {}
    def to_html(self):
        raise NotImplementedError()
    def props_to_html(self):
        props_list = []
        props_string = ""
        for k, v in self.props.items():
             props_list.append(f'{k}="{v}"')
        if props_list != []:
            props_string = " "+" ".join(props_list)
        return props_string
    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (self.tag == other.tag and 
            self.value == other.value and 
            self.children == other.children and 
            self.props == other.props)
    
    def __repr__(self):
        return(f"tag={self.tag} value={self.value} children={self.children} props={self.props}")
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, children=None, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value == None:
            raise ValueError
        if self.tag == None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag, value=None, children=None, props=None):
        super().__init__(tag, None, children, props)        
    def to_html(self):
        if self.tag == None:
            raise ValueError("Missing Tag")
        if self.children == []:
            raise ValueError("Missing Children")
        string= f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
             string += child.to_html()
        return string+f"</{self.tag}>"


        
        