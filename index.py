from fasthtml.common import *
from Analyser1 import Analyser
import os

app, rt = fast_app()

@rt("/")
def get():
    return Titled("Quadratic Equation Analyzer",
        Div(
            H1("Quadratic Equation Analyzer", style="text-align: center; color: #333;"),
            P("Enter coefficients for ax² + bx + c = 0", style="text-align: center; color: #666;"),
            
            Form(
                Div(
                    Label("Coefficient a:", for_="a"),
                    Input(type="number", name="a", id="a", step="any", required=True, placeholder="Enter a"),
                    style="margin: 10px 0;"
                ),
                Div(
                    Label("Coefficient b:", for_="b"), 
                    Input(type="number", name="b", id="b", step="any", required=True, placeholder="Enter b"),
                    style="margin: 10px 0;"
                ),
                Div(
                    Label("Coefficient c:", for_="c"),
                    Input(type="number", name="c", id="c", step="any", required=True, placeholder="Enter c"), 
                    style="margin: 10px 0;"
                ),
                Div(
                    Button("Analyze", type="submit", style="background: #007bff; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer; margin: 10px 5px;"),
                    A("Refresh", href="/", style="display: inline-block; background: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px;"),
                    style="text-align: center;"
                ),
                method="post", action="/analyze"
            ),
            
            Div(id="results", style="margin-top: 30px;"),
            
            style="max-width: 600px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;"
        )
    )
@rt("/analyze", methods=["POST"])
def post(a:float,b:float,c:float):
    if a == 0:
        error_msg = "Coefficient 'a' cannot be zero for a quadratic equation!"
        return Titled("Quadratic Equation Analyzer",
            Div(
                H1("Quadratic Equation Analyzer", style="text-align: center; color: #333;"),
                Div(
                    H2("Error", style="color: #dc3545;"),
                    P(error_msg, style="color: #dc3545; font-weight: bold;"),
                    A("Go Back", href="/", style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 0;")
                ),
                style="max-width: 600px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;"
            )
        )
    
    Instance = Analyser(a,b,c)
    Analysed=Instance.AnalyserC()
    
    # Format roots display
    if len(Analysed)==9:
      return Titled("Quadratic Equation Analysis Results",
        Div(
            H1("Analysis Results", style="text-align: center; color: #333;"),
                Div(
                    H3("Nature of Discriminant:"),
                    P(f"{Analysed["Nature of Discriminant"]}")
                ),
                Div(
                    H4("Discriminant:"),
                    P(f"{Analysed['Discriminant']:.4f}")
                ),
                Div(
                    H4("Vertex:"),
                    P(f"({Analysed['Vertex X Coordinate']:.4f},{Analysed['Vertex Y Coordinate']})")
                ),
                Div(
                    H4("Intercept:"),
                    P(f"{Analysed["Intercept"]}")
                ),
                Div(
                    H4("Direction:"),
                    P(f"{Analysed["Direction"]}")
                ),
                Div(
                    H4("Nature of Roots:"),
                    P(f"{Analysed['Nature of Roots']}")
                ),
                Div(
                    H4("Root1:"),
                    P(f"{Analysed["Root1"]}")
                ),
                Div(
                    H4("Root2:"),
                    P(f"{Analysed["Root2"]}")
                ),
                  
                style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;"
            ),
            
            Div(
                A("Analyze Another", href="/", style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px;"),
                A("Refresh", href="/", style="display: inline-block; background: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px;"),
                style="text-align: center;"
            ),
            
            style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;"
        )
    if len(Analysed)==8:
        return Titled("Quadratic Equation Analysis Results",
        Div(
            H1("Analysis Results", style="text-align: center; color: #333;"),
                Div(
                    H3("Nature of Discriminant:"),
                    P(f"{Analysed["Nature of Discriminant"]}")
                ),
                Div(
                    H4("Discriminant:"),
                    P(f"{Analysed['Discriminant']:.4f}")
                ),
                Div(
                    H4("Vertex:"),
                    P(f"({Analysed['Vertex X Coordinate']:.4f},{Analysed['Vertex Y Coordinate']})")
                ),
                Div(
                    H4("Intercept:"),
                    P(f"{Analysed["Intercept"]}")
                ),
                Div(
                    H4("Direction:"),
                    P(f"{Analysed["Direction"]}")
                ),
                Div(
                    H4("Nature of Root:"),
                    P(f"{Analysed['Nature of Roots']}")
                ),
                Div(
                    H4("Root:"),
                    P(f"{Analysed["Root"]}")
                ),
                style="background: #f8f9fa; padding: 20px; border-radius: 10px; margin: 20px 0;"
            ),
            
            Div(
                A("Analyze Another", href="/", style="display: inline-block; background: #007bff; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px;"),
                A("Refresh", href="/", style="display: inline-block; background: #28a745; color: white; padding: 10px 20px; text-decoration: none; border-radius: 5px; margin: 10px 5px;"),
                style="text-align: center;"
            ),
            
            style="max-width: 800px; margin: 0 auto; padding: 20px; font-family: Arial, sans-serif;"
        )

if __name__ == "__main__":
    serve(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))
