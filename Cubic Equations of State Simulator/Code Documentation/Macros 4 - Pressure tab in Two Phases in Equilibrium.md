# "Pressure" tab in "Two Phases in Equilibrium.xlsm" file

This spreadsheet allows performing calculations with the simulator results or experimental data of the thermodynamic properties in saturated liquid–vapor mixture based on pressure.

## 1. Spreadsheet Design

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros4-1.jpg" width="1100" height="433">

*Figure 1. Spreadsheet Design of "Pressure" tab in "Two Phases in Equilibrium.xlsm".*

<img src="https://github.com/IMClick-Project/IQ/blob/main/Cubic%20Equations%20of%20State%20Simulator/Code%20Documentation/macros4-2.jpg" width="948" height="474">

*Figure 2. Controls properties.*

## 2. Excel Macro Code

```vbscript
Private Sub CLEAN_2_Click()
    Dim row As Integer ' Helper to pass rows
    FUGACITY_TEST_2.Enabled = True
    FUGACITY_TEST_2.Value = True
    EXPERIMENTAL_DATA_2.Enabled = True
    COMPUTE_2.Enabled = True
    CLEAN_2.Enabled = False
    With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Pressure")
        .Range("B3:B9").Value = ""
        .Range("L14").Value = ""
        .Range("P18").Value = ""
        .Range("A6").Value = "Reference Temperature"
        .Range("A7").Value = "Reference Pressure"
        .Range("A8").Value = "Reference Enthalpy"
        .Range("A9").Value = "Reference Entropy"
        .Range("I4").Value = "EoS Simulator"
        .Range("A11:J11").Value = ""
        .Range("L12:S12").Value = ""
        .Range("O24").Value = "V"
        .Range("O25").Value = "H"
        .Range("O26").Value = "S"
        .Range("O27").Value = "U"
        .Range("O28").Value = "A"
        .Range("O29").Value = "G"
        .Range("O22").Value = "Psat"
        .Range("O22").Select
        With ActiveCell.Characters(Start:=2, Length:=3).Font
            .Name = "Calibri"
            .FontStyle = "Regular"
            .Size = 11
            .Strikethrough = False
            .Superscript = False
            .Subscript = True
            .OutlineFont = False
            .Shadow = False
            .Underline = xlUnderlineStyleNone
            .ThemeColor = xlThemeColorLight1
            .TintAndShade = 0
            .ThemeFont = xlThemeFontMinor
        End With
        With Selection.Font
            .Color = -8762076
            .TintAndShade = 0
        End With
        Selection.Font.Bold = True
        .Range("O23").Value = "Tsat"
        .Range("O23").Select
        With ActiveCell.Characters(Start:=2, Length:=3).Font
            .Name = "Calibri"
            .FontStyle = "Regular"
            .Size = 11
            .Strikethrough = False
            .Superscript = False
            .Subscript = True
            .OutlineFont = False
            .Shadow = False
            .Underline = xlUnderlineStyleNone
            .ThemeColor = xlThemeColorLight1
            .TintAndShade = 0
            .ThemeFont = xlThemeFontMinor
        End With
        With Selection.Font
            .Color = -8762076
            .TintAndShade = 0
        End With
        Selection.Font.Bold = True
        .Range("O18").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="x,T,V,H,S"
            .IgnoreBlank = False
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        .Range("O18").Value = "x"
        .Range("L14").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(L14)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        .Range("P18").Select
        With Selection.Validation
            .Delete
            .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
            xlBetween, Formula1:="=ISBLANK(P18)"
            .IgnoreBlank = True
            .InCellDropdown = True
            .InputTitle = ""
            .ErrorTitle = ""
            .InputMessage = ""
            .ErrorMessage = ""
            .ShowInput = True
            .ShowError = True
        End With
        row = 0
        While .Cells(12 + row, 1).Value <> ""
            .Range(Cells(12 + row, 1), Cells(12 + row, 10)).Value = ""
            .Range(Cells(12 + row, 1), Cells(12 + row, 10)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            Selection.Borders(xlEdgeLeft).LineStyle = xlNone
            Selection.Borders(xlEdgeBottom).LineStyle = xlNone
            Selection.Borders(xlEdgeRight).LineStyle = xlNone
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            Selection.Borders(xlInsideHorizontal).LineStyle = xlNone
            row = row + 1
        Wend
        .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[-1]C[-11]<=R[1]C[0],R[-1]C[-11]:R[-1]C[-11])))"
        .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[-1]C[-3],2,FALSE),""-"")"
        .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[-1]C[-4],5,FALSE),""-"")"
        .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[-1]C[-5],6,FALSE),""-"")"
        .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[-1]C[-6],7,FALSE),""-"")"
        .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[-1]C[-7],8,FALSE),""-"")"
        .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[-1]C[-8],9,FALSE),""-"")"
        .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[-1]C[-9],10,FALSE),""-"")"
        .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[-3]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[-3]C[-11])))"
        .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[-3]C[-3],2,FALSE),""-"")"
        .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[-3]C[-4],5,FALSE),""-"")"
        .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[-3]C[-5],6,FALSE),""-"")"
        .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[-3]C[-6],7,FALSE),""-"")"
        .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[-3]C[-7],8,FALSE),""-"")"
        .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[-3]C[-8],9,FALSE),""-"")"
        .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[-3]C[-9],10,FALSE),""-"")"
        .Columns("A:S").EntireColumn.AutoFit
        .Columns("B:S").ColumnWidth = 16.71
        .Range("A3").Select
    End With
End Sub

Private Sub COMPUTE_2_Click()
    Dim row As Integer ' Helper to pass rows
    Dim row_data As Integer ' Number of rows of data
    Dim Tfactor As Double ' Temperature conversion factor
    Dim Pfactor As Double ' Pressure conversion factor
    Dim Vfactor As Double ' Volume conversion factor
    Dim Hfactor As Double ' Enthalpy conversion factor
    Dim Sfactor As Double ' Entropy conversion factor
    If FUGACITY_TEST_2.Value = True Then
        ' Check if it is possible to export results
        If Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Pressure").Range("A12") <> "" Then
            MsgBox "Information is found in the data area.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B1") Or Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B1") Or Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B1") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B1") Then
            MsgBox "The value of COMPOUND does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B2") Or Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B2") Or Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B2") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B2") Then
            MsgBox "The value of CUBIC EQUATION OF STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B3") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B3") Then
            MsgBox "The value of REFERENCE STATE does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B4") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B4") Then
            MsgBox "The value of REFERENCE TEMPERATURE [K] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        If Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B5") <> Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B5") Then
            MsgBox "The value of REFERENCE PRESSURE [BAR] does not match between spreadsheets.", vbExclamation
            Exit Sub
        End If
        With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Pressure")
            ' Export results
            row = 0
            row_data = 0
            If .Range("I4").Value = "EoS Simulator" Then
                Tfactor = 1
                Pfactor = 1
                Vfactor = 1
                Hfactor = 1
                Sfactor = 1
            Else
                Tfactor = 1.8
                Pfactor = 14.50377377
                Vfactor = 16.01846337
                Hfactor = 0.429922614
                Sfactor = 0.238845897
            End If
            While Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 1).Value <> ""
                If Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 3).Value <> "NaN" Then
                    .Cells(12 + row_data, 1).Value = CDbl(Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 2).Value) * Pfactor
                    .Cells(12 + row_data, 2).Value = CDbl(Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 3).Value) * Tfactor
                    .Cells(12 + row_data, 3).Value = Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 4).Value
                    .Cells(12 + row_data, 4).Value = Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 5).Value
                    .Cells(12 + row_data, 5).Value = CDbl(Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 6).Value) * Vfactor
                    .Cells(12 + row_data, 6).Value = CDbl(Workbooks("Two-Phase Envelope on a TV Diagram.xlsm").Worksheets("TV Diagram").Cells(6 + 3 * row, 7).Value) * Vfactor
                    .Cells(12 + row_data, 7).Value = CDbl(Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Cells(10 + 3 * row, 6).Value) * Hfactor
                    .Cells(12 + row_data, 8).Value = CDbl(Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Cells(10 + 3 * row, 7).Value) * Hfactor
                    .Cells(12 + row_data, 9).Value = CDbl(Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Cells(10 + 3 * row, 6).Value) * Sfactor
                    .Cells(12 + row_data, 10).Value = CDbl(Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Cells(10 + 3 * row, 7).Value) * Sfactor
                    row_data = row_data + 1
                End If
                row = row + 1
            Wend
            If row_data = 0 Then
                MsgBox "No numerical Fugacity Test results found.", vbExclamation
                Exit Sub
            End If
            If .Range("I4").Value = "EoS Simulator" Then
                .Range("A6").Value = "Reference Temperature [K]"
                .Range("A7").Value = "Reference Pressure [bar]"
                .Range("A8").Value = "Reference Enthalpy [kJ/kg]"
                .Range("A9").Value = "Reference Entropy [kJ/kg/K]"
                .Range("O24").Value = "V [m3/kg]"
                .Range("O24").Select
                With ActiveCell.Characters(Start:=5, Length:=1).Font
                    .Name = "Calibri"
                    .FontStyle = "Regular"
                    .Size = 11
                    .Strikethrough = False
                    .Superscript = True
                    .Subscript = False
                    .OutlineFont = False
                    .Shadow = False
                    .Underline = xlUnderlineStyleNone
                    .ThemeColor = xlThemeColorLight1
                    .TintAndShade = 0
                    .ThemeFont = xlThemeFontMinor
                End With
                With Selection.Font
                    .Color = -8762076
                    .TintAndShade = 0
                End With
                Selection.Font.Bold = True
                .Range("O25").Value = "H [kJ/kg]"
                .Range("O26").Value = "S [kJ/kg/K]"
                .Range("O27").Value = "U [kJ/kg]"
                .Range("O28").Value = "A [kJ/kg]"
                .Range("O29").Value = "G [kJ/kg]"
                .Range("O23").Value = "Tsat [K]"
                .Range("O22").Value = "Psat [bar]"
                .Range("D6:M6").Select
                Selection.Copy
                .Range("A11").Select
                ActiveSheet.Paste
                .Range("D6:E6").Select
                Selection.Copy
                .Range("L12").Select
                ActiveSheet.Paste
                .Range("H6:M6").Select
                Selection.Copy
                .Range("N12").Select
                ActiveSheet.Paste
                .Range("O18").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
                    xlBetween, Formula1:="x,T [K],V [m3/kg],H [kJ/kg],S [kJ/kg/K]"
                    .IgnoreBlank = False
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            Else
                .Range("A6").Value = "Reference Temperature [R]"
                .Range("A7").Value = "Reference Pressure [psia]"
                .Range("A8").Value = "Reference Enthalpy [BTU/lbm]"
                .Range("A9").Value = "Reference Entropy [BTU/lbm/R]"
                .Range("O24").Value = "V [ft3/lbm]"
                .Range("O24").Select
                With ActiveCell.Characters(Start:=6, Length:=1).Font
                    .Name = "Calibri"
                    .FontStyle = "Regular"
                    .Size = 11
                    .Strikethrough = False
                    .Superscript = True
                    .Subscript = False
                    .OutlineFont = False
                    .Shadow = False
                    .Underline = xlUnderlineStyleNone
                    .ThemeColor = xlThemeColorLight1
                    .TintAndShade = 0
                    .ThemeFont = xlThemeFontMinor
                End With
                With Selection.Font
                    .Color = -8762076
                    .TintAndShade = 0
                End With
                Selection.Font.Bold = True
                .Range("O25").Value = "H [BTU/lbm]"
                .Range("O26").Value = "S [BTU/lbm/R]"
                .Range("O27").Value = "U [BTU/lbm]"
                .Range("O28").Value = "A [BTU/lbm]"
                .Range("O29").Value = "G [BTU/lbm]"
                .Range("O23").Value = "Tsat [R]"
                .Range("O22").Value = "Psat [psia]"
                .Range("D7:M7").Select
                Selection.Copy
                .Range("A11").Select
                ActiveSheet.Paste
                .Range("D7:E7").Select
                Selection.Copy
                .Range("L12").Select
                ActiveSheet.Paste
                .Range("H7:M7").Select
                Selection.Copy
                .Range("N12").Select
                ActiveSheet.Paste
                .Range("O18").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
                    xlBetween, Formula1:="x,T [R],V [ft3/lbm],H [BTU/lbm],S [BTU/lbm/R]"
                    .IgnoreBlank = False
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            End If
            .Range("O23").Select
            With ActiveCell.Characters(Start:=2, Length:=3).Font
                .Name = "Calibri"
                .FontStyle = "Regular"
                .Size = 11
                .Strikethrough = False
                .Superscript = False
                .Subscript = True
                .OutlineFont = False
                .Shadow = False
                .Underline = xlUnderlineStyleNone
                .ThemeColor = xlThemeColorLight1
                .TintAndShade = 0
                .ThemeFont = xlThemeFontMinor
            End With
            With Selection.Font
                .Color = -8762076
                .TintAndShade = 0
            End With
            Selection.Font.Bold = True
            .Range("O22").Select
            With ActiveCell.Characters(Start:=2, Length:=3).Font
                .Name = "Calibri"
                .FontStyle = "Regular"
                .Size = 11
                .Strikethrough = False
                .Superscript = False
                .Subscript = True
                .OutlineFont = False
                .Shadow = False
                .Underline = xlUnderlineStyleNone
                .ThemeColor = xlThemeColorLight1
                .TintAndShade = 0
                .ThemeFont = xlThemeFontMinor
            End With
            With Selection.Font
                .Color = -8762076
                .TintAndShade = 0
            End With
            Selection.Font.Bold = True
            .Range("B3:B5").Value = Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B1:B3").Value
            .Range("B6") = CDbl(Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B4").Value) * Tfactor
            .Range("B7").Value = CDbl(Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B5").Value) * Pfactor
            .Range("B8").Value = CDbl(Workbooks("Two-Phase Envelope on a TH Diagram.xlsm").Worksheets("TH Diagram").Range("B6").Value) * Hfactor
            .Range("B9").Value = CDbl(Workbooks("Two-Phase Envelope on a TS Diagram.xlsm").Worksheets("TS Diagram").Range("B6").Value) * Sfactor
            ' Format
            .Range(Cells(12, 1), Cells(11 + row_data, 10)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(11, 1), Cells(11 + row_data, 1)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
            .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[" & row_data - 2 & "]C[-11]<=R[1]C[0],R[-1]C[-11]:R[" & row_data - 2 & "]C[-11])))"
            .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[" & row_data - 2 & "]C[-3],2,FALSE),""-"")"
            .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[" & row_data - 2 & "]C[-4],5,FALSE),""-"")"
            .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[" & row_data - 2 & "]C[-5],6,FALSE),""-"")"
            .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[" & row_data - 2 & "]C[-6],7,FALSE),""-"")"
            .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[" & row_data - 2 & "]C[-7],8,FALSE),""-"")"
            .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[" & row_data - 2 & "]C[-8],9,FALSE),""-"")"
            .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[" & row_data - 2 & "]C[-9],10,FALSE),""-"")"
            .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[" & row_data - 4 & "]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[" & row_data - 4 & "]C[-11])))"
            .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[" & row_data - 4 & "]C[-3],2,FALSE),""-"")"
            .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[" & row_data - 4 & "]C[-4],5,FALSE),""-"")"
            .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[" & row_data - 4 & "]C[-5],6,FALSE),""-"")"
            .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[" & row_data - 4 & "]C[-6],7,FALSE),""-"")"
            .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[" & row_data - 4 & "]C[-7],8,FALSE),""-"")"
            .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[" & row_data - 4 & "]C[-8],9,FALSE),""-"")"
            .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[" & row_data - 4 & "]C[-9],10,FALSE),""-"")"
            .Range("L14").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(A12:A" & 11 + row_data & ")", Formula2:="=MAX(A12:A" & 11 + row_data & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Range("P18").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
                xlBetween, Formula1:="=ISNUMBER(P18)"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Columns("A:S").EntireColumn.AutoFit
            .Columns("C:S").ColumnWidth = 16.71
            .Range("A3").Select
        End With
    Else
        With Workbooks("Two Phases in Equilibrium.xlsm").Worksheets("Pressure")
            ' Check if it is possible to use experimental data
            If .Range("B3") = "" Then
                MsgBox "The value of COMPOUND is empty.", vbExclamation
                Exit Sub
            End If
            If .Range("A12") = "" Then
                MsgBox "No experimental data presented.", vbExclamation
                Exit Sub
            End If
            If .Range("I4").Value = "EoS Simulator" Then
                .Range("A6").Value = "Reference Temperature [K]"
                .Range("A7").Value = "Reference Pressure [bar]"
                .Range("A8").Value = "Reference Enthalpy [kJ/kg]"
                .Range("A9").Value = "Reference Entropy [kJ/kg/K]"
                .Range("O24").Value = "V [m3/kg]"
                .Range("O24").Select
                With ActiveCell.Characters(Start:=5, Length:=1).Font
                    .Name = "Calibri"
                    .FontStyle = "Regular"
                    .Size = 11
                    .Strikethrough = False
                    .Superscript = True
                    .Subscript = False
                    .OutlineFont = False
                    .Shadow = False
                    .Underline = xlUnderlineStyleNone
                    .ThemeColor = xlThemeColorLight1
                    .TintAndShade = 0
                    .ThemeFont = xlThemeFontMinor
                End With
                With Selection.Font
                    .Color = -8762076
                    .TintAndShade = 0
                End With
                Selection.Font.Bold = True
                .Range("O25").Value = "H [kJ/kg]"
                .Range("O26").Value = "S [kJ/kg/K]"
                .Range("O27").Value = "U [kJ/kg]"
                .Range("O28").Value = "A [kJ/kg]"
                .Range("O29").Value = "G [kJ/kg]"
                .Range("O23").Value = "Tsat [K]"
                .Range("O22").Value = "Psat [bar]"
                .Range("D6:M6").Select
                Selection.Copy
                .Range("A11").Select
                ActiveSheet.Paste
                .Range("D6:E6").Select
                Selection.Copy
                .Range("L12").Select
                ActiveSheet.Paste
                .Range("H6:M6").Select
                Selection.Copy
                .Range("N12").Select
                ActiveSheet.Paste
                .Range("O18").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
                    xlBetween, Formula1:="x,T [K],V [m3/kg],H [kJ/kg],S [kJ/kg/K]"
                    .IgnoreBlank = False
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            Else
                .Range("A6").Value = "Reference Temperature [R]"
                .Range("A7").Value = "Reference Pressure [psia]"
                .Range("A8").Value = "Reference Enthalpy [BTU/lbm]"
                .Range("A9").Value = "Reference Entropy [BTU/lbm/R]"
                .Range("O24").Value = "V [ft3/lbm]"
                .Range("O24").Select
                With ActiveCell.Characters(Start:=6, Length:=1).Font
                    .Name = "Calibri"
                    .FontStyle = "Regular"
                    .Size = 11
                    .Strikethrough = False
                    .Superscript = True
                    .Subscript = False
                    .OutlineFont = False
                    .Shadow = False
                    .Underline = xlUnderlineStyleNone
                    .ThemeColor = xlThemeColorLight1
                    .TintAndShade = 0
                    .ThemeFont = xlThemeFontMinor
                End With
                With Selection.Font
                    .Color = -8762076
                    .TintAndShade = 0
                End With
                Selection.Font.Bold = True
                .Range("O25").Value = "H [BTU/lbm]"
                .Range("O26").Value = "S [BTU/lbm/R]"
                .Range("O27").Value = "U [BTU/lbm]"
                .Range("O28").Value = "A [BTU/lbm]"
                .Range("O29").Value = "G [BTU/lbm]"
                .Range("O23").Value = "Tsat [R]"
                .Range("O22").Value = "Psat [psia]"
                .Range("D7:M7").Select
                Selection.Copy
                .Range("A11").Select
                ActiveSheet.Paste
                .Range("D7:E7").Select
                Selection.Copy
                .Range("L12").Select
                ActiveSheet.Paste
                .Range("H7:M7").Select
                Selection.Copy
                .Range("N12").Select
                ActiveSheet.Paste
                .Range("O18").Select
                With Selection.Validation
                    .Delete
                    .Add Type:=xlValidateList, AlertStyle:=xlValidAlertStop, Operator:= _
                    xlBetween, Formula1:="x,T [R],V [ft3/lbm],H [BTU/lbm],S [BTU/lbm/R]"
                    .IgnoreBlank = False
                    .InCellDropdown = True
                    .InputTitle = ""
                    .ErrorTitle = ""
                    .InputMessage = ""
                    .ErrorMessage = ""
                    .ShowInput = True
                    .ShowError = True
                End With
            End If
            .Range("O23").Select
            With ActiveCell.Characters(Start:=2, Length:=3).Font
                .Name = "Calibri"
                .FontStyle = "Regular"
                .Size = 11
                .Strikethrough = False
                .Superscript = False
                .Subscript = True
                .OutlineFont = False
                .Shadow = False
                .Underline = xlUnderlineStyleNone
                .ThemeColor = xlThemeColorLight1
                .TintAndShade = 0
                .ThemeFont = xlThemeFontMinor
            End With
            With Selection.Font
                .Color = -8762076
                .TintAndShade = 0
            End With
            Selection.Font.Bold = True
            .Range("O22").Select
            With ActiveCell.Characters(Start:=2, Length:=3).Font
                .Name = "Calibri"
                .FontStyle = "Regular"
                .Size = 11
                .Strikethrough = False
                .Superscript = False
                .Subscript = True
                .OutlineFont = False
                .Shadow = False
                .Underline = xlUnderlineStyleNone
                .ThemeColor = xlThemeColorLight1
                .TintAndShade = 0
                .ThemeFont = xlThemeFontMinor
            End With
            With Selection.Font
                .Color = -8762076
                .TintAndShade = 0
            End With
            Selection.Font.Bold = True
            .Range("B4:B9").Value = "-"
            row = 0
            While .Cells(12 + row, 1) <> ""
                row = row + 1
            Wend
            row_data = row
            ' Format
            .Range(Cells(12, 1), Cells(11 + row_data, 10)).Select
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlBottom
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            With Selection
                .HorizontalAlignment = xlCenter
                .VerticalAlignment = xlCenter
                .WrapText = False
                .Orientation = 0
                .AddIndent = False
                .IndentLevel = 0
                .ShrinkToFit = False
                .ReadingOrder = xlContext
                .MergeCells = False
            End With
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlInsideVertical)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            With Selection.Borders(xlInsideHorizontal)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlThin
            End With
            .Range(Cells(11, 1), Cells(11 + row_data, 1)).Select
            Selection.Borders(xlDiagonalDown).LineStyle = xlNone
            Selection.Borders(xlDiagonalUp).LineStyle = xlNone
            With Selection.Borders(xlEdgeLeft)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeTop)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeBottom)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            With Selection.Borders(xlEdgeRight)
                .LineStyle = xlContinuous
                .Color = -8762076
                .TintAndShade = 0
                .Weight = xlMedium
            End With
            Selection.Borders(xlInsideVertical).LineStyle = xlNone
            ' Formulas of "EXACT DATA OR LINEAR INTERPOLATION" section
            .Range("L13").Formula2R1C1 = "=IF(R[1]C[0]="""",""-"",MAX(IF(R[-1]C[-11]:R[" & row_data - 2 & "]C[-11]<=R[1]C[0],R[-1]C[-11]:R[" & row_data - 2 & "]C[-11])))"
            .Range("M13").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-1]C[-12]:R[" & row_data - 2 & "]C[-3],2,FALSE),""-"")"
            .Range("N13").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-1]C[-13]:R[" & row_data - 2 & "]C[-4],5,FALSE),""-"")"
            .Range("O13").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-1]C[-14]:R[" & row_data - 2 & "]C[-5],6,FALSE),""-"")"
            .Range("P13").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-1]C[-15]:R[" & row_data - 2 & "]C[-6],7,FALSE),""-"")"
            .Range("Q13").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-1]C[-16]:R[" & row_data - 2 & "]C[-7],8,FALSE),""-"")"
            .Range("R13").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-1]C[-17]:R[" & row_data - 2 & "]C[-8],9,FALSE),""-"")"
            .Range("S13").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-1]C[-18]:R[" & row_data - 2 & "]C[-9],10,FALSE),""-"")"
            .Range("L15").Formula2R1C1 = "=IF(R[-1]C[0]="""",""-"",MIN(IF(R[-3]C[-11]:R[" & row_data - 4 & "]C[-11]>=R[-1]C[0],R[-3]C[-11]:R[" & row_data - 4 & "]C[-11])))"
            .Range("M15").Formula2R1C1 = "=IF(R[0]C[-1]<>""-"",VLOOKUP(R[0]C[-1],R[-3]C[-12]:R[" & row_data - 4 & "]C[-3],2,FALSE),""-"")"
            .Range("N15").Formula2R1C1 = "=IF(R[0]C[-2]<>""-"",VLOOKUP(R[0]C[-2],R[-3]C[-13]:R[" & row_data - 4 & "]C[-4],5,FALSE),""-"")"
            .Range("O15").Formula2R1C1 = "=IF(R[0]C[-3]<>""-"",VLOOKUP(R[0]C[-3],R[-3]C[-14]:R[" & row_data - 4 & "]C[-5],6,FALSE),""-"")"
            .Range("P15").Formula2R1C1 = "=IF(R[0]C[-4]<>""-"",VLOOKUP(R[0]C[-4],R[-3]C[-15]:R[" & row_data - 4 & "]C[-6],7,FALSE),""-"")"
            .Range("Q15").Formula2R1C1 = "=IF(R[0]C[-5]<>""-"",VLOOKUP(R[0]C[-5],R[-3]C[-16]:R[" & row_data - 4 & "]C[-7],8,FALSE),""-"")"
            .Range("R15").Formula2R1C1 = "=IF(R[0]C[-6]<>""-"",VLOOKUP(R[0]C[-6],R[-3]C[-17]:R[" & row_data - 4 & "]C[-8],9,FALSE),""-"")"
            .Range("S15").Formula2R1C1 = "=IF(R[0]C[-7]<>""-"",VLOOKUP(R[0]C[-7],R[-3]C[-18]:R[" & row_data - 4 & "]C[-9],10,FALSE),""-"")"
            .Range("L14").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateDecimal, AlertStyle:=xlValidAlertStop, Operator _
                :=xlBetween, Formula1:="=MIN(A12:A" & 11 + row_data & ")", Formula2:="=MAX(A12:A" & 11 + row_data & ")"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Range("P18").Select
            With Selection.Validation
                .Delete
                .Add Type:=xlValidateCustom, AlertStyle:=xlValidAlertStop, Operator:= _
                xlBetween, Formula1:="=ISNUMBER(P18)"
                .IgnoreBlank = True
                .InCellDropdown = True
                .InputTitle = ""
                .ErrorTitle = ""
                .InputMessage = ""
                .ErrorMessage = ""
                .ShowInput = True
                .ShowError = True
            End With
            .Columns("A:S").EntireColumn.AutoFit
            .Columns("C:S").ColumnWidth = 16.71
            .Range("A3").Select
        End With
    End If
    FUGACITY_TEST_2.Enabled = False
    EXPERIMENTAL_DATA_2.Enabled = False
    COMPUTE_2.Enabled = False
    CLEAN_2.Enabled = True
End Sub
```